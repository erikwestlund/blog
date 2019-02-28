<script>
import Filters from '../mixins/FiltersMixin'
import PaginatedContent from '../mixins/PaginatedContentMixin'

export default {
    name: 'AdminPanel',
    mixins: [ PaginatedContent, Filters ],
    props: {
        object: {
            type: String,
            default: 'object'
        }
    },
    methods: {
        fetch () {
            axios.get(this.paginatedEndpoint)
                .then(response => {
                    this.data = response.data
                    this.ready = true
                })
                .catch(errors => {
                    flash(`Could not get ${this.object}s`, 'danger')
                })
        }
    }
}
</script>
