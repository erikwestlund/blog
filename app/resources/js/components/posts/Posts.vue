<template>
    <div>
        <div
            v-for="(post, index) in data.data"
            v-if="ready"
            :key="post.id"
            class="rounded-lg p-5 shadow bg-white"
            :class="index==0 ? '' : 'mt-5'"
        >
            <a :href="post.url"><h2>{{ post.title }}</h2></a>

            <div
                class="mt-2"
                v-html="post.body_md"
            />
            <div class="mt-6  text-grey-darker">
                <fa-icon
                    class="mr-2 text-grey"
                    :icon="['fas', 'user-circle']"
                />
                <span class="mr-2 text-lg font-bold">{{ post.user.display_name }}</span>
                <span class="text-grey">{{ post.published_at | ago }} ago</span>
            </div>
        </div>
        <div
            v-else
            class="text-grey"
        >
            <fa-icon
                class="fa-2x fa-spin"
                :icon="['far', 'circle-notch']"
            />
        </div>
        <div class="flex justify-center">
            <paginate
                class="mt-8"
                name="posts"
                :data="paginationMeta"
            />
        </div>
    </div>
</template>

<script>
import Filters from '../mixins/FiltersMixin'
import Pagination from '../mixins/PaginatedContentMixin'

export default {
    mixins: [Filters, Pagination],
    props: {
        page: {
            type: Number,
            default: 1
        }
    },
    data () {
        return {
            ready: false
        }
    },
    created () {
        Event.listen('newPageSelected', (page) => this.setActivePage(page))
    },
    methods: {
        fetch () {
            axios.get(this.paginatedEndpoint).then(response => {
                this.data = response.data
                this.ready = true
            }).catch(errors => {
                flash('Could not load posts.')
            })
        }
    }
}
</script>

<style scoped>

</style>
