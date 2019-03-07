<script>
import FileUploadMixin from './FileUploadMixin'

export default {
    mixins: [FileUploadMixin],
    data () {
        return {
            uploadedImages: [],
            uploading_image: false,
            submittingType: 'uploading_image',
            showUploadImagePrompt: false,
            markdownEditorPosition: null
        }
    },
    created () {
        Event.listen('newImageUploaded', (newImageUpload) => this.addNewImageToUploads(newImageUpload))
    },
    methods: {
        replaceFilenameWithUrl (newImageUploaded) {
            this.form.body = this.form.body.replace(
                new RegExp(`(!\\[.*?\\]\\()(${newImageUploaded.uploadPosition})(\\))`),
                (whole, a, b, c) => {
                    return a + newImageUploaded.url + c
                })
        },

        uploadImage (imageToUpload, uploadPosition = null) {
            this.uploading_image = true

            return this.imageFileUpload(imageToUpload)
                .then(response => {
                    let newImageUploaded = response.data.data.image
                    newImageUploaded.originalImage = imageToUpload
                    newImageUploaded.uploadPosition = uploadPosition

                    this.replaceFilenameWithUrl(newImageUploaded)

                    Event.fire('newImageUploaded', newImageUploaded)

                    this.showUploadImagePrompt = false
                    this.uploading_image = false

                    flash('Image uploaded successfully.')
                })
                .catch(errors => {
                    this.showUploadImagePrompt = false
                    this.uploading_image = false
                    flash('Image upload failed.', 'danger')
                })
        },

        addNewImageToUploads (newImageUploaded) {
            this.uploadedImages = _.clone(this.uploadedImages)

            this.uploadedImages.push(newImageUploaded)
        },

        deleteImageFromServer (imageId) {
            axios.delete('/admin/images/' + imageId)
                .then(response => {
                    flash('Image deleted from server.')
                })
                .catch(errors => {
                    flash('Failed to delete image from server.', 'danger')
                })
        },

        deleteUploadRecord (matchingUpload) {
            this.uploadedImages = _.reject(this.uploadedImages, (upload) => {
                return upload === matchingUpload
            })

            Event.fire('imageDeletedFromUploads', this.uploadedImages)
        },

        deleteImageFromUploads (image) {
            let matchingUpload = _.find(this.uploadedImages, (uploadedImage) => {
                return uploadedImage.uploadPosition === image[1]
            })

            if (matchingUpload) {
                this.deleteUploadRecord(matchingUpload)
            }

            if (matchingUpload && matchingUpload.hasOwnProperty('id')) {
                this.deleteImageFromServer(matchingUpload.id)
            }
        }
    }
}
</script>
