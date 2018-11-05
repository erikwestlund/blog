import fontawesome from '@fortawesome/fontawesome'

import faExclamationCircle from '@fortawesome/fontawesome-pro-regular/faExclamationCircle';
import faKey from '@fortawesome/fontawesome-pro-regular/faKey';
import faTimes from '@fortawesome/fontawesome-pro-regular/faTimes';
import faSignIn from '@fortawesome/fontawesome-pro-regular/faSignIn';
import faSignOut from '@fortawesome/fontawesome-pro-regular/faSignOut';
import faUser from '@fortawesome/fontawesome-pro-regular/faUser';
import faUserPlus from '@fortawesome/fontawesome-pro-regular/faUserPlus';

fontawesome.library.add(
    faExclamationCircle,
    faKey,
    faSignIn,
    faSignOut,
    faTimes,
    faUser,
    faUserPlus,
)

import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

Vue.component('fa-icon', FontAwesomeIcon);