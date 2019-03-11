<script>
import Filters from '../mixins/FiltersMixin'

export default {
    mixins: [Filters],
    props: {
        objectId: {
            type: Number,
            required: true
        },
        object: {
            type: String,
            required: true
        }
    },
    data () {
        return {
            ready: false,
            post: {},
            revisions: {},
            loadedRevision: {}
        }
    },
    computed: {
        hasRevisions () {
            return !_.isEmpty(this.revisions)
        },
        objectPlural () {
            return `${this.object}s`
        },
        showRevision () {
            return !_.isEmpty(this.loadedRevision)
        }
    },
    created () {
        this.fetch()
    },
    methods: {
        fetch () {
            this.ready = false

            axios.get(this.getEndpoint())
                .then(response => {
                    this.revisions = response.data.data
                    this.ready = true
                })
        },
        getEndpoint () {
            return `/admin/${this.objectPlural}/${this.objectId}/revisions`
        },
        loadRevision (revision) {
            this.loadedRevision = revision.revision
        },
        reset () {
            this.loadedRevision = {}
            this.fetch()
        }
    }
}
</script>

<style scoped>

</style>
