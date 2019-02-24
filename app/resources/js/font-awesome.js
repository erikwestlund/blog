import fontawesome from '@fortawesome/fontawesome'

import faAngleDoubleLeft from '@fortawesome/fontawesome-pro-regular/faAngleDoubleLeft'
import faAngleDoubleRight from '@fortawesome/fontawesome-pro-regular/faAngleDoubleRight'
import faEllipsisH from '@fortawesome/fontawesome-pro-regular/faEllipsisH'
import faEdit from '@fortawesome/fontawesome-pro-regular/faEdit'
import faExclamationCircle from '@fortawesome/fontawesome-pro-regular/faExclamationCircle'
import faEye from '@fortawesome/fontawesome-pro-regular/faEye'
import faEyeSlash from '@fortawesome/fontawesome-pro-regular/faEyeSlash'
import faKey from '@fortawesome/fontawesome-pro-regular/faKey'
import faLock from '@fortawesome/fontawesome-pro-regular/faLock'
import faPencil from '@fortawesome/fontawesome-pro-regular/faPencil'
import faPlusCircle from '@fortawesome/fontawesome-pro-regular/faPlusCircle'
import faSave from '@fortawesome/fontawesome-pro-regular/faSave'
import faSignIn from '@fortawesome/fontawesome-pro-regular/faSignIn'
import faSignOut from '@fortawesome/fontawesome-pro-regular/faSignOut'
import faTimes from '@fortawesome/fontawesome-pro-regular/faTimes'
import faUser from '@fortawesome/fontawesome-pro-regular/faUser'
import faUserPlus from '@fortawesome/fontawesome-pro-regular/faUserPlus'

import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

fontawesome.library.add(
  faAngleDoubleLeft,
  faAngleDoubleRight,
  faEllipsisH,
  faEdit,
  faExclamationCircle,
  faEye,
  faEyeSlash,
  faKey,
  faLock,
  faPencil,
  faPlusCircle,
  faSave,
  faSignIn,
  faSignOut,
  faTimes,
  faUser,
  faUserPlus
)

Vue.component('fa-icon', FontAwesomeIcon)
