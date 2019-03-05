<script>
    import FileUploadMixin from './FileUploadMixin'

    export default {
        mixins: [FileUploadMixin],
        data() {
            return {
                uploadedImages: [],
                uploading_image: false,
                submittingType: 'uploading_image',
                imageToUpload: null,
                showUploadImagePrompt: false,
                markdownEditorPosition: null
            }
        },
        created() {
            Event.listen('newImageUploaded', (newImageUpload) => this.addNewImageToUploads(newImageUpload))
        },
        methods: {
            uploadImage(markdownEditorPosition = null) {
                this.uploading_image = true
                this.imageFileUpload(this.imageToUpload)
                    .then(response => {
                        let newImageUploaded = response.data.data.image

                        console.log('m', markdownEditorPosition)

                        if (Number.isInteger(markdownEditorPosition)) {
                            newImageUploaded.markdownEditorPosition = markdownEditorPosition
                        }

                        Event.fire('newImageUploaded', newImageUploaded)

                        this.imageToUpload = null
                        this.showUploadImagePrompt = false
                        this.uploading_image = false
                    })
                    .catch(errors => {
                        this.imageToUpload = null
                        this.showUploadImagePrompt = false
                        this.uploading_image = false
                        flash('Could not upload image', 'danger')
                    })
            },
            addNewImageToUploads(newImageUploaded) {
                console.log('here')
                this.uploadedImages.push(newImageUploaded)
            },

            deleteImageFromServer(imageId) {
                axios.delete("/admin/images/" + imageId)
                    .then(response => {
                        flash('Image deleted from server.')
                    })
                    .catch(errors => {
                        flash('Failed to delete image from server.')
                    })
            },

            deleteUploadRecord(matchingUpload) {
                this.uploadedImages = _.reject(this.uploadedImages, (upload) => {
                    return upload == matchingUpload
                })

                Event.fire('imageDeletedFromUploads', this.uploadedImages)
            },

            deleteImageFromUploads(identifier) {
console.log('searching', identifier)
                if (Number.isInteger(identifier)) {
                    var matchingUpload = _.find(this.uploadedImages, (upload) => {
                        return upload.markdownEditorPosition === identifier
                    })
                } else if (typeof identifier === 'string' || identifier instanceof String) {
                    var matchingUpload = _.find(this.uploadedImages, (upload) => {
                        return upload.url === identifier
                    })
                }

                console.log('found', matchingUpload)

                if (matchingUpload) {
                    this.deleteUploadRecord(matchingUpload)
                }

                if (matchingUpload && matchingUpload.hasOwnProperty("id")) {
                    this.deleteImageFromServer(matchingUpload.id)
                }

            },

            cloudinaryUpload(url, public_name) {

            }
        }

    }
</script>
