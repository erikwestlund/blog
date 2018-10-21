require('./bootstrap');

window.Vue = require('vue');

import RegisterUser from './components/users/RegisterUser'

const app = new Vue({
    el: '#app',
    components: {
        'register-user': RegisterUser,
    }
});