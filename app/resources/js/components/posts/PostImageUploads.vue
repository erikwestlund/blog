<template>
    <div>
        <div class="flex">
            <h2
                    v-if="showHeader"
                    class="font-normal"
            >
                <fa-icon
                        class="fax-2x text-grey mr-2"
                        :icon="['far', 'images']"
                />
                Images
            </h2>
            <button
                    class="ml-auto btn btn-white hover:bg-grey-lightest hover:border-grey p-2"
                    @click.prevent="showUploadImagePrompt = true"
            >
                <fa-icon
                        class="mr-2"
                        :icon="['far', 'upload']"
                />
                Upload an Image
            </button>
        </div>

        <ul
                v-if="hasUploads"
                class="list-unstyled pl-0"
        >
            <li
                    v-for="upload in uploadedImages"
                    :key="upload.id"
                    class="flex mt-5"
            >
                <img
                        class="mr-2 rounded-lg border border-grey-light max-w-thumbnail max-h-thumbnail"
                        :src="upload.url"
                >
                <div class="flex-auto">
                    <input
                            readonly
                            class="text-grey-dark w-100 text-input self-start p-1"
                            :value="upload.url"
                    >
                    <button class="btn btn-sm btn-white">
                        Cloudinary
                    </button>
                </div>
            </li>
        </ul>
        <div
                v-else
                class="text-grey-darker mt-5"
        >
            No images have been uploaded.
        </div>
        <modal
                :show="showUploadImagePrompt"
                no-footer
                @close="showUploadImagePrompt = false"
        >
            <h3 slot="header">
                Upload an Image
            </h3>

            <div
                    slot="body"
            >
                <div class="mb-5">
                    <input
                            v-show="! uploading_image"
                            id="file"
                            ref="imageUpload"
                            type="file"
                            @change="triggerImageUpload()"
                            accept=".gif,.jpg,.jpeg,.png"
                    >
                </div>
                <submitting-label
                        v-if="uploading_image"
                        class="text-grey mb-20"
                        type="uploading_image"
                />
            </div>
        </modal>
    </div>
</template>

<script>
    import Modal from '../ui/Modal'
    import FileUploadImageMixin from '../mixins/FileUploadImageMixin'
    import SubmittingMixin from '../mixins/SubmittingMixin'

    export default {
        components: {
            Modal
        },
        mixins: [FileUploadImageMixin, SubmittingMixin],
        props: {
            initImageUploads: {
                type: Array,
                default: () => {
                    return []
                }
            },
            showHeader: {
                type: Boolean,
                default: true
            }
        },
        data() {
            return {
                uploadedImages: this.initImageUploads
            }
        },
        computed: {
            hasUploads() {
                return !_.isEmpty(this.uploadedImages)
            }
        },
        created() {
            Event.listen('uploadedImageTrashed', (image) => this.deleteImageFromUploads(image))
        },
        methods: {
            triggerImageUpload() {
                this.uploading_image = true
                this.imageFileUpload(this.$refs.imageUpload.files[0])
                    .then(response => {
                        this.showUploadImagePrompt = false
                        this.uploading_image = false
                        this.$refs.imageUpload.value = ''

                        let newImageUploaded = response.data.data.image
                        Event.fire('newImageUploaded', newImageUploaded)

                        flash('Image uploaded successfully.')
                    })
                    .catch(error => {
                        this.$refs.imageUpload.value = ''
                        this.showUploadImagePrompt = false
                        flash(error.response.data.hasOwnProperty('data') && error.response.data.data.message || 'Image upload failed.', 'danger')
                    })
            },
            loadInitialImages() {
                this.uploadedImages = _.clone(this.initImageUploads)
            }
        },
        watch: {
            'initImageUploads': 'loadInitialImages'
        }
    }
</script>

<style scoped>

</style>
