<template>
    <ul class="pagination" v-if="shouldPaginate">
        <li v-show="prevUrl">
            <a href="#" aria-label="Previous" rel="prev" @click.prevent="page--">
                <span aria-hidden="true">&laquo; Previous</span>
            </a>
        </li>
        <li v-show="nextUrl">
            <a href="#" aria-label="Next" rel="next" @click.prevent="page++">
                <span aria-hidden="true">Next &raquo;</span>
            </a>
        </li>
    </ul>
</template>

<script>
    export default {
        mounted() {
            this.$nextTick(function () {
                if (! this.ready) {
//                    this.setData();
                }
            });
        },
        props: {
            meta: {
                required: true,
            },
            name: {
                type: String,
                required: false,
                default: 'paginator'
            }
        },

        data() {
            return {
                ready: false,
                page: 1,
                prevUrl: false,
                nextUrl: false
            }
        },

        watch: {
            meta: {
                handler: 'setData',
                deep: true
            },

            page() {
                return Event.fire('pageChanged', {
                    page: this.page,
                    name: this.name,
                });

                this.updateUrl();
            }
        },

        computed: {
            shouldPaginate() {
                return !!this.prevUrl || !!this.nextUrl;
            }
        },

        methods: {
            setData: _.debounce(function () {
                this.page = this.meta ? this.meta.current_page : 1;
                this.prevUrl = this.meta ? this.meta.prev_page_url : null;
                this.nextUrl = this.meta ? this.meta.next_page_url : null;
                this.ready = true;
            }, 250),
            updateUrl() {
                history.pushState(null, null, '?page=' + this.page);
            }
        }
    }
</script>