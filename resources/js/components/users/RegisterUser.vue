<template>
    <div class="flex mt-8">
        <form class="w-full max-w-md"
              method="POST"
              action="/register"
              @submit.prevent="onSubmit"
              @keydown="form.errors.clear($event.target.name)"
        >
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full px-3">
                    <label class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
                           :class="{'text-red' : form.errors.has('username')}"
                           for="grid-username">
                        Username
                    </label>
                    <input class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey"
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
                    <label class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
                           for="grid-first-name">
                        First Name
                    </label>
                    <input class="appearance-none block w-full bg-grey-lighter text-grey-darker border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
                           v-model="form.first_name"
                           id="grid-first-name"
                           type="text"
                           placeholder="Jane">
                </div>
                <div class="w-full md:w-1/2 px-3">
                    <label class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
                           for="grid-last-name">
                        Last Name
                    </label>
                    <input class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-grey"
                           v-model="form.last_name"
                           id="grid-last-name"
                           type="text"
                           placeholder="Doe">
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-6">
                <div class="w-full px-3">
                    <label class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
                           :class="{'text-red' : form.errors.has('email')}"
                           for="grid-email">
                        Email
                    </label>
                    <input class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey"
                           :class="{'border border-red' : form.errors.has('email')}"
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
                    <label class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
                           :class="{'text-red' : form.errors.has('password') ||  form.errors.has('password_confirm')}"
                           for="grid-password">
                        Password
                    </label>
                    <input class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey"
                           :class="{'border border-red' : form.errors.has('password')}"
                           v-model="form.password"
                           id="grid-password"
                           type="password"
                           placeholder="Password">
                    <p class="text-red text-xs italic mb-4"
                       v-if="form.errors.has('password')"
                       v-text="form.errors.get('password')"></p>
                    <input class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey"
                           :class="{'border border-red' : form.errors.has('password_confirm')}"
                           v-model="form.password_confirm"
                           id="grid-password-confirm"
                           type="password"
                           placeholder="Confirm password">
                    <p class="text-red text-xs italic"
                       v-if="form.errors.has('password_confirm')"
                       v-text="form.errors.get('password_confirm')"></p>
                </div>
            </div>
            <div class="flex flex-wrap mb-6">
                <button class="flex-no-shrink bg-blue-darker hover:bg-blue-darkest border-blue-darker hover:border-blue-darkest text-sm border-4 text-white py-1 px-2 rounded">
                    Sign Up
                </button>
            </div>
        </form>
    </div>
</template>x

<script>
    import Form from '../../modules/Form.js'

    export default {
        data() {
            return {
                form: new Form({
                    username: '',
                    first_name: '',
                    last_name: '',
                    email: '',
                    password: '',
                    password_confirm: '',
                })
            }
        },
        methods: {
            onSubmit() {
                this.form.post('/register')
                    .then((response) => {
                        flash('User registration successful!')
                    })
                    .catch((errors) => {
                        flash('User registration failed.', 'danger')
                    });
            },
        }
    }
</script>