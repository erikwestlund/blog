<template>
    <ul class="list-reset flex">
        <li
            v-for="(tag, tag_index) in tags"
            :key="tag.id"
            class="inline py-0 text-sm"
            :class="{'mr-3' : tags.length - 1 != tag_index }"
        >
            <a :href="tag.post_url">{{ tag.name }}</a>
        </li>
    </ul>
</template>

<script>
export default {
    props: {
        tags: {
            type: Array,
            required: true
        }
    }
}
</script>

<style scoped>

</style>
