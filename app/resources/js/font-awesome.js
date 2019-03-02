import { library } from '@fortawesome/fontawesome-svg-core'

import {
    faAngleDoubleLeft,
    faAngleDoubleRight,
    faAsterisk,
    faCircleNotch,
    faEdit,
    faEllipsisH,
    faEnvelope,
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
    faTag,
    faTags,
    faTimes,
    faTrash,
    faUniversity,
    faUser,
    faUserCircle,
    faUserEdit,
    faUserPlus
} from '@fortawesome/pro-regular-svg-icons'

import { faUserCircle as fasUserCircle, faEnvelope as fasEnvelope, faUniversity as fasUniversity } from '@fortawesome/pro-solid-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons'

library.add(
    faAngleDoubleLeft,
    faAngleDoubleRight,
    faAsterisk,
    faCircleNotch,
    faEdit,
    faEllipsisH,
    faEnvelope,
    fasEnvelope,
    faExclamationCircle,
    faEye,
    faEyeSlash,
    faGithub,
    faFileEdit,
    faKey,
    faLock,
    faPencil,
    faPlusCircle,
    faSave,
    faSignIn,
    faSignOut,
    faTag,
    faTags,
    faTimes,
    faTrash,
    faTwitter,
    faUser,
    faUserCircle,
    fasUserCircle,
    faUserEdit,
    faUserPlus,
    faUniversity,
    fasUniversity
)

Vue.component('fa-icon', FontAwesomeIcon)
