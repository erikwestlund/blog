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
                <span class="capitalize">{{ action }}</span> Post
            </h1>
            <div class="block xl:flex mt-6">
                <div class="w-full p-3 xl:w-2/3 ">
                    <div class="w-full">
                        <label
                                class="text-input-label"
                                for="grid-title"
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
                    <div
                            v-if="hasSlug"
                            class="w-full mt-5"
                    >
                        <label
                                class="text-input-label"
                                for="grid-slug"
                        >
                            Slug
                        </label>
                        <input
                                id="grid-slug"
                                v-model="form.slug"
                                class="text-input focus:outline-none focus:border-grey"
                                name="slug"
                                :class="{'border border-red' : form.errors.has('slug')}"
                                placeholder="Slug"
                        >
                        <p
                                v-if="form.errors.has('slug')"
                                class="text-red text-xs italic"
                                v-text="form.errors.get('slug')"
                        />
                    </div>
                    <div class="w-full mt-5">
                        <label
                                class="text-input-label"
                                for="grid-body"
                        >
                            Body
                        </label>
                        <mavon-editor
                                ref="markdownEditor"
                                v-model="form.body"
                                class="rounded"
                                language="en"
                                font-size="14px"
                                placeholder="Body"
                                :box-shadow="false"
                                :subfield="false"
                                :toolbars="mavonToolbarSettings"
                                :class="{'border border-red' : form.errors.has('body')}"
                                @imgAdd="editorUploadImage"
                                @imgDel="editorDeleteImage"
                                @save="postSave"
                        />

                        <p
                                v-if="form.errors.has('body')"
                                class="text-red text-xs italic mt-3"
                                v-text="form.errors.get('body')"
                        />

                        <div
                                class="text-grey text-right text-xs mt-3 h-4"
                        >
                            <submitting-label
                                    v-if="uploading_image"
                                    type="uploading_image"
                            />
                        </div>
                    </div>
                    <div class="w-full mt-4">
                        <image-uploads :init-image-uploads="uploadedImages"/>
                    </div>
                </div>
                <div class="w-full xl:w-1/3 mt-5 xl:mt-0 p-3">
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
                    <div class="w-full mt-6">
                        <div>
                            <span
                                    v-if="publishTimeSet"
                                    class="text-sm text-red-darker cursor-pointer ml-auto float-right"
                                    @click="clearPublishedAt()"
                            >
                                <fa-icon
                                        class="mr-1"
                                        :icon="['far', 'times']"
                                />
                            </span>
                            <label
                                    class="text-input-label"
                                    for="grid-published"
                            >
                                {{ publishOnLabel }}
                            </label>
                        </div>
                        <label
                                v-if="! publishTimeSet"
                                class="w-full block text-grey cursor-pointer flex mb-2"
                        >
                            <input
                                    v-model="setPublishTimeManually"
                                    class="mr-2 leading-tight"
                                    type="checkbox"
                            >
                            <span class="text-sm">
                                Set publish time manually.
                            </span>
                        </label>

                        <div v-if="showPublishTimePicker">
                            <datetime
                                    v-model="form.published_at"
                                    type="datetime"
                                    placeholder="Select date"
                                    input-class="text-input focus:outline-none focus:border-grey"
                                    zone="local"
                                    :format="{ year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: '2-digit' }"
                                    :phrases="{ok: 'Save', cancel: 'Cancel'}"
                                    :week-start="7"
                                    use12-hour
                                    auto
                            />
                        </div>
                    </div>
                    <div class="mt-6">
                        <button
                                class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest mr-2"
                                :disabled="form.errors.any() || saving"
                                @click="postSave()"
                        >
                            <submitting-label
                                    v-if="saving"
                                    type="saving"
                            />
                            <span v-else>
                                <fa-icon
                                        class="mr-2"
                                        :icon="['far', 'save']"
                                />
                                Save
                            </span>
                        </button>
                        <button
                                v-show="! isPublished"
                                class="btn btn-green hover:bg-green-dark hover:border-green-dark mr-2"
                                :disabled="form.errors.any() || publishing"
                                @click="postPublish()"
                        >
                            <submitting-label
                                    v-if="publishing"
                                    type="publishing"
                            />
                            <span v-else>
                                <fa-icon
                                        class="mr-2"
                                        :icon="['far', 'eye']"
                                />
                                Publish
                            </span>
                        </button>
                        <button
                                v-show="isPublished"
                                class="btn btn-orange hover:bg-orange-darker hover:border-orange-darker mr-2"
                                :disabled="form.errors.any() || unpublishing"
                                @click.prevent="postUnpublish()"
                        >
                            <submitting-label
                                    v-if="unpublishing"
                                    type="unpublishing"
                            />
                            <span v-else>
                                <fa-icon
                                        class="mr-2"
                                        :icon="['far', 'eye-slash']"
                                />
                                Unpublish
                            </span>
                        </button>
                        <button class="btn btn-white hover:bg-grey-lightest hover:border-grey p-2 mr-2" @click.prevent="showPreview()">
                            <fa-icon class="mr-2" :icon="['far', 'search']" /> Preview
                        </button>
                    </div>
                    <div
                            v-if="isSaved"
                            class="mt-5"
                    >
                        <button
                                class="text-sm text-red-darker ml-1"
                                @click="showDeletePost = true"
                        >
                            <fa-icon
                                    class="mr-2"
                                    :icon="['far', 'trash']"
                            />
                            Delete
                        </button>
                    </div>
                    <div
                            v-show="savedButNotPublished"
                            class="mt-5 text-grey text-sm"
                    >
                        This post has not been published.
                    </div>
                    <div
                            v-show="notSaved"
                            class="mt-5 text-grey text-sm"
                    >
                        This post has not been saved.
                    </div>
                </div>
            </div>
            <modal
                    :show="showDeletePost"
                    no-footer
                    @close="showDeletePost = false"
            >
                <h3 slot="header">
                    Delete Post
                </h3>

                <div
                        slot="body"
                >
                    Are you you want to delete this post?

                    <div class="mt-6">
                        <button
                                class="btn btn-red hover:bg-red-darkest hover:border-red-darkest"
                                @click.prevent="postDelete()"
                        >
                            <submitting-label
                                    v-if="deleting"
                                    type="deleting"
                            />
                            <span v-else>
                                <fa-icon
                                        class="mr-2"
                                        :icon="['far', 'trash']"
                                />
                                Delete It
                            </span>
                        </button>
                    </div>
                </div>
            </modal>

            <post-preview :body="form.body" :title="form.title"></post-preview>
        </form>
    </div>
</template>

<script>
    import Form from '../../modules/Form'
    import Modal from '../ui/Modal'
    import Tags from '../ui/Tags'
    import ImageUploads from './PostImageUploads'
    import SubmittingMixin from '../mixins/SubmittingMixin'
    import {Datetime} from 'vue-datetime'
    import {mavonEditor} from 'mavon-editor'
    import FileUploadImageMixin from '../mixins/FileUploadImageMixin'
    import PostPreview from './PostPreview'

    export default {
        name: 'Post',

        components: {
            Datetime,
            Modal,
            Tags,
            ImageUploads,
            mavonEditor,
            PostPreview
        },
        mixins: [FileUploadImageMixin, SubmittingMixin],

        props: {
            initAction: {
                type: String,
                default: 'create'
            },

            initPostId: {
                type: Number,
                required: false,
                default: null
            }
        },

        data() {
            return {
                now: new Date().toISOString(),
                savedPost: {},
                loaded: false,
                postId: this.initPostId,
                action: this.initAction,
                seedTags: [],
                setPublishTimeManually: false,
                showDeletePost: false,
                showPreviewPost: false,
                form: new Form(
                    {
                        tags: [],
                        title: '',
                        body: '',
                        published_at: '',
                        slug: '',
                        uploaded_images: []
                    },
                    this.isUpdateForm,
                    true
                ),
                mavonToolbarSettings: {
                    bold: true,
                    italic: true,
                    header: true,
                    underline: true,
                    mark: true,
                    quote: true,
                    ol: true,
                    ul: true,
                    link: true,
                    imagelink: true,
                    code: true,
                    table: true,
                    alignleft: true,
                    aligncenter: true,
                    alignright: true,
                    preview: true
                }
            }
        },

        computed: {
            actionIcon() {
                return this.action === 'create'
                    ? 'plus-circle'
                    : 'pencil'
            },

            endpoint() {
                return this.action === 'edit'
                    ? `/admin/posts/${this.postId}`
                    : '/admin/posts/create'
            },

            hasSlug() {
                return this.form.slug
            },

            isPublished() {
                return this.isSaved &&
                    this.savedPost.published_at
            },

            isSaved() {
                return this.postId && !_.isEmpty(this.savedPost)
            },

            isUpdateForm() {
                return this.action !== 'create'
            },

            notSaved() {
                return !this.postId
            },

            requestType() {
                return this.isSaved
                    ? 'patch'
                    : 'post'
            },

            publishTimeSet() {
                return this.form.published_at
            },

            publishInFuture() {
                return this.form.published_at > this.now
            },

            publishedInPast() {
                return this.form.published_at <= this.now
            },

            publishOnLabel() {
                return this.publishedInPast
                    ? 'Published'
                    : 'Publish On'
            },

            savedButNotPublished() {
                return this.isSaved && !this.isPublished
            },

            showPublishTimePicker() {
                return this.setPublishTimeManually || this.form.published_at
            }
        },
        watch: {
            'uploadedImages': 'updateFormUploadedImages'
        },

        created() {
            setInterval(() => {
                this.now = new Date().toISOString()
            }, 100)

            Event.listen('tagsUpdated', (payload) => this.tagsUpdate(payload))
            Event.listen('imageDeletedFromUploads', (refreshUploadedImages) => this.refreshUploadedImages(refreshUploadedImages))

            if (this.initPostId && this.initAction === 'edit') {
                this.postFetch(this.initPostId)
                    .then(response => {
                        this.savedPost = response.data.data

                        this.form.title = this.savedPost.title
                        this.form.body = this.savedPost.body
                        this.form.published_at = this.savedPost.published_at
                            ? new Date(this.savedPost.published_at).toISOString()
                            : ''
                        this.form.slug = this.savedPost.slug || ''
                        this.uploadedImages = this.savedPost.images
                        this.form.uploaded_images = this.savedPost.images.map(image => {
                            return image.id
                        })

                        this.seedTags = this.savedPost.tags.map(tag => {
                            return {
                                id: tag.id,
                                text: tag.name
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

            clearPublishedAt() {
                this.form.published_at = ''
            },

            editorUploadImage(pos, $formData) {
                this.uploadImage($formData, pos)
            },

            editorDeleteImage(image) {
                Event.fire('uploadedImageTrashed', image)
            },

            postDelete() {
                this.action = 'delete'
                this.submittingType = 'deleting'
                this.turnOnSubmitting()

                axios.delete(`/admin/posts/${this.postId}`)
                    .then(response => {
                        setTimeout(() => {
                            window.location.replace('/admin/posts')
                        }, 250)
                    })
                    .catch(errors => {
                        flash('Could not delete post.', 'danger')
                        this.turnOffSubmitting()
                    })
            },

            postFetch(postId) {
                return axios.get(`/admin/posts/${postId}.json`)
            },

            postPersist() {
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

                        this.form.slug = response.post.slug

                        setTimeout(() => {
                            this.savedPost = response.post

                            history.pushState({}, 'Edit Post', this.endpoint)
                        }, this.timerDelay)

                        this.turnOffSubmitting()
                    })
                    .catch(errors => {
                        if (this.action === 'save' || this.action === 'create') {
                            flash('Failed to save post.', 'danger')
                        } else if (this.action === 'publish') {
                            flash('Failed to publish post.', 'danger')
                        }

                        this.turnOffSubmitting()
                    })
            },

            postPublish() {
                this.form.published_at = new Date().toISOString()
                this.submittingType = 'publishing'
                this.postPersist()
            },

            postSave() {
                this.action = this.postId
                    ? 'edit'
                    : 'create'

                this.submittingType = 'saving'
                this.postPersist()
            },

            postUnpublish() {
                this.action = 'unpublish'
                this.submittingType = 'unpublishing'
                this.turnOnSubmitting()

                axios.patch(`/admin/posts/${this.postId}/unpublish`)
                    .then(response => {
                        flash('Post successfully unpublished!')

                        this.action = 'edit'
                        this.form.published_at = ''

                        setTimeout(() => {
                            this.savedPost = response.data.post
                        }, this.timerDelay)

                        this.turnOffSubmitting()
                    })
                    .catch(errors => {
                        flash('Could not unpublish post.', 'danger')
                        this.turnOffSubmitting()
                    })
            },

            refreshUploadedImages(uploadedImages) {
                this.uploadedImages = _.clone(uploadedImages)
            },

            showPreview() {
              Event.fire('showPostPreview')
            },

            tagsUpdate(payload) {
                if (payload.for === 'tags') {
                    this.form.tags = _.map(payload.tags, 'id')
                }
            },

            updateFormUploadedImages() {
                Vue.set(this.form, 'uploaded_images', this.uploadedImages.map(image => {
                    return image.id
                }))
            }
        }
    }
</script>

<style>
    @import '~vue-datetime/dist/vue-datetime.min.css';
    @import '~mavon-editor/dist/css/index.css';

    .vue-tags-input.component-tags {
        max-width: 100%;
    }

</style>
