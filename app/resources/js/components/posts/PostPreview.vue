<template>
    <div class="post-preview">
        <modal
            medium
            :show="show"
            no-footer
            @close="show = false"
        >
            <h3 slot="header" class="flex">
                {{ renderedTitle }}
                <fa-icon class="ml-auto cursor-pointer"
                         :icon="['far', 'times']"
                         @click="show = false"
                />
            </h3>

            <div slot="body">
                <div v-if="loaded && ! body">
                    Write something!
                </div>
                <div
                    v-else-if="loaded && body"
                    class="post"
                    v-html="renderedHtml"
                />
                <div v-else>
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
    components: { Modal },
    props: {
        title: {
            type: String,
            default: 'Preview Post'
        },
        body: {
            type: String,
            required: true
        }
    },
    data () {
        return {
            loaded: false,
            show: false,
            renderedHtml: ''
        }
    },
    computed: {
        renderedTitle () {
            return this.title || 'Preview Post'
        }
    },
    created () {
        Event.listen('showPostPreview', () => this.showPreview())
    },
    methods: {
        fetch () {
            this.loaded = false
            axios.post('/admin/posts/render-preview', {
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
        showPreview () {
            this.fetch()
        }
    }
}
</script>

<style>
    .post-preview .modal-container {
        width: 90% !important;
        max-width: 800px;
    }
</style>
