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
        <div class="w-1/4">
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
              :for="action"
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
            <button v-show="! isPublished "
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
  computed: {
    isPublished() {
      return !_.isEmpty(this.publishedPost)
    }
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
  data () {
    return {
      action: this.initAction,
      submitting: false,
      savedPost: {},
      publishedPost: {},
      loaded: false,
      form: new Form({
        action: 'save',
        post_id: '',
        tags: [],
        title: '',
        body: ''
      })
    }
  },
  computed: {
    actionIcon () {
      return this.action === 'create'
        ? 'plus-circle'
        : 'pencil'
    },

    isPublished () {
      if (
        !_.isEmpty(this.savedPost) &&
                    _.isDate(this.savedPost.published_at)
      ) {
        return true
      }

      return false
    }
  },
  created () {
    Event.listen('tagsUpdated', (payload) => this.updateTags(payload))

    this.loaded = true
  },
  methods: {
    updateTags (payload) {
      if (payload.for === this.name) {
        this.form.tags = payload.tags
      }
    },

    publishPost () {
      this.savePost('publish');
    },

    savePost (action = 'save') {
      this.form.action = action

      this.form.submit('post', this.endpoint)
        .then(response => {
          console.log(response)
        })
        .catch(errors => {
          console.log(errors)
        })
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
