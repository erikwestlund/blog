<script>
import FileUploadMixin from './FileUploadMixin'

export default {
    mixins: [FileUploadMixin],
    data () {
        return {
            uploadedImages: [],
            uploading_image: false,
            submittingType: 'uploading_image',
            imageToUpload: null,
            showUploadImagePrompt: false,
            markdownEditorPosition: null
        }
    },
    created () {
        Event.listen('newImageUploaded', (newImageUpload) => this.addNewImageToUploads(newImageUpload))
    },
    methods: {
        uploadImage () {
            this.uploading_image = true
            this.imageFileUpload(this.imageToUpload)
                .then(response => {
                    let newImageUploaded = response.data.data.image

                    newImageUploaded.markdownEditorPosition = this.markdownEditorPosition

                    Event.fire('newImageUploaded', newImageUploaded)

                    this.imageToUpload = null
                    this.markdownEditorPosition = null
                    this.showUploadImagePrompt = false
                    this.uploading_image = false
                })
        },
        addNewImageToUploads (newImageUploaded) {
            this.uploadedImages.push(newImageUploaded)
        },

        cloudinaryUpload (url, public_name) {

        }
    }

}
</script>
