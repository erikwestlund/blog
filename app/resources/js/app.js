import Event from './modules/Event'

import Alert from './components/ui/Alert'
import ContactForm from './components/ui/ContactForm'
import Flash from './components/ui/Flash'
import NavigationBar from './components/ui/NavigationBar'
import Paginate from './components/ui/Paginate'
import ConfirmEmailAlert from './components/users/ConfirmEmailAlert'
import Post from './components/posts/Post'
import Posts from './components/posts/Posts'
import PostForm from './components/posts/PostForm'
import PostsAdminPanel from './components/posts/PostsAdminPanel'
import PageForm from './components/pages/PageForm'
import PagesAdminPanel from './components/pages/PagesAdminPanel'
import EditUser from './components/users/EditUser'
import LoginUser from './components/users/LoginUser'
import RegisterUser from './components/users/RegisterUser'
import ResetPassword from './components/users/ResetPassword'
import ResetPasswordRequest from './components/users/ResetPasswordRequest'
import UsersAdminPanel from './components/users/UsersAdminPanel'
import VueClipboard from 'vue-clipboard2'

require('./bootstrap')

window.Vue = require('vue')

require('./font-awesome')

Vue.use(VueClipboard)
window.Event = new Event()

window.flash = function (message, level = 'success', timeout = 3) {
    window.Event.fire('flash', { message, level, timeout })
}

/* eslint no-unused-vars: "off" */
const app = new Vue({
    el: '#app',
    components: {
        // ui
        Alert,
        ContactForm,
        Flash,
        NavigationBar,
        Paginate,
        // posts
        Posts,
        PostForm,
        PostsAdminPanel,
        // pages
        PageForm,
        PagesAdminPanel,
        // users
        ConfirmEmailAlert,
        EditUser,
        LoginUser,
        Post,
        RegisterUser,
        ResetPassword,
        ResetPasswordRequest,
        UsersAdminPanel
    }
})
