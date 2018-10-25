require('./bootstrap');

window.Vue = require('vue');

import Event from './modules/Event';
window.Event = new Event;

window.flash = function (message, level = 'success', timeout = 3) {
    window.Event.fire('flash', {message, level, timeout});
};

import Flash from './components/ui/Flash'
import RegisterUser from './components/users/RegisterUser'

const app = new Vue({
    el: '#app',
    components: {
        'register-user': RegisterUser,
        'flash': Flash,
    }
});