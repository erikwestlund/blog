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
            }
        },
        methods: {
            uploadImage() {
                this.uploading_image = true;
                this.fileUpload(this.imageToUpload)
                    .then(response => {
                        this.uploadedImages.push(response.data.data)

                        this.imageToUpload = null
                        this.uploading_image
                        this.showUploadImagePrompt = false
                    })

            },

            cloudinaryUpload(url, public_name) {

            },
        },
    }
</script>