<script>
    import Preview from '../ui/Preview'

    export default {
        extends: Preview,
        methods: {
            fetch() {
                this.loaded = false
                axios.post('/admin/pages/render-preview', {
                    body: this.body
                })
                    .then(response => {
                        this.renderedHtml = response.data.html
                        this.show = true
                        this.loaded = true
                    })
                    .catch(errors => {
                        flash('Could not lost preview', 'danger')
                    })
            },
        }
    }
</script>
