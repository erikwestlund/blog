<template>
    <div>
        <h2 class="font-normal">
            <fa-icon
                    class="text-grey mr-2"
                    :icon="['far', 'copy']"
            />
            Revisions
        </h2>
        <ul class="mt-4 list-reset" v-if="hasRevisions">
            <li v-for="revision in revisions"
                :key="revision.id"
                class="mt-3 flex items-center"
                :class="{'font-bold' : revisionIsLoaded(revision) }"
            >
                <fa-icon v-if="revisionIsLoaded(revision)"
                         class="fa-fw ml-1 mr-4 text-grey-dark"
                         :icon="['far', 'chevron-down']"/>
                <fa-icon v-else
                         class="fa-fw ml-1 mr-4 text-grey-dark"
                         :icon="['far', 'chevron-right']"/>
                <span class="mr-4 w-24">
                    {{ revision.created_at_ago}}
                </span>
                <button role="link" class="mr-4 text-sm w-12">
                    <fa-icon class="mr-1 text-grey" :icon="['far', 'search']"/>
                    <span class="cursor-pointer" @click="loadRevision(revision)">See</span>
                </button>
                <button v-show="revisionIsLoaded(revision)" role="link" class="mr-4 text-sm w-18" @click="restoreRevision(revision)">
                    <fa-icon class="mr-1 text-grey" :icon="['far', 'window-restore']"/>
                    Restore
                </button>
                <span class="ml-auto font-normal text-grey" v-if="revisionIsLoaded(revision)">
                    loaded below
                </span>
            </li>
        </ul>
        <div v-if="showRevision" class="mt-6 bg-white shadow rounded p-5">
            <h3>{{ visibleRevision.data.title }}</h3>
            <div class="mt-4">
                {{ visibleRevision.data.body }}
            </div>
        </div>
    </div>
</template>

<script>
    import Filters from '../mixins/FiltersMixin'

    export default {
        mixins: [Filters],
        created() {
            this.fetch()
        },
        computed: {
            hasRevisions() {
                return !_.isEmpty(this.revisions)
            },
            objectPlural() {
                return `${this.object}s`
            },
            showRevision() {
                return !_.isEmpty(this.visibleRevision)
            }
        },
        props: {
            objectId: {
                type: Number,
                required: true,
            },
            object: {
                type: String,
                required: true,
            }
        },
        data() {
            return {
                ready: false,
                post: {},
                revisions: {},
                visibleRevision: {}
            }
        },
        methods: {
            fetch() {
                this.ready = false

                axios.get(this.getEndpoint())
                    .then(response => {
                        this.revisions = response.data.data
                        this.ready = true
                    })
            },
            getEndpoint() {
                return `/admin/${this.objectPlural}/${this.objectId}/revisions`
            },
            loadRevision(revision) {
                this.visibleRevision = revision
                this.visibleRevision.data = JSON.parse(revision.revision)

            },
            revisionIsLoaded(revision) {
                return !_.isEmpty(this.visibleRevision) &&
                    this.visibleRevision.hasOwnProperty('id') &&
                    revision.id == this.visibleRevision.id
            },
            restoreRevision(revision) {
                Event.fire('restoreRevision', revision)
            }
        }
    }
</script>

<style scoped>

</style>