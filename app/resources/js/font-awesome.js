import { library } from '@fortawesome/fontawesome-svg-core'

import {
    faAngleDoubleLeft,
    faAngleDoubleRight,
    faCircleNotch,
    faEllipsisH,
    faEdit,
    faExclamationCircle,
    faEye,
    faEyeSlash,
    faFileEdit,
    faKey,
    faLock,
    faPencil,
    faPlusCircle,
    faSave,
    faSignIn,
    faSignOut,
    faTimes,
    faTrash,
    faUser,
    faUserPlus
} from '@fortawesome/pro-regular-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(
    faAngleDoubleLeft,
    faAngleDoubleRight,
    faCircleNotch,
    faEllipsisH,
    faEdit,
    faExclamationCircle,
    faEye,
    faEyeSlash,
    faFileEdit,
    faKey,
    faLock,
    faPencil,
    faPlusCircle,
    faSave,
    faSignIn,
    faSignOut,
    faTimes,
    faTrash,
    faUser,
    faUserPlus
)

Vue.component('fa-icon', FontAwesomeIcon)
