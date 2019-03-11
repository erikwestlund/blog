
<script>
    export default {
        methods: {
            restoreRevisedField(payload) {
                Vue.set(this.form, payload.element, payload.revised)
                // this.form[payload.element] = payload.revised

                flash(`${payload.element.capitalize()} restored to editing form from revision. Click save to persist changes.`, 'warning')
            }
        }
    }
</script>

