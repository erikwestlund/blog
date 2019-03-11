<script>
export default {
    created () {
        Event.listen('revisionElementRestored', (payload) => this.flashRevisionElementRestoredMessage(payload))
    },
    methods: {
        flashRevisionElementRestoredMessage (payload) {
            let label = payload.label
                ? payload.label
                : payload.element.capitalize()

            flash(`${label} restored to editing form from revision. Click save to persist changes.`, 'warning')
        },
        restoreRevisedField (payload, flash = true) {
            Vue.set(this.form, payload.element, payload.revised)
            flash && Event.fire('revisionElementRestored', payload)
        }
    }
}
</script>
