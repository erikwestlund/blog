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
                Restore All Post Fields
            </button>
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
        <div class="mt-2 flex">
            <div class="w-1/2">
                <div class="text-grey text-sm">old</div>
                <div class="mt-1" v-if="revision.title">
                    <h2>{{ revision.title }}</h2>
                </div>
                <div v-else class="text-grey">
                    (empty)
                </div>
            </div>
            <div class="w-1/2 text-normal">
                <div class="text-grey text-sm">current</div>
                <div class="mt-1">
                    <h2 v-if="form.title && revision.title">
                        <span
                                v-for="word in getWordDiff(revision.title, form.title)"
                                :class="`text-${getDiffColor(word)}`">
                            {{ word.value }}
                        </span>
                    </h2>
                    <h2 v-else>
                        {{ form.title }}
                    </h2>
                </div>
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
        <div class="mt-2 flex">
            <div class="w-1/2">
                <div class="text-grey text-sm">old</div>
                <div class="mt-1">
                    <span v-if="revision.slug">
                        {{ revision.slug }}
                    </span>
                    <span v-else class="text-grey">
                        (empty)
                    </span>
                </div>
            </div>
            <div class="w-1/2 text-normal">
                <div class="text-grey text-sm">current</div>
                <div class="mt-1" v-if="form.slug && revision.slug">
                    <span v-for="word in getWordDiff(revision.slug, form.slug)"
                          :class="`text-${getDiffColor(word)}`">
                        {{ word.value }}
                    </span>
                </div>
                <div v-else>
                    {{ form.slug }}
                </div>
            </div>
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
        <!--<div-->
                <!--class="mt-2 bg-white p-3 shadow rounded post post-content"-->
                <!--v-html="revision.body_html"-->
        <!--/>-->
        <div class="mt-2 flex">
            <div class="w-1/2 mr-5">
                <div class="text-grey text-sm">old</div>
                <div class="mt-1">
                    <div v-if="revision.body"
                         class="mt-2 bg-white p-3 shadow rounded post post-content"
                         v-html="revision.body">
                    </div>
                    <span v-else class="text-grey">
                        (empty)
                    </span>
                </div>
            </div>
            <div class="w-1/2 text-normal">
                <div class="text-grey text-sm">current</div>
                 <div class="mt-2 bg-white p-3 shadow rounded post post-content" v-if="form.body && revision.body">
                    <div v-for="line in getLineDiff(revision.body, form.body)"
                          >
                        {{ line.value }}
                    </div>
                </div>
                <div v-else>
                    {{ form.body }}
                </div>
            </div>
        </div>
        <!-- eslint-enable vue/no-v-html -->

        <div class="flex mt-10">
            <label class="text-input-label">Tags</label>
            <button
                    role="link"
                    class="ml-auto text-sm"
                    @click="restoreRevisedTags()"
            >
                <fa-icon
                        class="mr-1 text-grey"
                        :icon="['far', 'window-restore']"
                />
                Restore
            </button>
        </div>
        <div class="mt-1">
            <ul
                    v-if="hasTags"
                    class="list-reset flex"
            >
                <li
                        v-for="tag in revision.tags"
                        :key="tag.id"
                        class="inline rounded bg-blue-light px-2 py-1 text-sm text-white mr-2"
                >
                    {{ tag.name }}
                </li>
            </ul>
            <span v-else>
                No tags.
            </span>
        </div>

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

        <img
                v-if="hasPrimaryImage"
                class="shadow rounded"
                :src="getThumbnailUrl(revision.primary_image.url)"
        >
        <div v-else>
            No primary image set.
        </div>

        <div class="flex mt-5">
            <label class="text-input-label">Published At</label>
            <button
                    role="link"
                    class="ml-auto text-sm"
                    @click="restoreRevisedField(revision.published_at, 'published_at', 'Published at')"
            >
                <fa-icon
                        class="mr-1 text-grey"
                        :icon="['far', 'window-restore']"
                />
                Restore
            </button>
        </div>

        <div
                v-if="hasPublishedAt"
                class="mt-2"
        >
            {{ revision.published_at }}
        </div>
        <div v-else>
            Not published.
        </div>
    </div>
</template>

<script>
    import RevisionRestore from '../ui/RevisionRestore'

    export default {
        extends: RevisionRestore,
        computed: {
            hasImages() {
                return !_.isEmpty(this.revision.images)
            },
            hasPrimaryImage() {
                return !_.isEmpty(this.revision.primary_image)
            },
            hasPublishedAt() {
                return !_.isNil(this.revision.published_at)
            },
            hasTags() {
                return !_.isEmpty(this.revision.tags)
            }
        },
        methods: {
            restoreRevisedField(revised, element, label = null) {
                Event.fire('restoreRevisedPostField', {revised, element, label})
            },
            restoreRevisedTags() {
                Event.fire('restoreRevisedTags', this.revision.tags)
            },
            restoreRevisedImages() {
                Event.fire('restoreRevisedImages', this.revision)
            },
            restoreRevisedPrimaryImage() {
                Event.fire('restoreRevisedPrimaryImage', this.revision.primary_image)
            },
            restoreAll() {
                Event.fire('restoreRevisedPost', this.revision)
            }
        }
    }
</script>

<style scoped>

</style>
