<template>
    <div class="flex mt-8">
        <form
            class="w-full max-w-md"
            method="POST"
            action="/register"
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
            <div class="flex flex-wrap mb-6">
                <button
                    class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                    :disabled="form.errors.any() || submitting"
                >
                    Sign Up
                </button>
            </div>
        </form>
    </div>
</template>x

<script>
import Form from '../../modules/Form.js'

export default {
    name: 'RegisterUser',
    data () {
        return {
            submitting: false,
            form: new Form({
                username: '',
                first_name: '',
                last_name: '',
                email: '',
                password: '',
                password_confirm: ''
            })
        }
    },
    methods: {
        onSubmit () {
            this.submitting = true
            this.form.post('/register')
                .then((response) => {
                    flash('Signing you up...')

                    setTimeout(() => {
                        window.location.replace('/')
                    }, 500)

                    this.submitting = false
                })
                .catch((errors) => {
                    flash('User registration failed.', 'danger')
                    this.submitting = false
                })
        }
    }
}
</script>
