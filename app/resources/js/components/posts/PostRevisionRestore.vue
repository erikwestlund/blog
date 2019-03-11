<template>
    <div>
        <div class="flex mt-5">
            <label class="text-input-label">Title</label>
            <button role="link" class="ml-auto text-sm"
                    @click="restoreRevisedField(revision.title, 'title')">
                <fa-icon class="mr-1 text-grey" :icon="['far', 'window-restore']"/>
                Restore
            </button>
        </div>
        <div class="mt-2 bg-white p-3 shadow rounded">{{ revision.title }}</div>

        <div class="flex mt-5">
            <label class="text-input-label">Slug</label>
            <button role="link" class="ml-auto text-sm"
                    @click="restoreRevisedField(revision.slug, 'slug')">
                <fa-icon class="mr-1 text-grey" :icon="['far', 'window-restore']"/>
                Restore
            </button>
        </div>
        <div class="mt-2 bg-white p-3 shadow rounded post post-content">
            {{ revision.slug }}
        </div>

        <div class="flex mt-5">
            <label class="text-input-label">Body</label>
            <button role="link" class="ml-auto text-sm"
                    @click="restoreRevisedField(revision.body, 'body')">
                <fa-icon class="mr-1 text-grey" :icon="['far', 'window-restore']"/>
                Restore
            </button>
        </div>
        <div class="mt-2 bg-white p-3 shadow rounded post post-content"
             v-html="revision.body_html"
        />

        <div class="flex mt-5">
            <label class="text-input-label">Tags</label>
            <button role="link" class="ml-auto text-sm"
                    @click="restoreRevisedTags(revision.tags)">
                <fa-icon class="mr-1 text-grey" :icon="['far', 'window-restore']"/>
                Restore
            </button>
        </div>
        <div class="mt-2 bg-white p-3 shadow rounded post post-content">
            {{ getTagList(revision.tags) }}
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            revision: {
                type: Object,
                required: true,
            }
        },
        methods: {
            getTagList(tags) {
                if (_.isEmpty(tags)) {
                    return 'No tags.'
                }

                return tags.map(tag => {
                    return tag.name
                }).join(', ')
            },
            restoreRevisedField(revised, element) {
                Event.fire('restoreRevisedPostField', {revised, element})
            },
            restoreRevisedTags(tags) {
                Event.fire('restoreRevisedTags', tags)
            }
        }
    }
</script>

<style scoped>

</style>