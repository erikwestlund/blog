<template>
    <div>
        <div v-if="hasRevisions">
            <h2 class="font-normal">
                <fa-icon
                    class="text-grey mr-2"
                    :icon="['far', 'copy']"
                />
                Revisions
            </h2>
            <revision-list
                :revisions="revisions"
                @loadRevision="loadRevision"
            />
            <div
                v-if="showRevision"
                class="mt-6"
            >
                <post-revision-restore :revision="loadedRevision" :form="form" />
            </div>
        </div>
    </div>
</template>

<script>
import Revisions from '../ui/Revisions'
import RevisionList from '../ui/RevisionList'
import PostRevisionRestore from './PostRevisionRestore'

export default {
    components: { RevisionList, PostRevisionRestore },
    extends: Revisions,
    created () {
        Event.listen('postSaved', () => this.reset())
    }
}
</script>

<style scoped>

</style>
