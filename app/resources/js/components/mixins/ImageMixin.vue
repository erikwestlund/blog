<script>
import CopyMixin from './CopyMixin'

export default {
    mixins: [CopyMixin],
    data () {
        return {
            state: window.State
        }
    },
    computed: {
        cloudinary () {
            return this.imageSettings.cloudinary
        },
        imageSettings () {
            return this.state.settings.images
        }
    },
    methods: {
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

        deleteUploadRecord (upload) {
            this.uploadedImages = _.reject(this.uploadedImages, (thisUpload) => {
                return thisUpload === upload
            })

            Event.fire('imageDeletedFromUploads', this.uploadedImages)
        },

        copyThumbnailUrl (url, size) {
            this.copyUrl(this.getThumbnailUrl(url, size), 'Image')
        },

        getCloudinaryImageFetchUrl (url, width) {
            return `https://res.cloudinary.com/${this.cloudinary.account}/image/fetch/w_${width}/${url}`
        },

        getThumbnailUrl (url, type = 'small') {
            return this.cloudinary.on
                ? this.getCloudinaryImageFetchUrl(url, this.imageSettings.thumbnail_widths[type])
                : url
        }
    }
}
</script>
