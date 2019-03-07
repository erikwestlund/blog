<script>
import SubmittingLabel from '../ui/SubmittingLabel'

export default {
    components: { SubmittingLabel },
    data () {
        return {
            deleting: false,
            publishing: false,
            saving: false,
            logging_in: false,
            uploading: false,
            unpublishing: false,
            submittingType: 'saving',
            timerDelay: 250
        }
    },
    computed: {
        submitting () {
            return this[this.submittingType]
        }
    },
    methods: {
        turnOnSubmitting () {
            this[this.submittingType] = true
        },

        turnOffSubmitting () {
            setTimeout(() => {
                this[this.submittingType] = false
            }, this.timerDelay)
        }
    }
}
</script>
