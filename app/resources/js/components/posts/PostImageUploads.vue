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
                    class="flex mt-5"
            >
                <img
                        class="mr-2 rounded-lg border border-grey-light max-w-full md:max-w-thumbnail max-h-full md:max-h-thumbnail"
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
                            id="file"
                            ref="imageUpload"
                            type="file"
                            v-show="! uploading_image"
                            @change="triggerImageUpload()"
                    >
                </div>
                <submitting-label
                        class="text-grey mb-10"
                        v-if="uploading_image"
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
        created() {
            Event.listen('uploadedImageTrashed', (image) => this.deleteImageFromUploads(image))
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
        methods: {
            triggerImageUpload() {
                this.uploadImage(this.$refs.imageUpload.files[0])
                    .then(response => {
                        flash('Image uploaded successfully.')
                    })
                    .catch(errors => {
                        flash('Image upload failed.', 'danger')
                    })
            },
        }
    }
</script>

<style scoped>

</style>
