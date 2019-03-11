
<script>
    import Filters from '../mixins/FiltersMixin'

    export default {
        mixins: [Filters],
        created() {
            this.fetch()
        },
        computed: {
            hasRevisions() {
                return !_.isEmpty(this.revisions)
            },
            objectPlural() {
                return `${this.object}s`
            },
            showRevision() {
                return !_.isEmpty(this.loadedRevision)
            }
        },
        props: {
            objectId: {
                type: Number,
                required: true,
            },
            object: {
                type: String,
                required: true,
            }
        },
        data() {
            return {
                ready: false,
                post: {},
                revisions: {},
                visibleRevision: {}
            }
        },
        methods: {
            fetch() {
                this.ready = false

                axios.get(this.getEndpoint())
                    .then(response => {
                        this.revisions = response.data.data
                        this.ready = true
                    })
            },
            getEndpoint() {
                return `/admin/${this.objectPlural}/${this.objectId}/revisions`
            },

        }
    }
</script>

<style scoped>

</style>