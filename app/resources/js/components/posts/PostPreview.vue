<template>
    <div class="post-preview">

        <modal
                medium
                :show="show"
                no-footer
                @close="show = false"
        >
            <h3 slot="header">
                {{ title }}
            </h3>

            <div slot="body">
                <div v-if="loaded" class="post" v-html="renderedHtml">
                </div>
                <div v-else="! loaded">
                    <fa-icon
                            class="mr-2 fa-spin"
                            :icon="['far', 'circle-notch']"
                    />
                    Loading...
                </div>
            </div>

        </modal>
    </div>
</template>

<script>
    import Modal from '../ui/Modal'

    export default {
        components: {Modal},
        created() {
            Event.listen('showPostPreview', () => this.show = true)
        },
        data() {
            return {
                loaded: false,
                show: false,
                renderedHtml: ''
            }
        },
        props: {
            title: {
              type: String,
              default: 'Preview Post',
            },
            body: {
                type: String,
                required: true,
            }
        },
        methods: {
            fetch() {
                this.loaded = false;
                axios.post("/admin/posts/render-preview", {
                    body: this.body
                })
                    .then(response => {
                        this.renderedHtml = response.data.html
                        this.loaded = true;
                    })
                    .catch(error => {
                        flash('Could not lost preview', 'danger')
                    })
            }
        },
        watch: {
            'show': 'fetch'
        }
    }
</script>

<style>
    .post-preview .modal-container {
        width: 100% !important;
        max-width: 800px;
    }
</style>