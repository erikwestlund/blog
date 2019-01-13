<script>
import Paginate from '../ui/Paginate'

export default {
  name: 'AdminPanel',
  abstract: true,
  components: {
    'paginate': Paginate
  },
  props: {
    name: {
      type: String,
      required: true
    },
    endpoint: {
      type: String,
      required: true
    },
    object: {
      type: String,
      default: 'object'
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
        : {}
    },
    paginatedEndpoint () {
      return `${this.endpoint}?page=${this.activePage}`
    }
  },
  watch: {
    activePage: 'fetch'
  },
  created () {
    this.fetch()
    Event.listen('newPageSelected', (page) => this.setActivePage(page))
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
    },
    setActivePage (payload) {
      if (payload.name === this.name) {
        this.activePage = payload.page
      }
    }
  }
}
</script>
