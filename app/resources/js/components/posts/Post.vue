<template>
    <div class="post">
        <a
            v-if="post.editable"
            class="text-grey float-right hover:text-grey-dark"
            :href="post.edit_url"
        >
            <fa-icon
                class="mr-2"
                :icon="['far', 'pencil']"
            />
            edit
        </a>

        <a :href="post.url"><h2 class="text-3xl">{{ post.title }}</h2></a>

        <div class="text-grey-darker mt-2">
            <span class="mr-2 text-md font-bold">{{ post.user.display_name }}</span>
            <span class="text-grey">{{ post.published_at | ago }} ago</span>
        </div>

        <div
            v-if="snip"
            class="mt-4"
            v-html="post.body_snippet"
        />
        <div
            v-else
            class="mt-4"
            v-html="post.body_html"
        />

        <div class="flex items-center mt-6">
            <fa-icon
                v-if="tagCount == 1"
                class="text-grey mr-2"
                :icon="['far', 'tag']"
            />
            <fa-icon
                v-else-if="tagCount > 1"
                class="text-grey mr-2"
                :icon="['far', 'tags']"
            />
            <tag-list :tags="post.tags" />
        </div>
    </div>
</template>

<script>
import Filters from '../mixins/FiltersMixin'
import TagList from './TagList'

export default {
    components: { TagList },
    mixins: [Filters],
    props: {
        post: {
            type: Object,
            required: true
        },
        snip: {
            type: Boolean,
            default: false
        }
    },
    computed: {
        tagCount () {
            return _.isEmpty(this.post.tags)
                ? 0
                : this.post.tags.length
        }
    }
}
</script>

<style scoped>

</style>
