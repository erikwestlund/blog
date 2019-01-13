<template>
  <alert
    important
    :temporary="false"
  >
    <div v-if="emailSent">
      An email has been sent with directions to verify your account. Thank you.
    </div>
    <div v-else>
      You have not verified you own the email address associated with this account.

      <a
        class="text-blue-dark hover:text-blue-darker cursor-pointer"
        @click="sendVerificationEmail()"
      >
        Click here to receive a confirmation email.
      </a>
    </div>
  </alert>
</template>

<script>
import Alert from '../ui/Alert'

export default {
  name: 'ConfirmEmailAlert',
  components: {
    'alert': Alert
  },
  data () {
    return {
      emailSent: false
    }
  },
  methods: {
    sendVerificationEmail () {
      axios.post('/users/confirm-email')
        .then(response => {
          flash('Email sent.')
          this.emailSent = true
        })
        .catch(errors => {
          flash('Could not send verification email.')
        })
    }
  }
}
</script>

<style scoped>

</style>
