require('./bootstrap');

window.Vue = require('vue');

require('./font-awesome')

import Event from './modules/Event';

window.Event = new Event;

window.flash = function (message, level = 'success', timeout = 3) {
    window.Event.fire('flash', {message, level, timeout});
};

import Alert from './components/ui/Alert'
import Flash from './components/ui/Flash'
import NavigationBar from './components/ui/NavigationBar'
import Paginate from './components/ui/Paginate'
import ConfirmEmailAlert from './components/users/ConfirmEmailAlert'
import CreatePost from './components/posts/CreatePost'
import EditUser from './components/users/EditUser'
import LoginUser from './components/users/LoginUser'
import RegisterUser from './components/users/RegisterUser'
import ResetPassword from './components/users/ResetPassword'
import ResetPasswordRequest from './components/users/ResetPasswordRequest'
import UsersAdminPanel from './components/users/UsersAdminPanel'

const app = new Vue({
    el: '#app',
    components: {
        // ui
        'alert': Alert,
        'flash': Flash,
        'navigation-bar': NavigationBar,
        'paginate': Paginate,
        //posts
        'create-post': CreatePost,
        // users
        'confirm-email-alert': ConfirmEmailAlert,
        'edit-user': EditUser,
        'login-user': LoginUser,
        'register-user': RegisterUser,
        'reset-password': ResetPassword,
        'reset-password-request': ResetPasswordRequest,
        'users-admin-panel': UsersAdminPanel,
    }
});