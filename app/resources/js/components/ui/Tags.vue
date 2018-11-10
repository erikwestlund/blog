<template>
    <div>
        <vue-tags-input
                v-model="input"
                :tags="tags"
                :autocomplete-items="autoCompleteItems"
                @tags-changed="updateTags"
                @before-adding-tag="createTag"
        />
    </div>
</template>

<script>
    import VueTagsInput from '@johmun/vue-tags-input';

    export default {
        components: {
            'vue-tags-input': VueTagsInput,
        },
        data() {
            return {
                input: '',
                autoCompleteItems: [],
                tags: [],
            };
        },
        methods: {
            createTag(obj) {
                axios.post('/tags', obj)
            },
            fetchTags() {
                axios.get('/tags', {
                    params: {
                        'q': this.input,
                    }
                })
                    .then(response => {
                        this.autoCompleteItems = response.data.data.map(tag => {
                            return {text: tag.name};
                        });
                    })
            },
            updateTags(tags) {
                this.tags = tags
            }
        },
        watch: {
            'input': 'fetchTags',
        },
    };
</script>


<style scoped>

</style>