<template>
    <span>
        <fa-icon class="mr-2 fa-spin" :icon="['far', 'circle-notch']"/>
        {{ submittingText }}
    </span>
</template>

<script>
    export default {
        computed: {
            submittingText() {
                if (this.type == 'saving') {
                    return 'Saving...'
                } else if (this.type == 'publishing') {
                    return 'Publishing...'
                } else if (this.type == 'unpublishing') {
                    return 'Unpublishing...'
                } else {
                    return 'Submitting...'
                }
            }
        },
        props: {
            submitting: {
                type: Boolean,
                default: false
            },
            type: {
                type: String,
                default: 'submitting'
            }
        }
    }
</script>