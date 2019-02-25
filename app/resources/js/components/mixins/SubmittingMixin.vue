<script>
    import SubmittingLabel from '../ui/SubmittingLabel'

    export default {
        components: { SubmittingLabel },
        computed: {
            submitting() {
                return this[this.submittingType]
            },
        },
        data() {
            return {
                submittingType: 'saving',
                saving: false,
                publishing: false,
                unpublishing: false,
                timerDelay: 250,
            }
        },
        methods: {
            turnOnSubmitting() {
                this[this.submittingType] = true;
            },

            turnOffSubmitting() {

                setTimeout(() => {
                    this[this.submittingType] = false;
                }, this.timerDelay)
            }
        }
    }
</script>
