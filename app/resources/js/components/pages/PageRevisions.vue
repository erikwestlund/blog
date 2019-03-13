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
                <page-revision-restore
                    :revision="loadedRevision"
                    :form="form"
                    :images="images"
                    :primary-image="primaryImage"
                />
            </div>
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
    props: {
        images: {
            type: Array,
            default: () => {
                return []
            }
        },
        primaryImage: {
            type: Object,
            default: () => {
                return {}
            }
        }
    },
    created () {
        Event.listen('pageSaved', () => this.reset())
    }
}
</script>
