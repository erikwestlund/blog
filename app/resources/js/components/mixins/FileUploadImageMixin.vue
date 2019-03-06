<script>
    import FileUploadMixin from './FileUploadMixin'

    export default {
        mixins: [FileUploadMixin],
        data() {
            return {
                uploadedImages: [],
                uploading_image: false,
                submittingType: 'uploading_image',
                showUploadImagePrompt: false,
                markdownEditorPosition: null
            }
        },
        created() {
            Event.listen('newImageUploaded', (newImageUpload) => this.addNewImageToUploads(newImageUpload))
        },
        methods: {
            uploadImage(imageToUpload, uploadPosition = null) {
                this.uploading_image = true

                return this.imageFileUpload(imageToUpload)
                    .then(response => {
                        let newImageUploaded = response.data.data.image
                        newImageUploaded.originalImage = imageToUpload
                        newImageUploaded.uploadPosition = uploadPosition

                        const reg_str = "/(!\\[\[^\\[\]*?\\]\(?=\\(\)\)\\(\\s*\(" + newImageUploaded.uploadPosition + "\)\\s*\\)/g"
                        const reg = eval(reg_str);
                        this.form.body = this.form.body.replace(reg, "$1(" + newImageUploaded.url + ")")

                        // this.$refs.markdownEditor.$img2Url(newImageUploaded.uploadPosition, newImageUploaded.url)
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

            addNewImageToUploads(newImageUploaded) {
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

            deleteImageFromUploads(image) {
                let matchingUpload = _.find(this.uploadedImages, (uploadedImage) => {
                    return uploadedImage.uploadPosition === image[1]
                })

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
