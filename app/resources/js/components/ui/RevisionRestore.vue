<script>
    import ImageMixin from '../mixins/ImageMixin'
    import {diffWords, diffLines} from 'diff'

    export default {
        mixins: [ImageMixin],
        props: {
            form: {
                type: Object,
                required: true
            },
            revision: {
                type: Object,
                required: true
            }
        },
        methods: {
            getDiffColor(part) {
                return part.added ? 'green' :
                    part.removed ? 'red' : 'grey';
            },
            getWordDiff(first, second) {
                return diffWords(first, second);
            },
            getLineDiff() {
                return diffLines(first, second);
            },
        }
    }
</script>
