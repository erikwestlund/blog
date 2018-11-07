<template>
    <ul class="pagination" v-if="shouldPaginate">
        <li v-show="data.has_prev">
            <a href="#" aria-label="Previous" rel="prev" @click.prevent="selectPage(data.current_page - 1)">
                <span aria-hidden="true">&laquo; Previous</span>
            </a>
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