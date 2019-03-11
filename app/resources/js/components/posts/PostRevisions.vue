<template>
    <div>
        <h2 class="font-normal">
            <fa-icon
                    class="text-grey mr-2"
                    :icon="['far', 'copy']"
            />
            Revisions
        </h2>
        <revision-list v-if="hasRevisions"
                       :revisions="revisions"
                       @loadRevision="loadRevision"
        />
        <div v-if="showRevision" class="mt-6">
            <post-revision-restore :revision="loadedRevision"/>
        </div>
    </div>
</template>

<script>
    import Revisions from '../ui/Revisions'
    import RevisionList from '../ui/RevisionList'
    import PostRevisionRestore from './PostRevisionRestore'

    export default {
        extends: Revisions,
        components: {RevisionList, PostRevisionRestore},
        data() {
            return {
                loadedRevision: {}
            }
        },
        methods: {
            loadRevision(revision) {
                this.loadedRevision = revision.revision
            },
        }
    }
</script>

<style scoped>

</style>