<template>
  <div>
    <vue-tags-input
      v-model="input"
      :tags="tags"
      :autocomplete-items="autoCompleteItems"
      @tags-changed="newTags => tags = newTags"
      @before-adding-tag="storeTag"
    />
  </div>
</template>

<script>
import VueTagsInput from '@johmun/vue-tags-input'

export default {
  components: {
    'vue-tags-input': VueTagsInput
  },
  props: {
    for: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      input: '',
      autoCompleteItems: [],
      tags: [],
      storedTags: []
    }
  },
  watch: {
    'input': 'fetchTags',
    'tags': 'sendUpdate'
  },
  methods: {

    storeTag (obj) {
      axios.post('/tags', {
        tag: obj.tag.text
      })
        .then(response => {
          obj.tag.classes = this.for + ' component-tagBox'
          obj.addTag()
          this.addStoredTag(response.data)
        })
    },
    addStoredTag (tag) {
      let newTags = this.storedTags
      newTags.push(tag)

      this.storedTags = _.uniq(this.storedTags)
    },
    fetchTags () {
      axios.get('/tags', {
        params: {
          'q': this.input
        }
      })
        .then(response => {
          this.autoCompleteItems = response.data.data.map(tag => {
            return { text: tag.name }
          })
        })
    },
    sendUpdate () {
      const savedStoredTags = _.map(this.tags, (tag) => {
        return _.find(this.storedTags, (storedTag) => {
          return storedTag.name === tag.text
        })
      })
      console.log(savedStoredTags)
      Event.fire('tagsUpdated', {
        for: this.for,
        tags: savedStoredTags
      })
    }
  }
}
</script>

<style scoped>

</style>
