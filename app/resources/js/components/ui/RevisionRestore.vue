<script>
import ImageMixin from '../mixins/ImageMixin'
import { diffWords, diffLines, diffArrays, diffJson } from 'diff'

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
        getDiffColor (part) {
            return part.added ? 'green'
                : part.removed ? 'red' : 'grey'
        },
        getWordDiff (first, second) {
            return diffWords(first, second)
        },
        getLineDiff (first, second) {
            return diffLines(first, second)
        },
        getImagesDiff (first, second) {
            return diffArrays(first, second, { comparator: this.compareImages })
        },
        compareImages (first, second) {
            return first.url === second.url
        },
        getJsonDiff (first, second) {
            return diffJson(first, second)
        },
        tagsToList (tags) {
            return !_.isEmpty(tags)
                ? tags.map(tag => {
                    return tag.hasOwnProperty('text')
                        ? tag.text
                        : tag.name
                }).join(', ')
                : ''
        }
    }
}
</script>
