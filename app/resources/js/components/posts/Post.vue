<template>
    <div class="post">

        <div class="p-3">
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
            <h1 class="text-4xl font-bold">{{ post.title }}</h1>

            <div class="text-grey-darker mt-3 flex items-center">
                <div class="flex">
                    <span class="mr-2 text-md font-bold">{{ post.user.display_name }}</span>
                    <span class="text-grey">{{ post.published_at | ago }} ago</span>
                </div>

                <div class="flex items-center ml-auto">
                    <fa-icon
                            v-if="tagCount == 1"
                            class="text-grey mr-3"
                            :icon="['far', 'tag']"
                    />
                    <fa-icon
                            v-else-if="tagCount > 1"
                            class="text-grey mr-3"
                            :icon="['far', 'tags']"
                    />
                    <tag-list :tags="post.tags"/>
                </div>
            </div>
        </div>


        <div
                class="mt-1 post-content post bg-white rounded-lg shadow p-5"
                v-html="post.body_html"
        />


    </div>
</template>

<script>
    import Filters from '../mixins/FiltersMixin'
    import TagList from './TagList'

    export default {
        components: {TagList},
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
            tagCount() {
                return _.isEmpty(this.post.tags)
                    ? 0
                    : this.post.tags.length
            }
        }
    }
</script>

<style scoped>

</style>
