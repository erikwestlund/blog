<template>
    <div class="flex mt-8">
        <form
            class="w-full max-w-md"
            method="POST"
            :action="endpoint"
            @submit.prevent="onSubmit"
            @keydown="form.errors.clear($event.target.name)"
        >
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full px-3">
                    <label
                        class="text-input-label"
                        :class="{'text-red' : form.errors.has('password') || form.errors.has('password_confirm')}"
                        for="grid-password"
                    >
                        New Password
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

                    <p
                        v-if="form.errors.has('token')"
                        class="text-red text-xs italic"
                        v-text="form.errors.get('token')"
                    />
                </div>
            </div>
            <div class="flex flex-wrap mb-6">
                <button
                    class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                    :disabled="form.errors.any() || submitting"
                >
                    Reset Password
                </button>
            </div>
        </form>
    </div>
</template>

<script>
import Form from '../../modules/Form.js'

export default {
    name: 'ResetPassword',
    props: {
        token: {
            type: String,
            required: true
        }
    },
    data () {
        return {
            submitting: false,
            form: new Form({
                password: '',
                password_confirm: ''
            })
        }
    },
    computed: {
        endpoint () {
            return `/users/reset-password/${this.token}`
        }
    },
    methods: {
        onSubmit () {
            this.submitting = true
            this.form.post(this.endpoint)
                .then((response) => {
                    flash('Resetting password...')

                    setTimeout(() => {
                        window.location.replace('/')
                    }, 500)

                    this.submitting = false
                })
                .catch((errors) => {
                    flash('Could not reset password.', 'danger')
                    this.submitting = false
                })
        }
    }
}
</script>

<style scoped>

</style>
