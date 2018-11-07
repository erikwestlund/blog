<template>
    <div class="flex mt-8">
        <form class="w-full max-w-md"
              method="POST"
              action="/login"
              @submit.prevent="onSubmit"
              @keydown="form.errors.clear($event.target.name)"
        >

            <div class="flex flex-wrap -mx-3 mb-3">
                <div class="w-full px-3">
                    <label class="text-input-label"
                           :class="{'text-red' : form.errors.has('email')}"
                           for="grid-email">
                        Email Address
                    </label>
                    <input class="text-input focus:outline-none focus:border-grey"
                           :class="{'border border-red' : form.errors.has('email')}"
                           name="email"
                           v-model="form.email"
                           id="grid-email"
                           placeholder="Email Address">
                    <p class="text-red text-xs italic"
                       v-if="form.errors.has('email')"
                       v-text="form.errors.get('email')"></p>
                </div>
            </div>


            <div class="flex flex-wrap -mx-3 mb-3">
                <div class="w-full px-3">
                    <label class="text-input-label"
                           :class="{'text-red' : form.errors.has('password')}"
                           for="grid-password">
                        Password
                    </label>
                    <input type="password"
                           class="text-input focus:outline-none focus:border-grey"
                           :class="{'border border-red' : form.errors.has('password')}"
                           name="password"
                           v-model="form.password"
                           id="grid-password"
                           placeholder="Password">
                    <p class="text-red text-xs italic"
                       v-if="form.errors.has('password')"
                       v-text="form.errors.get('password')"></p>
                </div>
            </div>

            <div class="flex flex-wrap mb-6">
                <label class="text-grey-dark">
                    <input class="mr-2 leading-tight" type="checkbox">
                    <span class="cursor-pointer">
                                Remember Me
                              </span>
                </label>
            </div>
            <div class="flex flex-wrap mb-3">
                <button class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                        :disabled="form.errors.any() || submitting"
                >
                    <fa-icon class="mr-2" :icon="['far', 'sign-in']"/>
                    Log In
                </button>
            </div>

        </form>
    </div>
</template>x

<script>
    import Form from '../../modules/Form.js'

    export default {
        name: "LoginUser",
        data() {
            return {
                submitting: false,
                showLoginModal: false,
                form: new Form({
                    next: this.next,
                    email: '',
                    password: '',
                })
            }
        },
        methods: {
            onSubmit() {
                this.submitting = true;
                this.form.post('/login')
                    .then((response) => {
                        Event.fire('closeLoginModal')

                        flash('Logging you in...')

                        setTimeout(() => {
                            window.location.replace(response.next);
                        }, 500);

                        this.submitting = false;
                    })
                    .catch(errors => {
                        this.submitting = false;
                    })
            },
        },
        props: {
            next: {
                type: String,
                default: null,
            }
        }
    }
</script>