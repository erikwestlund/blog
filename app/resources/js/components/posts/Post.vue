<template>
    <div v-show="loaded">
        <form
                class="w-full"
                method="POST"
                :action="endpoint"
                @submit.prevent
                @keydown="form.errors.clear($event.target.name)"
        >
            <h1 class="p-3">
                <fa-icon
                        class="mr-2 text-grey"
                        :icon="['far', actionIcon ]"
                />
                <span class="capitalize">
          {{ form.action }}
        </span> Post
            </h1>
            <div class="flex mt-6">
                <div class="w-3/4 bg-white rounded shadow pt-5 pb-5 pl-3 pr-3">
                    <div class="w-full px-3">
                        <label
                                class="text-input-label"
                                for="grid-body"
                        >
                            Title
                        </label>
                        <input
                                id="grid-title"
                                v-model="form.title"
                                class="text-input focus:outline-none focus:border-grey"
                                name="title"
                                :class="{'border border-red' : form.errors.has('title')}"
                                placeholder="Title"
                        >
                        <p
                                v-if="form.errors.has('title')"
                                class="text-red text-xs italic"
                                v-text="form.errors.get('title')"
                        />
                    </div>
                    <div class="w-full px-3 mt-3">
                        <label
                                class="text-input-label"
                                for="grid-body"
                        >
                            Body
                        </label>
                        <markdown-editor
                                ref="markdownEditor"
                                placeholder="body"
                                v-model="form.body"
                                :class="{'border border-red' : form.errors.has('title')}"
                        />
                        <p
                                v-if="form.errors.has('body')"
                                class="text-red text-xs italic mt-3"
                                v-text="form.errors.get('body')"
                        />
                    </div>
                </div>
                <div class="w-1/4 p-3">
                    <div class="w-full px-3">
                        <label
                                class="text-input-label"
                                for="grid-tags"
                        >
                            Tags
                        </label>
                        <tags
                                class="component-tags"
                                name="tags"
                                for="tags"
                        />
                    </div>
                    <div class="mt-6 px-3">
                        <button
                                class="btn btn-white hover:bg-grey-lightest hover:border-grey p-2 mr-2"
                                :disabled="form.errors.any() || submitting"
                                @click="savePost()"
                        >
                            <fa-icon
                                    class="mr-2"
                                    :icon="['far', 'save']"
                            />
                            Save
                        </button>
                        <button v-show="! isPublished"
                                class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                                :disabled="form.errors.any() || submitting"
                                @click="publishPost()"
                        >
                            <fa-icon
                                    class="mr-2"
                                    :icon="['far', 'eye']"
                            />
                            Publish
                        </button>
                        <button v-show="isPublished"
                                class="btn btn-red hover:bg-red-darkest hover:border-red-darkest"
                                :disabled="form.errors.any() || submitting"
                                @click="unpublishPost()"
                        >
                            <fa-icon
                                    class="mr-2"
                                    :icon="['far', 'eye-slash']"
                            />
                            Unpublish
                        </button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
    import Form from '../../modules/Form'
    import Tags from '../ui/Tags'
    import MarkdownEditor from 'vue-simplemde/src/markdown-editor'

    export default {
        name: 'Post',
        components: {
            'tags': Tags,
            'markdown-editor': MarkdownEditor
        },

        props: {
            endpoint: {
                type: String,
                required: true
            },

            initAction: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                submitting: false,
                savedPost: {},
                loaded: false,
                form: new Form({
                    action: this.initAction,
                    post_id: '',
                    tags: [],
                    title: '',
                    body: '',
                    dontReset: true,
                }, this.isUpdateForm)
            }
        },
        computed: {
            actionIcon() {
                return this.form.action === 'create'
                    ? 'plus-circle'
                    : 'pencil'
            },

            hasPostRecord() {
                return !_.isEmpty(this.savedPost) &&
                    this.savedPost.id
            },

            isPublished() {
                return this.hasPostRecord &&
                    this.savedPost.published_at
            },

            isUpdateForm() {
                return this.form.action === 'edit'
            },

            requestType() {
                return this.hasPostRecord ?
                    'patch' :
                    'post'
            }
        },
        created() {
            Event.listen('tagsUpdated', (payload) => this.updateTags(payload))

            this.loaded = true
        },
        methods: {
            updateTags(payload) {
                if (payload.for === 'tags') {

                    this.form.tags = _.map(payload.tags, 'id')
                }
            },

            updatePostFromServer(post) {
                this.form.post_id = post.id
                this.form.title = post.title
                this.form.body = post.body
            },

            publishPost() {
                this.form.action = 'publish'
                this.savePost();
            },

            unpublishPost() {
                this.form.action = 'unpublish'
                this.savePost();
            },

            savePost() {

                this.form.submit(this.requestType, this.endpoint)
                    .then(response => {
                        this.savedPost = response.post
                        this.form.action = 'edit'

                        if (response.action === 'create') {
                            flash('Post successfully created!')
                            this.form.post_id = response.post.id
                        } else if(response.action === 'edit') {
                            flash('Post successfully saved!')
                        } else if (response.action === 'publish') {
                            flash('Post successfully published!')
                        } else if (response.action === 'unpublish') {
                            flash('Post successfully unpublished!')
                        }

                        // this.updatePostFromServer(response.post)
                    })
                    .catch(errors => {

                        if (this.form.action === 'save') {
                            flash('Failed to save post.', 'danger')
                        } else if (action === 'publish') {
                            flash('Failed to publish post.', 'danger')
                        }
                    })
            }
        },
        watch: {
            'action': 'updateFormAction'
        }
    }
</script>

<style>
    @import '~simplemde/dist/simplemde.min.css';

    /*.ti-tag.ti-valid {*/
    /*background-color: #3490cd !important;*/
    /*}*/
</style>
