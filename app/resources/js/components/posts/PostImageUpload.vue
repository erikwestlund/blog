<template>
    <div>
        <div class="max-w-tiny-thumbnail mr-3">
            <img
                    class="block rounded-lg shadow"
                    :src="getThumbnailUrl(upload.url, 'tiny')"
            >
            <div class="text-grey text-sm mt-2 flex items-center pr-2" v-show="hasHeightAndWidth">
                <span class="mr-2">{{ upload.width }}x{{ upload.height }}</span>
                            <fa-icon @click="deleteImageUpload(upload)"
                     class="ml-auto cursor-pointer text-grey hover:text-red-dark"
                     :icon="['far', 'trash']"/>
            </div>
        </div>
        <div class="flex-auto">
            <div class="flex mb-2 items-center">
                <input
                        readonly
                        class="border-grey-light bg-grey-lighter text-grey-dark w-100 text-input self-start p-1 mb-0 mr-1 h-7"
                        :value="upload.url"
                >
                <button class="btn btn-grey border-grey-light hover:bg-grey hover:border-grey py-1"
                        @click="copyUrl(upload.url)">
                    <fa-icon :icon="['far', 'cut']"/>
                </button>
            </div>
            <div class="mt-2 flex md:items-center">
                <fa-icon class="mr-2 mt-3 md:mt-0 text-grey" :icon="['far', 'cut']"/>
                <div class="flex flex-wrap">
                    <button class="btn btn-sm btn-grey border-grey-light hover:bg-grey hover:border-grey py-2 font-normal text-sm h-7 mr-2 mb-2 md:mb-0"
                            @click="copyThumbnailUrl(upload.url, 'tiny')"
                    >
                        Tiny Thumb
                    </button><!--
                 -->
                    <button class="btn btn-sm btn-grey border-grey-light hover:bg-grey hover:border-grey py-2 font-normal text-sm h-7 mr-2 mb-2 md:mb-0"
                            @click="copyThumbnailUrl(upload.url, 'small')"
                    >
                        Sm. Thumb
                    </button><!--
                 -->
                    <button class="btn btn-sm btn-grey border-grey-light hover:bg-grey hover:border-grey py-2 font-normal text-sm h-7 mr-2 mb-2 md:mb-0"
                            @click="copyThumbnailUrl(upload.url, 'large')"
                    >
                        Lg. Thumb
                    </button><!--
                 -->
                    <button v-for="width in imageSettings.widths"
                            v-show="upload.width > width"
                            :key="width"
                            class="btn btn-sm btn-grey border-grey-light hover:bg-grey hover:border-grey py-2 font-normal text-sm mr-2 mb-2 h-7 md:mb-0"
                            @click="copyUrl(getCloudinaryImageFetchUrl(upload.url, width))"
                    >
                        {{ width }} px.
                    </button><!--
                 --><input
                        type="number"
                        class="inline border-grey-light text-grey-dark w-20 text-sm text-input self-start px-1 py-2 h-7 mb-0 mr-1"
                        v-model="customWidth"
                        placeholder="Custom"
                ><!--
                 -->
                    <button v-show="customWidth"
                            class="btn btn-grey border-grey-light hover:bg-grey hover:border-grey py-2"
                            @click="copyUrl(getCloudinaryImageFetchUrl(upload.url, customWidth))">
                        <fa-icon :icon="['far', 'cut']"/>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Image from '../mixins/ImageMixin'

    export default {
        mixins: [Image],
        props: {
            upload: {
                type: Object,
                required: true,
            },
        },
        data() {
            return {
                customWidth: null
            }
        },
        computed: {
          hasHeightAndWidth() {
              return this.upload.width && this.upload.height
          }
        },

        methods: {
            deleteImageUpload(upload) {
                Event.fire('uploadedImageTrashed', upload)
            }
        }
    }
</script>