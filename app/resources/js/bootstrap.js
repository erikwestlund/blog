window._ = require('lodash')
window.axios = require('axios')

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

const token = document.head.querySelector('meta[name="csrf-token"]')

if (token) {
    window.axios.defaults.headers.common['X-CSRF-TOKEN'] = token.content
} else {
    console.error('CSRF token not found.')
}

/* eslint-disable no-extend-native */
String.prototype.capitalize = function () {
    return this.charAt(0).toUpperCase() + this.slice(1)
}
/* eslint-enable no-extend-native */
