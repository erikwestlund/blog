<template>
    <div>
        <div class="max-w-thumbnail mr-2 ">
            <img
                    class="rounded-lg shadow"
                    :src="upload.url"
            >
        </div>
        <div class="flex-auto">
            <div class="flex mb-2 items-center">
                <input
                        readonly
                        class="border-grey-light bg-grey-lighter text-grey-dark w-100 text-input self-start p-1 mb-0 mr-1"
                        :value="upload.url"
                >
                <button class="btn btn-grey border-grey-light hover:bg-grey hover:border-grey py-1" @click="copyUrl">
                    <fa-icon :icon="['far', 'cut']" />
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            upload: {
                type: Object,
                required: true,
            }
        },
        methods: {
            copyUrl() {
                this.$copyText(this.upload.url).then(e => {
                    flash('Image URL copied to clipboard.')
                })
                    .catch(e => {
                        flash('Failed to copy URL to clipboard.', 'danger')
                    })
            }
        }
    }
</script>