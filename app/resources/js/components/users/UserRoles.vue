<template>
    <div class="flex flex-wrap -mx-3 mb-6">
        <div class="w-full px-3">
            <label class="text-input-label"
                   :class="{'text-red' : hasErrors }"
                   for="grid-password">
                Roles
            </label>

            <p class="text-red text-xs italic"
               v-if="hasErrors"
               v-text="errorMessage"></p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "UserRoles",
        computed: {
            hasErrors() {
                return ! _.isEmpty(this.errors);
            },
            errorMessage() {
                return this.hasErrors ?
                    this.errors[0] :
                    null
            }
        },
        data() {
            return {}
        },
        props: {
            errors: {
                type: Array,
                required: true,
            },
            initUserRoles: {
                type: Object,
                required: true,
            },
            possibleRoles: {
                type: Object,
                required: true,
            }
        }
    }
</script>

<style scoped>

</style>