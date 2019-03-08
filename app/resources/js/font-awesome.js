import { library } from '@fortawesome/fontawesome-svg-core'

import {
    faAngleDoubleLeft,
    faAngleDoubleRight,
    faAsterisk,
    faCircleNotch,
    faCloudUpload,
    faCopy,
    faCut,
    faEdit,
    faEllipsisH,
    faEnvelope,
    faExclamationCircle,
    faEye,
    faEyeSlash,
    faFileEdit,
    faImages,
    faKey,
    faLink,
    faList,
    faLock,
    faPencil,
    faPlusCircle,
    faPlusSquare,
    faSave,
    faSearch,
    faSignIn,
    faSignOut,
    faTag,
    faTags,
    faTimes,
    faTrash,
    faUniversity,
    faUpload,
    faUser,
    faUserCircle,
    faUserEdit,
    faUserPlus
} from '@fortawesome/pro-regular-svg-icons'

import { faUserCircle as fasUserCircle, faEnvelope as fasEnvelope, faUniversity as fasUniversity } from '@fortawesome/pro-solid-svg-icons'

import {FontAwesomeIcon, FontAwesomeLayers} from '@fortawesome/vue-fontawesome'

import { faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons'

library.add(
    faAngleDoubleLeft,
    faAngleDoubleRight,
    faAsterisk,
    faCircleNotch,
    faCloudUpload,
    faCut,
    faCopy,
    faEdit,
    faEllipsisH,
    faEnvelope,
    fasEnvelope,
    faExclamationCircle,
    faEye,
    faEyeSlash,
    faGithub,
    faFileEdit,
    faImages,
    faKey,
    faLink,
    faList,
    faLock,
    faPencil,
    faPlusCircle,
    faPlusSquare,
    faSave,
    faSearch,
    faSignIn,
    faSignOut,
    faTag,
    faTags,
    faTimes,
    faTrash,
    faTwitter,
    faUpload,
    faUser,
    faUserCircle,
    fasUserCircle,
    faUserEdit,
    faUserPlus,
    faUniversity,
    fasUniversity
)

Vue.component('fa-icon', FontAwesomeIcon)
Vue.component('fa-layers', FontAwesomeLayers)
