<template>
    <div>
        <transition name="trx-fade-in">
            <div v-if="ready && hasObjects">
                <div
                    v-for="(post, index) in data.data"
                    :key="post.id"
                    class="rounded-lg p-5 shadow bg-white"
                    :class="index==0 ? '' : 'mt-5'"
                >
                    <post :post="post" />
                </div>
            </div>
            <div v-else-if="ready">
                No posts have been published yet! <a href="/admin/posts/create">Make One</a>.
            </div>
        </transition>
        <div
            v-if="hasObjects"
            class="flex justify-center"
        >
            <paginate
                class="mt-8"
                name="posts"
                :data="paginationMeta"
            />
        </div>
    </div>
</template>

<script>
import Pagination from '../mixins/PaginatedContentMixin'
import Post from './Post'
export default {
    components: { Post },
    mixins: [Pagination],
    props: {
        page: {
            type: Number,
            default: 1
        }

    },
    data () {
        return {
            state: State,
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
