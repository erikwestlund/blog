<template>
    <div class="preview">
        <modal
            medium
            :show="show"
            no-footer
            @close="show = false"
        >
            <h3
                slot="header"
                class="flex"
            >
                {{ renderedTitle }}
                <fa-icon
                    class="ml-auto cursor-pointer"
                    :icon="['far', 'times']"
                    @click="show = false"
                />
            </h3>

            <div slot="body">
                <div v-if="loaded && ! body">
                    Write something!
                </div>

                <!-- eslint-disable vue/no-v-html -->
                <div
                    v-else-if="loaded && body"
                    class="post"
                    v-html="renderedHtml"
                />
                <!-- eslint-enable vue/no-v-html -->
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
import Modal from './Modal'

export default {
    components: { Modal },
    props: {
        title: {
            type: String,
            default: 'Preview'
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
            return this.title || 'Preview'
        }
    },
    created () {
        Event.listen('showPreview', () => this.showPreview())
    },
    methods: {
        showPreview () {
            this.fetch()
        }
    }
}
</script>

<style>
    .preview .modal-container {
        width: 90% !important;
        max-width: 800px;
    }
</style>
