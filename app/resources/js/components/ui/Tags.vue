<template>
    <div>
        <vue-tags-input
                v-model="tag"
                :tags="tags"
                @tags-changed="updateTags"
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
                tag: '',
                tags: [],
            };
        },
        methods: {
            updateTags(tags) {
                this.tags = tags
            }
        }
    };
</script>


<style scoped>

</style>