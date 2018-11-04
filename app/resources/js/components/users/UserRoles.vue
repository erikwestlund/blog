<template>
    <div class="flex flex-wrap -mx-3 mb-6">
        <div class="w-full px-3">
            <label class="text-input-label mb-3"
                   :class="{'text-red' : hasErrors }"
                   for="grid-password">
                Roles
            </label>

            <div class="flex flex-wrap mb-3" v-for="role in possibleRoles" >
                <label class="text-grey-dark">
                    <input class="mr-2 leading-tight" :value="role.id" type="checkbox">
                    <span class="cursor-pointer">
                            {{ role.display_name }}
                    </span>
                </label>
            </div>

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
                return !_.isEmpty(this.errors);
            },
            errorMessage() {
                return this.hasErrors ?
                    this.errors[0] :
                    null
            }
        },
        props: {
            errors: {
                type: Array,
                required: true,
            },
            userRoles: {
                type: Array,
                required: true,
            },
            possibleRoles: {
                type: Array,
                required: true,
            }
        }
    }
</script>

<style scoped>

</style>