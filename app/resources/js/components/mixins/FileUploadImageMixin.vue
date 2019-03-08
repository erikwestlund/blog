<script>
import FileUploadMixin from './FileUploadMixin'
import Image from './ImageMixin'

export default {
    mixins: [FileUploadMixin, Image],
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

    }
}
</script>
