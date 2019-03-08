<template>
    <div>
        <label
                class="text-input-label"
                for="grid-primary-image"
        >
            Primary Image
        </label>
        <div v-if="hasImage">
            <transition name="trx-fade-in">
                <img class="mt-1 shadow rounded"
                     :src="getThumbnailUrl(image.url, 'small')">
            </transition>
            <div class="mt-2 text-grey text-sm">
                {{ image.width }}x{{ image.height }}s
            </div>
            <div class="mt-3 text-sm text-grey-dark hover:text-red-dark cursor-pointer" @click="clearPrimaryImage()">
                <fa-icon class="mr-1" :icon="['far', 'times']" />
                <span>Clear</span>
            </div>
        </div>
        <span v-else class="text-grey mt-1">
            None set.
        </span>
    </div>
</template>

<script>
    import Image from '../mixins/ImageMixin'

    export default {
        mixins: [Image],
        computed: {
            hasImage() {
                return !_.isEmpty(this.image) && this.image.url
            }
        },
        props: {
            image: {
                type: Object,
                default: () => {
                    return {}
                },
            },
            parentType: {
                type: String,
                default: '',
            }
        },
        methods: {
            clearPrimaryImage() {
                Event.fire('clearPrimaryImage', this.parentType)
            }
        }
    }
</script>

<style scoped>

</style>