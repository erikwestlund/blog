<template>
    <div class="flex">
        <form
            class="w-full"
            method="PATCH"
            :action="endpoint"
            @submit.prevent="onSubmit"
            @keydown="form.errors.clear($event.target.name)"
        >
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full px-3">
                    <label
                        class="text-input-label"
                        :class="{'text-red' : form.errors.has('username')}"
                        for="grid-username"
                    >
                        Username
                    </label>
                    <input
                        id="grid-username"
                        v-model="form.username"
                        class="text-input focus:outline-none focus:border-grey"
                        name="username"
                        :class="{'border border-red' : form.errors.has('username')}"
                        placeholder="Username"
                    >
                    <p
                        v-if="form.errors.has('username')"
                        class="text-red text-xs italic"
                        v-text="form.errors.get('username')"
                    />
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                    <label
                        class="text-input-label"
                        for="grid-first-name"
                    >
                        First Name
                    </label>
                    <input
                        id="grid-first-name"
                        v-model="form.first_name"
                        class="text-input focus:outline-none focus:border-grey"
                        name="first_name"
                        type="text"
                        placeholder="Jane"
                    >
                </div>
                <div class="w-full md:w-1/2 px-3">
                    <label
                        class="text-input-label"
                        for="grid-last-name"
                    >
                        Last Name
                    </label>
                    <input
                        id="grid-last-name"
                        v-model="form.last_name"
                        class="text-input focus:outline-none focus:border-grey"
                        name="last_name"
                        type="text"
                        placeholder="Doe"
                    >
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full px-3">
                    <label
                        class="text-input-label"
                        :class="{'text-red' : form.errors.has('email')}"
                        for="grid-email"
                    >
                        Email
                    </label>
                    <input
                        id="grid-email"
                        v-model="form.email"
                        class="text-input focus:outline-none focus:border-grey"
                        :class="{'border border-red' : form.errors.has('email')}"
                        name="email"
                        placeholder="name@domain.com"
                    >
                    <p
                        v-if="form.errors.has('email')"
                        class="text-red text-xs italic"
                        v-text="form.errors.get('email')"
                    />
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full px-3">
                    <label
                        class="text-input-label"
                        :class="{'text-red' : form.errors.has('password') || form.errors.has('password_confirm')}"
                        for="grid-password"
                    >
                        Password
                    </label>
                    <input
                        id="grid-password"
                        v-model="form.password"
                        class="text-input focus:outline-none focus:border-grey"
                        :class="{'border border-red' : form.errors.has('password')}"
                        name="password"
                        type="password"
                        placeholder="Password"
                    >
                    <p
                        v-if="form.errors.has('password')"
                        class="text-red text-xs italic mb-4"
                        v-text="form.errors.get('password')"
                    />
                    <input
                        id="grid-password-confirm"
                        v-model="form.password_confirm"
                        class="text-input focus:outline-none focus:border-grey"
                        :class="{'border border-red' : form.errors.has('password_confirm')}"
                        name="password_confirm"
                        type="password"
                        placeholder="Confirm password"
                    >
                    <p
                        v-if="form.errors.has('password_confirm')"
                        class="text-red text-xs italic"
                        v-text="form.errors.get('password_confirm')"
                    />
                </div>
            </div>
            <user-roles
                v-if="isAdmin"
                :possible-roles="possibleRoles"
                :init-user-roles="form.user_roles"
                :errors="rolesErrors"
            />
            <div class="flex flex-wrap">
                <button
                    class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                    :disabled="form.errors.any() || submitting"
                >
                    Update Account
                </button>
            </div>
        </form>
    </div>
</template>x

<script>
import Form from '../../modules/Form.js'
import UserRoles from './UserRoles'

export default {
    name: 'EditUser',
    components: {
        'user-roles': UserRoles
    },
    props: {
        initUser: {
            type: Object,
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
            user_id: this.initUser.id,
            state: window.State,
            submitting: false,
            form: new Form({
                username: this.initUser.username,
                first_name: this.initUser.first_name,
                last_name: this.initUser.last_name,
                email: this.initUser.email,
                password: '',
                password_confirm: '',
                user_roles: this.initUserRoles
            })
        }
    },
    computed: {
        endpoint () {
            return `/users/${this.user_id}`
        },
        isAdmin () {
            return this.state.user.is_admin
        },
        rolesErrors () {
            return _.has(this.form.errors.roles)
                ? this.form.errors.roles
                : []
        }
    },
    created () {
        Event.listen('updateUserRoles', (userRoles) => this.updateUserRoles(userRoles))
    },
    methods: {
        onSubmit () {
            this.submitting = true
            this.form.patch(this.endpoint)
                .then((response) => {
                    flash('Your account has been updated.')
                    this.resetForm(response)
                    this.submitting = false
                })
                .catch((errors) => {
                    flash('Failed to update account.', 'danger')
                    this.submitting = false
                })
        },
        resetForm (response) {
            this.form.username = response.user.username
            this.form.email = response.user.email
            this.form.first_name = response.user.first_name
            this.form.last_name = response.user.last_name
        },
        updateUserRoles (userRoles) {
            this.form.userRoles = userRoles
        }
    }
}
</script>
