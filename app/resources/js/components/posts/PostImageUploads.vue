<template>
    <div>
        <div class="flex">
            <h2
                    v-if="showHeader"
                    class="font-normal"
            >
                <fa-icon
                        class="fax-2x text-grey mr-2"
                        :icon="['far', 'cloud-upload']"
                />
                Uploaded Images
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
                            @change="setImage()"
                    >
                </div>

                <button
                        :disabled="uploading_image"
                        v-if="imageToUpload"
                        class="btn btn-blue"
                        @click.prevent="uploadImage()"
                >
                    <submitting-label
                            v-if="uploading_image"
                            type="uploading_image"
                    />
                    <span v-else>
                        <fa-icon
                                class="mr-2"
                                :icon="['far', 'upload']"
                        />
                        Upload
                    </span>
                </button>
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
            Event.listen('uploadedImageDeleted', (identifier) => this.deleteImageFromUploads(identifier))
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
            setImage() {
                this.imageToUpload = this.$refs.imageUpload.files[0]
            }
        }
    }
</script>

<style scoped>

</style>
