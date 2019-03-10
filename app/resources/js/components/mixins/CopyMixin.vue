<script>
export default {
    methods: {
        copyUrl (url, urlFor = '') {
            this.$copyText(url).then(e => {
                let object = urlFor
                    ? `${urlFor} URL`
                    : 'URL'
                flash(`${object} copied to clipboard`)
            })
                .catch(e => {
                    flash(`Failed to copy URL to clipboard.`, 'danger')
                })
        }
    }
}
</script>
