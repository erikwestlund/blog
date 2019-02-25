import { library } from '@fortawesome/fontawesome-svg-core'

import { faAngleDoubleLeft } from '@fortawesome/pro-regular-svg-icons'
import { faAngleDoubleRight } from '@fortawesome/pro-regular-svg-icons'
import { faCircleNotch } from '@fortawesome/pro-regular-svg-icons'
import { faEllipsisH } from '@fortawesome/pro-regular-svg-icons'
import { faEdit } from '@fortawesome/pro-regular-svg-icons'
import { faExclamationCircle } from '@fortawesome/pro-regular-svg-icons'
import { faEye } from '@fortawesome/pro-regular-svg-icons'
import { faEyeSlash } from '@fortawesome/pro-regular-svg-icons'
import { faKey } from '@fortawesome/pro-regular-svg-icons'
import { faLock } from '@fortawesome/pro-regular-svg-icons'
import { faPencil } from '@fortawesome/pro-regular-svg-icons'
import { faPlusCircle } from '@fortawesome/pro-regular-svg-icons'
import { faSave } from '@fortawesome/pro-regular-svg-icons'
import { faSignIn } from '@fortawesome/pro-regular-svg-icons'
import { faSignOut } from '@fortawesome/pro-regular-svg-icons'
import { faTimes } from '@fortawesome/pro-regular-svg-icons'
import { faUser } from '@fortawesome/pro-regular-svg-icons'
import { faUserPlus } from '@fortawesome/pro-regular-svg-icons'

library.add(
  faAngleDoubleLeft,
  faAngleDoubleRight,
  faCircleNotch,
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

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

Vue.component('fa-icon', FontAwesomeIcon);
