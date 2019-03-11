<script>
import ImageMixin from '../mixins/ImageMixin'

export default {
    mixins: [ImageMixin],
    props: {
        revision: {
            type: Object,
            required: true
        }
    }
}
</script>
