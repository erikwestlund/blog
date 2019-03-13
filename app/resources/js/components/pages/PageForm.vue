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
                <span class="capitalize">{{ action }}</span> Page
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
                    <div
                        v-if="isSaved"
                        class="w-full"
                    >
                        <label
                            class="text-input-label"
                            for="grid-url"
                        >
                            URL
                        </label>
                        <div
                            class="flex"
                            url
                        >
                            <input
                                readonly
                                class="border-grey-light bg-grey-lighter text-grey-dark w-100 text-input self-start p-1 mb-0 mr-1 h-7"
                                :value="savedPage.url"
                            >
                            <button
                                class="btn btn-grey border-grey-light hover:bg-grey hover:border-grey py-1 mr-2"
                                @click="copyUrl(savedPage.url)"
                            >
                                <fa-icon :icon="['far', 'cut']" />
                            </button>
                            <a
                                role="button"
                                :href="savedPage.url"
                                target="_blank"
                                class="btn btn-grey border-grey-light hover:bg-grey hover:border-grey py-1"
                            >
                                <fa-icon :icon="['far', 'external-link']" />
                            </a>
                        </div>
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
                            @save="pageSave"
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
                        <image-upload-collection
                            parent-type="page"
                            :init-image-uploads="uploadedImages"
                        />
                    </div>
                    <div class="w-full mt-10">
                        <page-revisions
                            v-if="isSaved"
                            object="page"
                            :form="form"
                            :object-id="savedPage.id"
                            :images="uploadedImages"
                            :primary-image="primaryImage"
                        />
                    </div>
                </div>
                <div class="w-full xl:w-1/3 mt-5 xl:mt-0 p-3">
                    <div class="mt-6 md:flex">
                        <button
                            class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest mr-2"
                            :disabled="form.errors.any() || saving"
                            @click="pageSave()"
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
                        <transition name="trx-fade-in">
                            <button
                                v-show="form.body"
                                class="btn btn-grey hover:bg-grey hover:border-grey p-2"
                                @click.prevent="showPreview()"
                            >
                                <fa-icon
                                    class="mr-2"
                                    :icon="['far', 'search']"
                                />
                                Preview
                            </button>
                        </transition>
                    </div>
                    <div
                        v-if="isSaved"
                        class="mt-5"
                    >
                        <button
                            class="text-sm text-red-darker ml-1"
                            @click="showDeletePage = true"
                        >
                            <fa-icon
                                class="mr-2"
                                :icon="['far', 'trash']"
                            />
                            Delete
                        </button>
                    </div>
                    <div
                        v-show="notSaved"
                        class="mt-5 text-grey text-sm"
                    >
                        This page has not been saved.
                    </div>
                    <div class="mt-10">
                        <image-primary
                            parent-type="page"
                            :image="primaryImage"
                        />
                    </div>
                </div>
            </div>
            <modal
                :show="showDeletePage"
                no-footer
                @close="showDeletePage = false"
            >
                <h3 slot="header">
                    Delete Page
                </h3>

                <div
                    slot="body"
                >
                    Are you you want to delete this page?

                    <div class="mt-6">
                        <button
                            class="btn btn-red hover:bg-red-darkest hover:border-red-darkest"
                            @click.prevent="pageDelete()"
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

            <page-preview
                :body="form.body"
                :title="form.title"
            />
        </form>
    </div>
</template>

<script>
import Form from '../../modules/Form'
import Modal from '../ui/Modal'
import ImageUploadCollection from '../ui/ImageUploadCollection'
import ImagePrimary from '../ui/ImagePrimary'
import SubmittingMixin from '../mixins/SubmittingMixin'
import { mavonEditor } from 'mavon-editor'
import FileUploadImageMixin from '../mixins/FileUploadImageMixin'
import PagePreview from './PagePreview'
import CopyMixin from '../mixins/CopyMixin'
import PageRevisions from './PageRevisions'
import RevisionMixin from '../mixins/RevisionMixin'

export default {
    name: 'Page',

    components: {
        Modal,
        ImagePrimary,
        ImageUploadCollection,
        mavonEditor,
        PagePreview,
        PageRevisions
    },
    mixins: [FileUploadImageMixin, SubmittingMixin, CopyMixin, RevisionMixin],

    props: {
        initAction: {
            type: String,
            default: 'create'
        },

        initPageId: {
            type: Number,
            required: false,
            default: null
        }
    },

    data () {
        return {
            objectType: 'page',
            state: window.State,
            now: new Date().toISOString(),
            savedPage: {},
            loaded: false,
            pageId: this.initPageId,
            action: this.initAction,
            primaryImage: {},
            showDeletePage: false,
            showPreviewPage: false,
            form: new Form(
                {
                    title: '',
                    body: '',
                    slug: '',
                    uploaded_images: [],
                    primary_image_id: ''
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
        actionIcon () {
            return this.action === 'create'
                ? 'plus-circle'
                : 'file-alt'
        },

        endpoint () {
            return this.action === 'edit'
                ? `/admin/pages/${this.pageId}`
                : '/admin/pages/create'
        },

        hasSlug () {
            return this.form.slug
        },

        isSaved () {
            return this.pageId && !_.isEmpty(this.savedPage)
        },

        isUpdateForm () {
            return this.action !== 'create'
        },

        notSaved () {
            return !this.pageId
        },

        requestType () {
            return this.isSaved
                ? 'patch'
                : 'post'
        }
    },
    watch: {
        'uploadedImages': 'updateFormUploadedImages',
        'primaryImage': 'updateFormPrimaryImage'
    },

    created () {
        setInterval(() => {
            this.now = new Date().toISOString()
        }, 100)

        Event.listen('imageDeletedFromUploads', (refreshUploadedImages) => this.refreshUploadedImages(refreshUploadedImages))
        Event.listen('setPrimaryImage', (payload) => this.setPrimaryImage(payload))
        Event.listen('clearPrimaryImage', (type) => this.clearPrimaryImage(type))
        Event.listen('restoreRevisedPageField', (revision) => this.restoreRevisedField(revision))
        Event.listen('restoreRevisedImages', (images) => this.restoreRevisedImages(images))
        Event.listen('restoreRevisedPrimaryImage', (image) => this.restoreRevisedPrimaryImage(image))
        Event.listen('restoreRevisedPage', (revision) => this.restoreRevisedPage(revision))

        if (this.initPageId && this.initAction === 'edit') {
            this.pageFetch(this.initPageId)
                .then(response => {
                    this.pageLoad(response.data.data)

                    this.loaded = true
                })
                .catch(errors => {
                    flash('Failed to lost page data', 'danger')
                })
        } else {
            this.loaded = true
        }
    },

    methods: {
        clearPrimaryImage (type) {
            if (type === 'page') {
                Vue.set(this, 'primaryImage', null)
            }
        },

        editorUploadImage (pos, $formData) {
            this.uploadImage($formData, pos)
        },

        editorDeleteImage (image) {
            Event.fire('uploadedImageTrashed', image)
        },

        pageDelete () {
            this.action = 'delete'
            this.submittingType = 'deleting'
            this.turnOnSubmitting()

            axios.delete(`/admin/pages/${this.pageId}`)
                .then(response => {
                    setTimeout(() => {
                        window.location.replace('/admin/pages')
                    }, 250)
                })
                .catch(errors => {
                    flash('Could not delete page.', 'danger')
                    this.turnOffSubmitting()
                })
        },

        pageFetch (pageId) {
            return axios.get(`/admin/pages/${pageId}.json`)
        },

        pageLoad (savedPage) {
            this.savedPage = savedPage

            this.form.title = this.savedPage.title
            this.form.body = this.savedPage.body
            this.form.primary_image_id = this.savedPage.primary_image_id || null
            this.form.slug = this.savedPage.slug || ''
            this.uploadedImages = this.savedPage.images
            this.form.uploaded_images = this.savedPage.images.map(image => {
                return image.id
            })

            if (this.savedPage.primary_image) {
                const primaryImageId = this.savedPage.primary_image.id
                this.primaryImage = _.find(this.savedPage.images, (image) => {
                    return image.id === primaryImageId
                })
            }
        },

        pagePersist () {
            this.turnOnSubmitting()

            this.form.submit(this.requestType, this.endpoint)
                .then(response => {
                    this.action = 'edit'

                    if (response.action === 'create') {
                        flash('Page successfully created!')
                        this.pageId = response.page.id
                    } else if (response.action === 'edit') {
                        flash('Page successfully saved!')
                    }

                    this.form.slug = response.page.slug

                    setTimeout(() => {
                        this.savedPage = response.page

                        history.pushState({}, 'Edit Page', this.endpoint)
                    }, this.timerDelay)

                    Event.fire('pageSaved')

                    this.turnOffSubmitting()
                })
                .catch(errors => {
                    flash('Failed to save page.', 'danger')

                    this.turnOffSubmitting()
                })
        },

        pageSave () {
            this.action = this.pageId
                ? 'edit'
                : 'create'

            this.submittingType = 'saving'
            this.pagePersist()
        },

        restoreRevisedImages (revision, flash = true) {
            this.uploadedImages = _.clone(revision.images)
            this.restoreRevisedPrimaryImage(revision.primary_image, false)

            flash && Event.fire('revisionElementRestored', { element: 'images' })
        },

        restoreRevisedPrimaryImage (image, flash = true) {
            this.primaryImage = _.clone(image)
            flash && Event.fire('revisionElementRestored', { element: 'primary image' })
        },

        restoreRevisedPage (revision) {
            this.restoreRevisedField({ element: 'title', revised: revision.title }, false)
            this.restoreRevisedField({ element: 'slug', revised: revision.slug }, false)
            this.restoreRevisedField({ element: 'body', revised: revision.body }, false)
            this.restoreRevisedImages(revision.images, false)
            this.restoreRevisedPrimaryImage(revision.primary_image, false)

            Event.fire('revisionElementRestored', { element: 'all fields' })
        },

        showPreview () {
            Event.fire('showPagePreview')
        }
    }
}
</script>

<style>
    @import '~vue-datetime/dist/vue-datetime.min.css';
    @import '~mavon-editor/dist/css/index.css';
</style>
