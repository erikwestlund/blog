<template>
    <ul class="mt-4 list-reset">
        <li
            v-for="revision in revisions"
            :key="revision.id"
            class="mt-3 flex items-center"
            :class="{'font-bold' : revisionIsLoaded(revision) }"
        >
            <fa-icon
                v-if="revisionIsLoaded(revision)"
                class="fa-fw ml-1 mr-4 text-grey-dark"
                :icon="['far', 'chevron-down']"
            />
            <fa-icon
                v-else
                class="fa-fw ml-1 mr-4 text-grey-dark"
                :icon="['far', 'chevron-right']"
            />
            <span class="mr-4 w-32">
                {{ revision.created_at_ago }}
            </span>
            <button
                role="link"
                class="mr-4 text-sm w-12"
            >
                <fa-icon
                    class="mr-1 text-grey"
                    :icon="['far', 'search']"
                />
                <span
                    class="cursor-pointer"
                    @click="loadRevision(revision)"
                >See</span>
            </button>
            <span
                v-if="revisionIsLoaded(revision)"
                class="ml-auto font-normal text-grey"
            >
                loaded
            </span>
        </li>
    </ul>
</template>

<script>
export default {
    props: {
        revisions: {
            type: Array,
            required: true
        }
    },
    data () {
        return {
            visibleRevision: {}
        }
    },
    watch: {
        'revisions': 'reset'
    },
    methods: {
        reset () {
            this.visibleRevision = {}
        },
        loadRevision (revision) {
            this.visibleRevision = revision
            this.$emit('loadRevision', revision)
        },
        revisionIsLoaded (revision) {
            return !_.isEmpty(this.visibleRevision) &&
                    this.visibleRevision.hasOwnProperty('id') &&
                    revision.id === this.visibleRevision.id
        }
    }
}
</script>
