import fontawesome from '@fortawesome/fontawesome'

import faUser from '@fortawesome/fontawesome-pro-regular/faUser';
import faTimes from '@fortawesome/fontawesome-pro-regular/faTimes';

fontawesome.library.add(
    faUser,
    faTimes,
)

import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
Vue.component('fa-icon', FontAwesomeIcon);