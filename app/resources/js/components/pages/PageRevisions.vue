<template>
    <div>
        <h2 class="font-normal">
            <fa-icon
                class="text-grey mr-2"
                :icon="['far', 'copy']"
            />
            Revisions
        </h2>
        <revision-list
            v-if="hasRevisions"
            :revisions="revisions"
            @loadRevision="loadRevision"
        />
        <div
            v-if="showRevision"
            class="mt-6"
        >
            <page-revision-restore :revision="loadedRevision" />
        </div>
    </div>
</template>

<script>
import Revisions from '../ui/Revisions'
import RevisionList from '../ui/RevisionList'
import PageRevisionRestore from './PageRevisionRestore'

export default {
    components: { RevisionList, PageRevisionRestore },
    extends: Revisions,
    created () {
        Event.listen('pageSaved', () => this.reset())
    }
}
</script>
