<template>
    <div class="flex">
        <div class="w-3/4">
            <div class="w-full px-3">
                <label class="text-input-label"
                       for="grid-body">
                    Body
                </label>
                <markdown-editor v-model="form.body" ref="markdownEditor"></markdown-editor>
            </div>
        </div>
        <div class="w-1/4">
            <div class="w-full px-3">
                <label class="text-input-label"
                       for="grid-tags">
                    Tags
                </label>
                <tags name="tags" :for="name"></tags>
            </div>
            <div class="mt-6 px-3">
                <button class="btn btn-white hover:bg-grey-lightest hover:border-grey p-2 mr-2"
                        :disabled="form.errors.any() || submitting"
                >
                    <fa-icon class="mr-2" :icon="['far', 'save']" /> Save
                </button>
                <button class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                        :disabled="form.errors.any() || submitting"
                >
                    <fa-icon class="mr-2" :icon="['far', 'eye']" /> Publish
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    import Form from '../../modules/Form';
    import Tags from '../ui/Tags'
    import MarkdownEditor from 'vue-simplemde/src/markdown-editor'

    export default {
        name: "CreatePost",
        created() {
            Event.listen('tagsUpdated', (payload) => this.updateTags(payload))
        },
        components: {
            'tags': Tags,
            'markdown-editor': MarkdownEditor,
        },
        data() {
            return {
                name: 'createPost',
                form: new Form({
                    tags: [],
                    body: '',
                })
            }
        },
        methods: {
            updateTags(payload) {
                if (payload.for == this.name) {
                    this.form.tags = payload.tags
                }
            }
        }
    }
</script>

<style>
    @import '~simplemde/dist/simplemde.min.css';

    .component-tagBox.tag.valid {
        background-color:#3490cd
    }
</style>