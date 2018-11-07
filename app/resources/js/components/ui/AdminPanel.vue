<template>

</template>

<script>
    import Paginate from '../ui/Paginate'

    export default {
        name: "AdminPanel",
        components: {
            'paginate': Paginate
        },
        created() {
            axios.get(this.endpoint)
                .then(response => {
                    this.data = response.data;
                    this.ready = true;
                })
                .catch(errors => {
                    flash(`Could not get ${this.object}s`, 'danger')
                })
        },
        computed: {
            paginationMeta() {
                return this.ready ?
                    this.data.meta.pagination :
                    {}
            }
        },
        data() {
            return {
                data: [],
                ready: false,
            }
        },
        props: {
            endpoint: {
                type: String,
                required: true,
            },
            object: {
                type: String,
                default: 'object'
            }
        }
    }
</script>

<style scoped>

</style>