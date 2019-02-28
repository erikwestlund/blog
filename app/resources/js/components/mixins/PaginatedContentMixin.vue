<script>
import Paginate from '../ui/Paginate'

export default {
    components: {
        Paginate
    },
    props: {
        endpoint: {
            type: String,
            required: true
        },
        name: {
            type: String,
            required: true
        }
    },
    data () {
        return {
            activePage: 1,
            data: [],
            ready: false
        }
    },
    computed: {
        paginationMeta () {
            return this.ready
                ? this.data.meta.pagination
                : { current_page: 1 }
        },
        paginatedEndpoint () {
            return `${this.endpoint}?page=${this.activePage}`
        },
        hasObjects () {
            return this.objectCount > 0
        },
        objectCount () {
            return _.isEmpty(this.data)
                ? 0
                : this.data.data.length
        }
    },
    watch: {
        activePage: 'fetch'
    },
    created () {
        Event.listen('newPageSelected', (page) => this.setActivePage(page))
        this.fetch()
    },
    methods: {
        setActivePage (payload) {
            if (payload.name === this.name) {
                this.activePage = payload.page
            }
        }
    }
}
</script>
