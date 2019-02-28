<template>
    <ul
        v-if="shouldPaginate"
        class="pagination list-reset flex"
    >
        <li v-if="data.has_prev">
            <a
                :href="getUrl(data.current_page - 1)"
                title="Previous"
                rel="prev"
                @click.prevent="selectPage(data.current_page - 1)"
            >
                <fa-icon :icon="['far', 'angle-double-left']" />
            </a>
        </li>
        <li
            v-for="page in data.page_list"
            :key="page"
            :class="{ active: data.current_page == page }"
        >
            <span
                v-if="page && data.current_page == page"
                v-text="page"
            />
            <span v-else-if="!page">
                <fa-icon
                    class="text-grey"
                    :icon="['far', 'ellipsis-h']"
                />
            </span>
            <a
                v-else-if="page && data.current_page != page"
                :href="getUrl(page)"
                @click.prevent="selectPage(page)"
                v-text="page"
            />
        </li>
        <li v-show="data.has_next">
            <a
                :href="getUrl(data.current_page + 1)"
                title="Next"
                rel="next"
                @click.prevent="selectPage(data.current_page + 1)"
            >
                <fa-icon :icon="['far', 'angle-double-right']" />
            </a>
        </li>
    </ul>
</template>

<script>
export default {
    name: 'Paginate',
    props: {
        data: {
            type: Object,
            default: () => {
                current_page: 1
            }
        },
        name: {
            type: String,
            required: false,
            default: 'paginator'
        }
    },
    computed: {
        shouldPaginate () {
            return this.data.has_next || this.data.has_prev
        }
    },
    watch: {
        'data.current_page': 'updateUrl'
    },
    created () {
        Event.listen('newPageLoaded', () => this.updateUrl())
    },
    methods: {
        getUrl (page) {
            return `${this.data.base_url}?page=${page}`
        },
        selectPage (page) {
            Event.fire('newPageSelected', {
                page: page,
                name: this.name
            })
            this.updateUrl()
        },
        updateUrl () {
            history.pushState(null, null, this.getUrl(this.data.current_page))
        }
    }
}
</script>
