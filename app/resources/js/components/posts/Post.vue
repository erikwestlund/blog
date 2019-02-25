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
          {{ action }}
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
                <div class="w-1/4  px-8">
                    <div class="w-full">
                        <label
                                class="text-input-label"
                                for="grid-tags"
                        >
                            Tags
                        </label>
                        <tags
                                :init-tags="seedTags"
                                class="component-tags"
                                name="tags"
                                for="tags"
                        />
                    </div>
                    <div class="mt-6">
                        <button
                                class="btn btn-white hover:bg-grey-lightest hover:border-grey p-2 mr-2"
                                :disabled="form.errors.any() || saving"
                                @click="savePost()"
                        >
                            <submitting-label v-if="saving" type="saving"/>
                            <span v-else>
                                <fa-icon
                                        class="mr-2"
                                        :icon="['far', 'save']"
                                />
                                Save
                            </span>
                        </button>
                        <button v-show="! isPublished"
                                class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                                :disabled="form.errors.any() || publishing"
                                @click="publishPost()"
                        >
                            <submitting-label v-if="publishing" type="publishing"/>
                            <span v-else>
                                <fa-icon
                                        class="mr-2"
                                        :icon="['far', 'eye']"
                                />
                                Publish
                            </span>
                        </button>
                        <button v-show="isPublished"
                                class="btn btn-red hover:bg-red-darkest hover:border-red-darkest"
                                :disabled="form.errors.any() || unpublishing"
                                @click.prevent="unpublishPost()"
                        >
                            <submitting-label v-if="unpublishing" type="unpublishing"/>
                            <span v-else>
                                <fa-icon
                                        class="mr-2"
                                        :icon="['far', 'eye-slash']"
                                />
                                Unpublish
                            </span>
                        </button>
                    </div>
                    <div class="mt-5">
                        <button class="text-sm text-red-darker" @click="showDeletePost = true">
                            <fa-icon class="mr-2" :icon="['far', 'trash']"/>
                            Delete
                        </button>
                    </div>
                    <div class="mt-5 text-grey text-sm" v-show="savedButNotPublished">
                        This post has not been published.
                    </div>
                    <div class="mt-5 text-grey text-sm" v-show="notSaved">
                        This post has not been saved.
                    </div>
                </div>
            </div>
            <modal
                    v-if="showDeletePost"
                    no-footer
                    @close="showDeletePost = false"
            >
                <h3 slot="header">
                    Delete Post
                </h3>

                <div slot="body" class="mb-5">
                    Are you you want to delete this post?

                    <div class="mt-10">
                        <button class="btn btn-white hover:bg-grey-lightest hover:border-grey p-2"
                                @click="deletePost()">
                            <fa-icon class="mr-2" :icon="['far', 'trash']"/>
                            Yes
                        </button>
                    </div>
                </div>
            </modal>
        </form>
    </div>
</template>

<script>
    import Form from '../../modules/Form'
    import Modal from '../ui/Modal'
    import Tags from '../ui/Tags'
    import SubmittingMixin from '../mixins/SubmittingMixin'
    import MarkdownEditor from 'vue-simplemde/src/markdown-editor'

    export default {
        name: 'Post',
        mixins: [SubmittingMixin],
        components: {
            Modal,
            Tags,
            MarkdownEditor
        },

        props: {
            initAction: {
                type: String,
                default: 'create'
            },

            initPostId: {
                type: Number,
                required: false,
                default: null,
            }
        },
        data() {
            return {
                savedPost: {},
                loaded: false,
                postId: this.initPostId,
                action: this.initAction,
                seedTags: [],
                showDeletePost: false,
                form: new Form(
                    {
                        tags: [],
                        title: '',
                        body: '',
                        published_at: ''
                    },
                    this.isUpdateForm,
                    true
                )
            }
        },
        computed: {
            actionIcon() {
                return this.action === 'create'
                    ? 'plus-circle'
                    : 'pencil'
            },

            endpoint() {
                return this.action === 'edit' ?
                    `/posts/${this.postId}` :
                    '/posts/create'
            },

            hasPostRecord() {
                return this.postId
            },

            notSaved() {
                return !this.postId
            },

            savedButNotPublished() {
                return this.hasPostRecord && !this.isPublished
            },

            isPublished() {
                return this.hasPostRecord &&
                    this.savedPost.published_at
            },

            isUpdateForm() {
                return this.action !== 'create'
            },

            requestType() {
                return this.hasPostRecord ?
                    'patch' :
                    'post'
            }
        },
        created() {
            Event.listen('tagsUpdated', (payload) => this.updateTags(payload))

            if (this.initPostId && this.initAction === 'edit') {
                this.fetchPost(this.initPostId)
                    .then(response => {
                        this.savedPost = response.data.data

                        this.form.title = this.savedPost.title
                        this.form.body = this.savedPost.title

                        this.seedTags = this.savedPost.tags.map(tag => {
                            return {
                                id: tag.id,
                                text: tag.name,
                            }
                        })

                        this.form.tags = this.savedPost.tags.map(tag => {
                            return tag.id
                        })

                        this.loaded = true
                    })
                    .catch(errors => {
                        flash('Failed to lost post data', 'danger')
                    })
            } else {
                this.loaded = true
            }
        },
        methods: {
            fetchPost(post_id) {
                return axios.get(`/api/posts/${post_id}`)
            },

            updateTags(payload) {
                if (payload.for === 'tags') {
                    this.form.tags = _.map(payload.tags, 'id')
                }
            },

            updatePostFromServer(post) {
                this.postId = post.id
                this.form.title = post.title
                this.form.body = post.body
            },

            deletePost() {
              this.showDeletePost = false;

            },

            savePost() {
                this.action = this.postId ?
                    'edit' :
                    'create'

                this.submittingType = 'saving';
                this.persistPost()
            },

            publishPost() {
                this.form.published_at = new Date()
                this.submittingType = 'publishing'
                this.persistPost();
            },

            unpublishPost() {
                this.action = 'unpublish'
                this.submittingType = 'unpublishing'
                this.turnOnSubmitting()

                axios.patch(`/posts/${this.postId}/unpublish`)
                    .then(response => {
                        flash('Post successfully unpublished!')

                        this.action = 'edit'

                        setTimeout(() => {
                            this.savedPost = response.post
                        }, this.timerDelay)

                        this.turnOffSubmitting()
                    })
                    .catch(errors => {
                        flash('Could not unpublish post.')
                        this.turnOffSubmitting()
                    })
            },

            persistPost() {
                this.turnOnSubmitting()

                this.form.submit(this.requestType, this.endpoint)
                    .then(response => {
                        this.action = 'edit'

                        if (response.action === 'create') {
                            flash('Post successfully created!')
                            this.postId = response.post.id
                        } else if (response.action === 'edit') {
                            flash('Post successfully saved!')
                        } else if (response.action === 'publish') {
                            flash('Post successfully published!')
                            this.postId = response.post.id
                        }

                        setTimeout(() => {
                            this.savedPost = response.post

                            history.pushState({}, 'Edit Post', this.endpoint)
                        }, this.timerDelay)

                        this.turnOffSubmitting()
                    })
                    .catch(errors => {
                        console.log('test')
                        if (this.action === 'save' || this.action === 'create') {
                            flash('Failed to save post.', 'danger')
                        } else if (this.action === 'publish') {
                            flash('Failed to publish post.', 'danger')
                        }

                        this.turnOffSubmitting()
                    })
            }
        },
        watch: {}
    }
</script>

<style>
    @import '~simplemde/dist/simplemde.min.css';
</style>
