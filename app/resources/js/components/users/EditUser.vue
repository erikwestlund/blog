<template>
    <div class="flex mt-8">
        <form class="w-full max-w-md"
              method="PATCH"
              :action="endpoint"
              @submit.prevent="onSubmit"
              @keydown="form.errors.clear($event.target.name)"
        >
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full px-3">
                    <label class="text-input-label"
                           :class="{'text-red' : form.errors.has('username')}"
                           for="grid-username">
                        Username
                    </label>
                    <input class="text-input focus:outline-none focus:border-grey"
                           name="username"
                           :class="{'border border-red' : form.errors.has('username')}"
                           v-model="form.username"
                           id="grid-username"
                           placeholder="Username">
                    <p class="text-red text-xs italic"
                       v-if="form.errors.has('username')"
                       v-text="form.errors.get('username')"></p>

                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                    <label class="text-input-label"
                           for="grid-first-name">
                        First Name
                    </label>
                    <input class="text-input focus:outline-none focus:border-grey"
                           name="first_name"
                           v-model="form.first_name"
                           id="grid-first-name"
                           type="text"
                           placeholder="Jane">
                </div>
                <div class="w-full md:w-1/2 px-3">
                    <label class="text-input-label"
                           for="grid-last-name">
                        Last Name
                    </label>
                    <input class="text-input focus:outline-none focus:border-grey"
                           name="last_name"
                           v-model="form.last_name"
                           id="grid-last-name"
                           type="text"
                           placeholder="Doe">
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full px-3">
                    <label class="text-input-label"
                           :class="{'text-red' : form.errors.has('email')}"
                           for="grid-email">
                        Email
                    </label>
                    <input class="text-input focus:outline-none focus:border-grey"
                           :class="{'border border-red' : form.errors.has('email')}"
                           name="email"
                           v-model="form.email"
                           id="grid-email"
                           placeholder="name@domain.com">
                    <p class="text-red text-xs italic"
                       v-if="form.errors.has('email')"
                       v-text="form.errors.get('email')"></p>
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full px-3">
                    <label class="text-input-label"
                           :class="{'text-red' : form.errors.has('password') ||  form.errors.has('password_confirm')}"
                           for="grid-password">
                        Password
                    </label>
                    <input class="text-input focus:outline-none focus:border-grey"
                           :class="{'border border-red' : form.errors.has('password')}"
                           name="password"
                           v-model="form.password"
                           id="grid-password"
                           type="password"
                           placeholder="Password">
                    <p class="text-red text-xs italic mb-4"
                       v-if="form.errors.has('password')"
                       v-text="form.errors.get('password')"></p>
                    <input class="text-input focus:outline-none focus:border-grey"
                           :class="{'border border-red' : form.errors.has('password_confirm')}"
                           name="password_confirm"
                           v-model="form.password_confirm"
                           id="grid-password-confirm"
                           type="password"
                           placeholder="Confirm password">
                    <p class="text-red text-xs italic"
                       v-if="form.errors.has('password_confirm')"
                       v-text="form.errors.get('password_confirm')"></p>
                </div>
            </div>
            <user-roles v-if="isAdmin"
                        :possible-roles="possibleRoles"
                        :init-user-roles="form.user_roles"
                        :errors="rolesErrors"
            />
            <div class="flex flex-wrap mb-6">
                <button class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                        :disabled="form.errors.any() || submitting"
                >
                    Update My Account
                </button>
            </div>
        </form>
    </div>
</template>x

<script>
    import Form from '../../modules/Form.js'
    import UserRoles from './UserRoles'

    export default {
        components: {
            'user-roles': UserRoles,
        },
        created() {
            Event.listen('updateUserRoles', (user_roles) => this.updateUserRoles(user_roles))
        },
        computed: {
            endpoint() {
              return `/users/${this.user_id}/edit`
            },
            isAdmin() {
                return this.state.user.is_admin
            },
            rolesErrors() {
                return _.has(this.form.errors.roles) ?
                    this.form.errors.roles :
                    []
            }
        },
        data() {
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
                    user_roles: this.initUserRoles,
                })
            }
        },
        methods: {
            onSubmit() {
                this.submitting = true;
                this.form.patch(this.endpoint)
                    .then((response) => {
                        flash('Your account has been updated.')
                        this.resetForm(response)
                        this.submitting = false;
                    })
                    .catch((errors) => {
                        flash('Failed to update account.', 'danger')
                        this.submitting = false;
                    });
            },
            resetForm(response) {
                this.form.username = response.user.username
                this.form.email = response.user.email
                this.form.first_name = response.user.first_name
                this.form.last_name = response.user.last_name
            },
            updateUserRoles(user_roles) {
                this.form.user_roles = user_roles
            }
        },
        props: {
            initUser: {
                type: Object,
                required: true,
            },
            initUserRoles: {
                type: Array,
                required: true,
            },
            possibleRoles: {
                type: Array,
                required: true,
            },
        }
    }
</script>