<template>
    <div>
        <div class="mt-16 flex items-end">
            <button
                class="text-sm btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                @click="restoreAll()"
            >
                <fa-icon
                    class="mr-1"
                    :icon="['far', 'window-restore']"
                />
                Restore All Page Fields
            </button>
            <div class="ml-auto w-1/2 text-sm flex items-end">
                <span class="text-grey mr-1">same</span>
                <span class="text-red mr-1">from revision</span>
                <span class="text-green mr-1">new</span>
            </div>
        </div>
        <div class="flex mt-10">
            <label class="text-input-label">Title</label>
            <button
                role="link"
                class="ml-auto text-sm"
                @click="restoreRevisedField(revision.title, 'title')"
            >
                <fa-icon
                    class="mr-1 text-grey"
                    :icon="['far', 'window-restore']"
                />
                Restore
            </button>
        </div>
        <div class="mt-2 ">
            <h2 v-if="revision.title">
                <span
                    v-for="(word, index) in getWordDiff(revision.title || '', form.title || '')"
                    :key="index"
                    :class="`text-${getDiffColor(word)}`"
                >
                    {{ word.value }}
                </span>
            </h2>
            <div
                v-else
                class="text-grey"
            >
                (empty)
            </div>
        </div>

        <div class="flex mt-10">
            <label class="text-input-label">Slug</label>
            <button
                role="link"
                class="ml-auto text-sm"
                @click="restoreRevisedField(revision.slug, 'slug')"
            >
                <fa-icon
                    class="mr-1 text-grey"
                    :icon="['far', 'window-restore']"
                />
                Restore
            </button>
        </div>
        <div class="mt-2">
            <span
                v-for="(word, index) in getWordDiff(revision.slug || '', form.slug || '')"
                :key="index"
                :class="`text-${getDiffColor(word)}`"
            >
                {{ word.value }}
            </span>
        </div>

        <div class="flex mt-10">
            <label class="text-input-label">Body</label>
            <button
                role="link"
                class="ml-auto text-sm"
                @click="restoreRevisedField(revision.body, 'body')"
            >
                <fa-icon
                    class="mr-1 text-grey"
                    :icon="['far', 'window-restore']"
                />
                Restore
            </button>
        </div>

        <!-- eslint-disable vue/no-v-html -->
        <div class="mt-2 bg-white p-3 shadow rounded post post-content">
            <div
                v-for="(line, index) in getLineDiff(revision.body || '', form.body || '')"
                :key="index"
                :class="`text-${getDiffColor(line)}`"
            >
                <div v-html="line.value" />
            </div>
        </div>
        <!-- eslint-enable vue/no-v-html -->

        <div class="flex mt-10">
            <label class="text-input-label">Images</label>
            <button
                role="link"
                class="ml-auto text-sm"
                @click="restoreRevisedImages()"
            >
                <fa-icon
                    class="mr-1 text-grey"
                    :icon="['far', 'window-restore']"
                />
                Restore
            </button>
        </div>

        <ul
            class="mt-2 list-reset flex items-start"
        >
            <li
                v-for="(image, index) in getImagesDiff(revision.images || [], images || [])"
                :key="index"
                class="inline flex items-start"
            >
                <img
                    v-for="(diffImage, imageIndex) in image.value"
                    :key="imageIndex"
                    class="rounded  mr-2"
                    :class="`border border-${getDiffColor(image)}`"
                    :src="getThumbnailUrl(diffImage.url)"
                >
            </li>
        </ul>

        <div class="flex mt-10">
            <label class="text-input-label">Primary Image</label>
            <button
                role="link"
                class="ml-auto text-sm"
                @click="restoreRevisedPrimaryImage()"
            >
                <fa-icon
                    class="mr-1 text-grey"
                    :icon="['far', 'window-restore']"
                />
                Restore
            </button>
        </div>

        <ul
            class="mt-2 list-reset flex"
        >
            <li
                v-for="(image, index) in getLineDiff((revision.primary_image && revision.primary_image.hasOwnProperty('url')) ? revision.primary_image.url : '', (primaryImage && primaryImage.hasOwnProperty('url')) ? primaryImage.url : '')"
                :key="index"
                class="inline mr-2"
            >
                <img
                    v-if="image.value"
                    class="rounded"
                    :class="`border border-${getDiffColor(image)}`"
                    :src="getThumbnailUrl(image.value)"
                >
                <div v-else>
                    No image.
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import RevisionRestore from '../ui/RevisionRestore'

export default {
    extends: RevisionRestore,
    props: {
        currentTags: {
            type: Array,
            default: () => {
                return []
            }
        },
        images: {
            type: Array,
            default: () => {
                return []
            }
        },
        primaryImage: {
            type: Object,
            default: () => {
                return {}
            }
        }
    },
    computed: {
        hasImages () {
            return !_.isEmpty(this.revision.images)
        },
        hasPrimaryImage () {
            return !_.isEmpty(this.revision.primary_image)
        },
        hasPublishedAt () {
            return !_.isNil(this.revision.published_at)
        }
    },
    methods: {
        restoreRevisedField (revised, element, label = null) {
            Event.fire('restoreRevisedPageField', { revised, element, label })
        },
        restoreRevisedImages () {
            Event.fire('restoreRevisedImages', this.revision)
        },
        restoreRevisedPrimaryImage () {
            Event.fire('restoreRevisedPrimaryImage', this.revision.primary_image)
        },
        restoreAll () {
            Event.fire('restoreRevisedPage', this.revision)
        }
    }
}
</script>

<style scoped>

</style>
