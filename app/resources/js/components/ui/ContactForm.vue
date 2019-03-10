<template>
    <div class="flex mt-8">
        <form
            class="w-full max-w-md"
            method="POST"
            action="/contact/email"
            @submit.prevent="onSubmit"
            @keydown="form.errors.clear()"
        >
            <div class="flex flex-wrap -mx-3 mb-3">
                <div class="w-full px-3">
                    <label
                        class="text-input-label"
                        :class="{'text-red' : form.errors.has('name')}"
                        for="grid-contact-name"
                    >
                        Name
                    </label>
                    <input
                        id="grid-contact-name"
                        v-model="form.name"
                        class="text-input focus:outline-none focus:border-grey"
                        name="name"
                        :class="{'border border-red' : form.errors.has('name')}"
                        placeholder="Name"
                    >
                    <p
                        v-if="form.errors.has('name')"
                        class="text-red text-xs italic"
                        v-text="form.errors.get('name')"
                    />
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-3">
                <div class="w-full px-3">
                    <label
                        class="text-input-label"
                        :class="{'text-red' : form.errors.has('email')}"
                        for="grid-contact-email"
                    >
                        Email
                    </label>
                    <input
                        id="grid-contact-email"
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
            </div><div class="flex flex-wrap -mx-3 mb-3">
                <div class="w-full px-3">
                    <label
                        class="text-input-label"
                        :class="{'text-red' : form.errors.has('body')}"
                        for="grid-contact-body"
                    >
                        Body
                    </label>
                    <textarea
                        id="grid-contact-body"
                        v-model="form.body"
                        class="text-input focus:outline-none focus:border-grey"
                        :class="{'border border-red' : form.errors.has('body')}"
                        name="body"
                        rows="20"
                        placeholder="Your message."
                    />
                    <p
                        v-if="form.errors.has('body')"
                        class="text-red text-xs italic"
                        v-text="form.errors.get('body')"
                    />
                </div>
            </div>

            <div class="flex flex-wrap mb-6">
                <button
                    class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                    :disabled="form.errors.any() || sending"
                >
                    <submitting-label
                        v-if="sending"
                        type="sending"
                    />
                    <span v-else>
                        <fa-icon
                            class="mr-2"
                            :icon="['far', 'envelope']"
                        />
                        Send It
                    </span>
                </button>
            </div>
        </form>
    </div>
</template>x

<script>
import Form from '../../modules/Form.js'
import Submitting from '../mixins/SubmittingMixin'

export default {
    name: 'RegisterUser',
    mixins: [ Submitting ],
    data () {
        return {
            form: new Form({
                name: '',
                email: '',
                body: ''
            })
        }
    },
    methods: {
        onSubmit () {
            this.sending = true
            this.form.post('/contact')
                .then((response) => {
                    flash('Sending your message...')

                    this.turnOffSubmitting()

                    setTimeout(() => {
                        window.location.replace('/')
                    }, 500)
                })
                .catch((errors) => {
                    this.sending = false
                    flash('Could not send email', 'danger')
                })
        }
    }
}
</script>
