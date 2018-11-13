<script>
    import Paginate from '../ui/Paginate'

    export default {
        name: "AdminPanel",
        abstract: true,
        components: {
            'paginate': Paginate
        },
        created() {
            this.fetch();
            Event.listen('newPageSelected', (page) => this.setActivePage(page))
        },
        computed: {
            paginationMeta() {
                return this.ready ?
                    this.data.meta.pagination :
                    {}
            },
            paginatedEndpoint() {
                return `${this.endpoint}?page=${this.activePage}`
            }
        },
        data() {
            return {
                activePage: 1,
                data: [],
                ready: false,
            }
        },
        methods: {
            fetch() {
                axios.get(this.paginatedEndpoint)
                    .then(response => {
                        this.data = response.data
                        this.ready = true
                    })
                    .catch(errors => {
                        flash(`Could not get ${this.object}s`, 'danger')
                    })
            },
            setActivePage(payload) {
                if(payload.name == this.name) {
                    this.activePage = payload.page
                }
            }
        },
        props: {
            name: {
                type: String,
                required: true,
            },
            endpoint: {
                type: String,
                required: true,
            },
            object: {
                type: String,
                default: 'object'
            }
        },
        watch: {
            activePage: 'fetch'
        }
    }
</script>
