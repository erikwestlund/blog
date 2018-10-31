require('./bootstrap');

window.Vue = require('vue');

require ('./font-awesome')

import Event from './modules/Event';
window.Event = new Event;

window.flash = function (message, level = 'success', timeout = 3) {
    window.Event.fire('flash', {message, level, timeout});
};

import Alert from './components/ui/Alert'
import Flash from './components/ui/Flash'
import NavigationBar from './components/ui/NavigationBar'
import LoginUser from './components/users/LoginUser'
import RegisterUser from './components/users/RegisterUser'

const app = new Vue({
    el: '#app',
    components: {
        // ui
        'alert': Alert,
        'flash': Flash,
        'navigation-bar': NavigationBar,
        // users
        'login-user': LoginUser,
        'register-user': RegisterUser,
    }
});