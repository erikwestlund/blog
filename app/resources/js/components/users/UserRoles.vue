<template>
    <div class="flex flex-wrap -mx-3 mb-6">
        <div class="w-full px-3">
            <label
                class="text-input-label mb-3"
                :class="{'text-red' : hasErrors }"
                for="grid-password"
            >
                Roles
            </label>

            <div
                v-for="role in possibleRoles"
                :key="role.id"
                class="flex flex-wrap mb-3"
            >
                <label class="text-grey-dark">
                    <input
                        v-model="userRoles"
                        class="mr-2 leading-tight"
                        :value="role.id"
                        type="checkbox"
                    >
                    <span class="cursor-pointer">
                        {{ role.display_name }}
                    </span>
                </label>
            </div>

            <p
                v-if="hasErrors"
                class="text-red text-xs italic"
                v-text="errorMessage"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: 'UserRoles',
    props: {
        errors: {
            type: Array,
            required: true
        },
        initUserRoles: {
            type: Array,
            required: true
        },
        possibleRoles: {
            type: Array,
            required: true
        }
    },
    data () {
        return {
            userRoles: this.initUserRoles
        }
    },
    computed: {
        hasErrors () {
            return !_.isEmpty(this.errors)
        },
        errorMessage () {
            return this.hasErrors
                ? this.errors[0]
                : null
        }
    },
    watch: {
        userRoles: 'sendUpdate'
    },
    methods: {
        sendUpdate () {
            Event.fire('updateUserRoles', this.userRoles)
        }
    }
}
</script>

<style scoped>

</style>
