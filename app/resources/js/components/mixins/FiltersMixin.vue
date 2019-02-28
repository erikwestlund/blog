<script>
import { format, distanceInWordsToNow } from 'date-fns'
import { markdown } from 'markdown'

export default {
    filters: {
        number (value) {
            return value !== '' ? value : null
        },
        ago (date) {
            return distanceInWordsToNow(date)
        },
        date_written (date) {
            return format(date, ['MM/DD/YYYY @ hh:mm a'])
        },
        truncate (string, length) {
            return string.length <= length ? string : string.substring(0, length) + '...'
        },
        markdown (string) {
            return markdown.toHTML(string)
        }
    }
}
</script>
