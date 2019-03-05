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
        uploadImage (markdownEditorPosition = null) {
            this.uploading_image = true
            this.imageFileUpload(this.imageToUpload)
                .then(response => {
                    let newImageUploaded = response.data.data.image
console.log(markdownEditorPosition)
                    if(Number.isInteger(markdownEditorPosition)) {
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
        addNewImageToUploads (newImageUploaded) {
            this.uploadedImages.push(newImageUploaded)
        },
        deleteImageFromUploads(identifier) {
            if(Number.isInteger(identifier)) {
                this.uploadedImages = _.filter(this.uploadedImages, (upload) => {
                    return upload.markdownEditorPosition !== identifier
                })
            } else if (typeof identifier === 'string' || identifier instanceof String) {
                console.log('isstring')
                this.uploadedImages = _.filter(this.uploadedImages, (upload) => {
                    return upload.url !== identifier
                })
            }
        },

        cloudinaryUpload (url, public_name) {

        }
    }

}
</script>
