<script>
    import Post from './Post'

    export default {
        extends: Post,
        name: "CreatePost",
        data() {
            return {
                name: 'create',
                loaded: true
            }
        },
        methods: {
            savePost() {
                this.form.submit('post', '/posts/create')
                    .then(response => {
                        console.log(response)
                    })
                    .catch(errors => {
                        console.log(errors)
                    })
            }
        }
    }
</script>

<style scoped>

</style>