<template>
    <ul class="pagination list-reset flex" v-if="shouldPaginate">
        <li v-if="data.has_prev">
            <a href="#"
               :href="getUrl(data.current_page - 1)"
               @click.prevent="selectPage(data.current_page - 1)"
               title="Previous" rel="prev">
                <fa-icon :icon="['far', 'angle-double-left']"/>
            </a>
        </li>
        <li v-for="page in data.page_list" :class="{'active': data.current_page==page}">
            <span v-if="page && data.current_page == page" v-text="page"/>
            <span v-else-if="! page"><fa-icon class="text-grey" :icon="['far', 'ellipsis-h']"/></span>
            <a v-else="page && data.current_page != page"
               @click.prevent="selectPage(page)"
               :href="getUrl(page)"
               v-text="page"/>
        </li>
        <li v-show="data.has_next">
            <a :href="getUrl(data.current_page + 1)"
               @click.prevent="selectPage(data.current_page + 1)"
               title="Next"
               rel="next">
                <fa-icon :icon="['far', 'angle-double-right']"/>
            </a>
        </li>
    </ul>
</template>

<script>
    export default {
        name: "Paginate",
        created() {
            Event.listen('newPageLoaded', () => this.updateUrl())
        },
        computed: {
            shouldPaginate() {
                return this.data.has_next || this.data.has_prev;
            }
        },
        methods: {
            getUrl(page) {
                return `${this.data.base_url}?page=${page}`
            },
            selectPage(page) {
                Event.fire('newPageSelected', {
                    page: page,
                    name: this.name,
                });
                this.updateUrl
            },
            updateUrl() {
                history.pushState(null, null, this.getUrl(this.data.current_page));
            }
        },
        props: {
            data: {
                type: Object,
            },
            name: {
                type: String,
                required: false,
                default: 'paginator'
            }
        },
        watch: {
            'data.current_page': 'updateUrl'
        }
    }
</script>
