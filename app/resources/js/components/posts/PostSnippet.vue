<template>
    <div class="post post-snippet">
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

        <div class="mt-4">
            <img class="float-right ml-2 mb-2 rounded-lg" :src="getPrimaryImage()" v-if="hasPrimaryImage">
            <div
                    v-html="post.body_snippet"
            />
            <div class="mt-6">
                <a :href="post.url" class="flex items-center">
                    <span v-if="post.needs_snip">Read More</span>
                    <span v-else>Full Post</span>
                    <fa-icon class="ml-2" transform="down-1" :icon="['far', 'angle-double-right']" />
                </a>
            </div>
        </div>

        <div class="flex items-center mt-6">
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
</template>

<script>
    import Filters from '../mixins/FiltersMixin'
    import TagList from './TagList'
    import Image from '../mixins/ImageMixin'

    export default {
        components: {TagList},
        mixins: [Filters, Image],
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
        methods: {
          getPrimaryImage() {
              return this.post.primary_image.width > this.imageSettings.thumbnail_widths.small ?
                  this.getThumbnailUrl(this.post.primary_image.url, 'small') :
                  this.post.primaryImage.url
          }
        },
        computed: {
            hasPrimaryImage() {
              return !_.isEmpty(this.post.primary_image) && this.post.primary_image.hasOwnProperty("url")
            },
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
