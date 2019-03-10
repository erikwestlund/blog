
<script>
    export default {
        methods: {
            restoreRevision(revision) {
                restoredObject = JSON.parse(revision.revision)
                this.form.title = restoredObject.title
                this.form.body = restoredObject.body
            }
        }
    }
</script>

