<template>
    <div v-show="loaded">
        <form class="w-full"
              method="POST"
              :action="endpoint"
              @submit.prevent
              @keydown="form.errors.clear($event.target.name)"
        >
            <h1 class="p-3">
                <fa-icon class="mr-2 text-grey" :icon="['far', actionIcon ]"></fa-icon>
                <span class="capitalize">{{ action }}</span> Post
            </h1>
            <div class="flex mt-6">
                <div class="w-3/4">
                    <div class="w-full px-3">
                        <label class="text-input-label"
                               for="grid-body">
                            Subject
                        </label>
                        <input class="text-input focus:outline-none focus:border-grey"
                               name="subject"
                               :class="{'border border-red' : form.errors.has('subject')}"
                               v-model="form.subject"
                               id="grid-subject"
                               placeholder="Subject">
                        <p class="text-red text-xs italic"
                           v-if="form.errors.has('subject')"
                           v-text="form.errors.get('subject')"></p>
                    </div>
                    <div class="w-full px-3 mt-3">
                        <label class="text-input-label"
                               for="grid-body">
                            Body
                        </label>
                        <markdown-editor v-model="form.body"
                                         :class="{'border border-red' : form.errors.has('subject')}"
                                         ref="markdownEditor"></markdown-editor>
                        <p class="text-red text-xs italic mt-3"
                           v-if="form.errors.has('body')"
                           v-text="form.errors.get('body')"></p>
                    </div>
                </div>
                <div class="w-1/4">
                    <div class="w-full px-3">
                        <label class="text-input-label"
                               for="grid-tags">
                            Tags
                        </label>
                        <tags class="component-tags" name="tags" :for="action"></tags>
                    </div>
                    <div class="mt-6 px-3">
                        <button class="btn btn-white hover:bg-grey-lightest hover:border-grey p-2 mr-2"
                                :disabled="form.errors.any() || submitting"
                                @click="savePost()"
                        >
                            <fa-icon class="mr-2" :icon="['far', 'save']"/>
                            Save
                        </button>
                        <button class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                                :disabled="form.errors.any() || submitting"
                        >
                            <fa-icon class="mr-2" :icon="['far', 'eye']"/>
                            Publish
                        </button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
    import Form from '../../modules/Form';
    import Tags from '../ui/Tags'
    import MarkdownEditor from 'vue-simplemde/src/markdown-editor'

    export default {
        name: "Post",
        created() {
            Event.listen('tagsUpdated', (payload) => this.updateTags(payload))

            this.loaded = true
        },
        computed: {
            actionIcon() {
                return this.action == 'create' ?
                    'plus-circle' :
                    'pencil'
            },

            isPublished() {
                if(
                    ! _.isEmpty(this.savedPost) &&
                    _.isDate(this.savedPost.published_at)
                ){
                    return true;
                }

                return false;
            }
        },
        components: {
            'tags': Tags,
            'markdown-editor': MarkdownEditor,
        },
        data() {
            return {
                action: this.initAction,
                submitting: false,
                savedPost: {},
                loaded: false,
                form: new Form({
                    tags: [],
                    subject: '',
                    body: '',
                })
            }
        },
        methods: {
            updateTags(payload) {
                if (payload.for == this.name) {
                    this.form.tags = payload.tags
                }
            },

            publishPost() {
                this.form.submit('post', '/posts/publish')
                    .then(response => {
                        console.log(response)
                    })
                    .catch(errors => {
                        console.log(errors)
                    })
            },


            savePost() {
                this.form.submit('post', '/posts/save')
                    .then(response => {
                        console.log(response)
                    })
                    .catch(errors => {
                        console.log(errors)
                    })
            }
        },
        props: {
            endpoint: {
                type: String,
                required: true
            },

            initAction: {
                type: String,
                required: true,
            }
        }
    }
</script>

<style>
    @import '~simplemde/dist/simplemde.min.css';

    .component-tagBox.tag.valid {
        background-color: #3490cd
    }
</style>