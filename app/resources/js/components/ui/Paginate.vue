<template>
    <ul class="pagination list-reset flex" v-if="shouldPaginate">
        <li v-if="data.has_prev">
            <a href="#"
               @click.prevent="selectPage(data.current_page - 1)"
               aria-label="Previous" rel="prev">
                <span aria-hidden="true">&laquo; Previous</span>
            </a>
        </li>
        <li v-for="page in data.page_list">
            <span v-if="page && data.current_page == page" v-text="page"/>
            <span v-if="page && data.current_page != page" class="cursor-pointer">
                <a @click.prevent="selectPage(page)" :href="getUrl(page)" v-text="page"/>
            </span>
            <span v-if="! page">...</span>
        </li>
        <li v-show="data.has_next">
            <a href="#" aria-label="Next" rel="next" @click.prevent="selectPage(data.current_page + 1)">
                <span aria-hidden="true">Next &raquo;</span>
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
            },
            updateUrl() {
                history.pushState(null, null, '?page=' + this.page);
            }
        },
        props: {
            data: {
                type: Object,
                // required: true,
            },
            name: {
                type: String,
                required: false,
                default: 'paginator'
            }
        },
    }
</script>
