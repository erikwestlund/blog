<template>
    <div>
        <div class="mt-10">
            <button
                class="ml-auto text-sm btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                @click="restoreAll()"
            >
                <fa-icon
                    class="mr-1"
                    :icon="['far', 'window-restore']"
                />
                Restore All Page Fields
            </button>
        </div>
        <div class="flex mt-6">
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
        <h2 class="mt-2">
            {{ revision.title }}
        </h2>

        <div class="flex mt-5">
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
            {{ revision.slug }}
        </div>

        <div class="flex mt-5">
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
        <div
            class="mt-2 bg-white p-3 shadow rounded post post-content"
            v-html="revision.body_html"
        />
        <!-- eslint-enable vue/no-v-html -->

        <div class="flex mt-5">
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
            v-if="hasImages"
            class="mt-2 list-reset flex"
        >
            <li
                v-for="image in revision.images"
                :key="image.id"
                class="inline mr-2"
            >
                <img
                    class="shadow rounded"
                    :src="getThumbnailUrl(image.url)"
                >
            </li>
        </ul>
        <div v-else>
            No images.
        </div>

        <div class="flex mt-5">
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

        <img
            v-if="hasPrimaryImage"
            class="shadow rounded"
            :src="getThumbnailUrl(revision.primary_image.url)"
        >
        <div v-else>
            No primary image set.
        </div>
    </div>
</template>

<script>
import RevisionRestore from '../ui/RevisionRestore'

export default {
    extends: RevisionRestore,
    computed: {
        hasImages () {
            return !_.isEmpty(this.revision.images)
        },
        hasPrimaryImage () {
            return !_.isEmpty(this.revision.primary_image)
        }
    },
    methods: {
        restoreRevisedField (revised, element, label = null) {
            Event.fire('restoreRevisedPageField', { revised, element, label })
        },
        restoreRevisedImages () {
            Event.fire('restoreRevisedImages', this.revision.images)
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
