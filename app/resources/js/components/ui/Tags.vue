<template>
    <vue-tags-input
            v-model="input"
            :tags="tags"
            :autocomplete-items="autoCompleteItems"
            @tags-changed="newTags => tags = newTags"
            @before-adding-tag="storeTag"
    />
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
            },
            initTags: {
                type: Array,
                default: [],
            }
        },
        data() {
            return {
                input: '',
                autoCompleteItems: [],
                tags: this.initTags,
                storedTags: []
            }
        },
        watch: {
            'input': 'fetchTags',
            'tags': 'sendUpdate',
            'initTags': 'seedTags'
        },
        methods: {
            seedTags() {
                this.tags = this.initTags.map(tag => {
                    return {
                        id: tag.id,
                        text: tag.text,
                        classes: "tags component-tagBox",
                    }
                })

                this.storedTags = this.initTags.map(tag => {
                    return {
                        id: tag.id,
                        name: tag.text,
                    }
                })
            },

            storeTag(obj) {
                axios.post('/tags', {
                    tag: obj.tag.text
                })
                    .then(response => {
                        obj.tag.classes = this.for + ' component-tagBox'
                        obj.addTag()
                        this.addStoredTag(response.data)
                    })
            },
            addStoredTag(tag) {
                let newTags = this.storedTags
                newTags.push(tag)

                this.storedTags = _.uniq(this.storedTags)
            },
            fetchTags() {
                axios.get('/tags', {
                    params: {
                        'q': this.input
                    }
                })
                    .then(response => {
                        this.autoCompleteItems = response.data.data.map(tag => {
                            return {text: tag.name}
                        })
                    })
            },
            sendUpdate() {
                const savedStoredTags = _.map(this.tags, (tag) => {
                    return _.find(this.storedTags, (storedTag) => {
                        return storedTag.name === tag.text
                    })
                })

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
