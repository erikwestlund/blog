<template>
    <div class="flex mt-8">
        <form class="w-full max-w-md"
              method="POST"
              action="/users/reset-password"
              @submit.prevent="onSubmit"
              @keydown="form.errors.clear($event.target.name)"
        >
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
            <div class="flex flex-wrap mb-6">
                <button class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                        :disabled="form.errors.any() || submitting"
                >
                    Get Confirmation Link
                </button>
            </div>
        </form>
    </div>
</template>

<script>
    import Form from '../../modules/Form.js'

    export default {
        name: "ResetPasswordRequest",
        data() {
            return {
                submitting: false,
                form: new Form({
                    email: '',
                })
            }
        },
        methods: {
            onSubmit() {
                this.submitting = true;
                this.form.post('/users/reset-password')
                    .then((response) => {
                        flash('Sending password reset link...')

                        setTimeout(() => {
                            window.location.replace('/');
                        }, 500);

                        this.submitting = false;
                    })
                    .catch((errors) => {
                        flash('Could not send reset password link.', 'danger')
                        this.submitting = false;
                    });
            },
        }
    }
</script>

<style scoped>

</style>