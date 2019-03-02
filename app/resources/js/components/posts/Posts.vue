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
                    <a v-if="post.editable" class="text-grey float-right hover:text-grey-dark" :href="post.edit_uri">
                        <fa-icon class="mr-2" :icon="['far', 'pencil']"/>
                        edit
                    </a>

                    <a :href="post.uri"><h2>{{ post.title }}</h2></a>

                    <div
                            class="mt-2"
                            v-html="post.body_md"
                    />
                    <div class="md:flex mt-6">
                        <div class="text-grey-darker">
                            <span class="mr-2 text-lg font-bold">{{ post.user.display_name }}</span>
                            <span class="text-grey">{{ post.published_at | ago }} ago</span>
                        </div>
                        <div class="md:ml-auto">
                            <ul class="list-reset flex">
                                <li class="inline rounded bg-grey-lightest text-grey-darker px-1 py-0 text-sm border border-grey-lighter"
                                    v-for="tag, index in post.tags" :key="tag.id"
                                    :class="{'mr-2' : post.tags.length - 1 != index }"
                                >
                                    {{ tag.name }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else-if="ready">
                No posts have been published yet! <a href="/admin/posts/create">Make One</a>.
            </div>
        </transition>
        <div class="flex justify-center" v-if="hasObjects">
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
        data() {
            return {
                state: State,
                ready: false
            }
        },
        created() {
            Event.listen('newPageSelected', (page) => this.setActivePage(page))
        },
        methods: {
            fetch() {
                axios.get(this.paginatedEndpoint).then(response => {
                    this.data = response.data
                    this.ready = true
                }).catch(errors => {
                    flash('Could not load posts.')
                })
            },

        }
    }
</script>

<style scoped>

</style>
