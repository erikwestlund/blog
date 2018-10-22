webpackJsonp([1],{

/***/ 12:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(13);
module.exports = __webpack_require__(42);


/***/ }),

/***/ 13:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_users_RegisterUser__ = __webpack_require__(36);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_users_RegisterUser___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__components_users_RegisterUser__);
__webpack_require__(14);

window.Vue = __webpack_require__(11);



var app = new Vue({
    el: '#app',
    components: {
        'register-user': __WEBPACK_IMPORTED_MODULE_0__components_users_RegisterUser___default.a
    }
});

/***/ }),

/***/ 14:
/***/ (function(module, exports, __webpack_require__) {

window._ = __webpack_require__(3);
window.axios = __webpack_require__(4);

var token = document.head.querySelector('meta[name="csrf-token"]');

if (token) {
    window.axios.defaults.headers.common['X-CSRF-TOKEN'] = token.content;
} else {
    console.error('CSRF token not found.');
}

/***/ }),

/***/ 36:
/***/ (function(module, exports, __webpack_require__) {

var disposed = false
var normalizeComponent = __webpack_require__(37)
/* script */
var __vue_script__ = __webpack_require__(38)
/* template */
var __vue_template__ = __webpack_require__(41)
/* template functional */
var __vue_template_functional__ = false
/* styles */
var __vue_styles__ = null
/* scopeId */
var __vue_scopeId__ = null
/* moduleIdentifier (server only) */
var __vue_module_identifier__ = null
var Component = normalizeComponent(
  __vue_script__,
  __vue_template__,
  __vue_template_functional__,
  __vue_styles__,
  __vue_scopeId__,
  __vue_module_identifier__
)
Component.options.__file = "resources/js/components/users/RegisterUser.vue"

/* hot reload */
if (false) {(function () {
  var hotAPI = require("vue-hot-reload-api")
  hotAPI.install(require("vue"), false)
  if (!hotAPI.compatible) return
  module.hot.accept()
  if (!module.hot.data) {
    hotAPI.createRecord("data-v-4936d4e0", Component.options)
  } else {
    hotAPI.reload("data-v-4936d4e0", Component.options)
  }
  module.hot.dispose(function (data) {
    disposed = true
  })
})()}

module.exports = Component.exports


/***/ }),

/***/ 37:
/***/ (function(module, exports) {

/* globals __VUE_SSR_CONTEXT__ */

// IMPORTANT: Do NOT use ES2015 features in this file.
// This module is a runtime utility for cleaner component module output and will
// be included in the final webpack user bundle.

module.exports = function normalizeComponent (
  rawScriptExports,
  compiledTemplate,
  functionalTemplate,
  injectStyles,
  scopeId,
  moduleIdentifier /* server only */
) {
  var esModule
  var scriptExports = rawScriptExports = rawScriptExports || {}

  // ES6 modules interop
  var type = typeof rawScriptExports.default
  if (type === 'object' || type === 'function') {
    esModule = rawScriptExports
    scriptExports = rawScriptExports.default
  }

  // Vue.extend constructor export interop
  var options = typeof scriptExports === 'function'
    ? scriptExports.options
    : scriptExports

  // render functions
  if (compiledTemplate) {
    options.render = compiledTemplate.render
    options.staticRenderFns = compiledTemplate.staticRenderFns
    options._compiled = true
  }

  // functional template
  if (functionalTemplate) {
    options.functional = true
  }

  // scopedId
  if (scopeId) {
    options._scopeId = scopeId
  }

  var hook
  if (moduleIdentifier) { // server build
    hook = function (context) {
      // 2.3 injection
      context =
        context || // cached call
        (this.$vnode && this.$vnode.ssrContext) || // stateful
        (this.parent && this.parent.$vnode && this.parent.$vnode.ssrContext) // functional
      // 2.2 with runInNewContext: true
      if (!context && typeof __VUE_SSR_CONTEXT__ !== 'undefined') {
        context = __VUE_SSR_CONTEXT__
      }
      // inject component styles
      if (injectStyles) {
        injectStyles.call(this, context)
      }
      // register component module identifier for async chunk inferrence
      if (context && context._registeredComponents) {
        context._registeredComponents.add(moduleIdentifier)
      }
    }
    // used by ssr in case component is cached and beforeCreate
    // never gets called
    options._ssrRegister = hook
  } else if (injectStyles) {
    hook = injectStyles
  }

  if (hook) {
    var functional = options.functional
    var existing = functional
      ? options.render
      : options.beforeCreate

    if (!functional) {
      // inject component registration as beforeCreate hook
      options.beforeCreate = existing
        ? [].concat(existing, hook)
        : [hook]
    } else {
      // for template-only hot-reload because in that case the render fn doesn't
      // go through the normalizer
      options._injectStyles = hook
      // register for functioal component in vue file
      options.render = function renderWithStyleInjection (h, context) {
        hook.call(context)
        return existing(h, context)
      }
    }
  }

  return {
    esModule: esModule,
    exports: scriptExports,
    options: options
  }
}


/***/ }),

/***/ 38:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__modules_Form_js__ = __webpack_require__(39);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//



/* harmony default export */ __webpack_exports__["default"] = ({
    mounted: function mounted() {
        console.log('Component mounted.');
    },
    data: function data() {
        return {
            form: new __WEBPACK_IMPORTED_MODULE_0__modules_Form_js__["a" /* default */]({
                username: '',
                first_name: '',
                last_name: '',
                email: '',
                password: '',
                password_confirm: ''
            })
        };
    },

    methods: {
        onSubmit: function onSubmit() {
            this.form.post('/register').then(function (response) {
                console.log(response);
            }).catch(function (errors) {
                console.log(errors);
            });
        }
    }
});

/***/ }),

/***/ 39:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__Errors_js__ = __webpack_require__(40);
var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }



var Form = function () {
    /**
     * Create a new Form instance.
     *
     * @param {object} data
     */
    function Form(data) {
        var isUpdateForm = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : false;

        _classCallCheck(this, Form);

        this.originalData = _.cloneDeep(data);

        for (var field in data) {
            this[field] = data[field];
        }

        this.formType = isUpdateForm ? 'update' : 'create';
        this.errors = new __WEBPACK_IMPORTED_MODULE_0__Errors_js__["a" /* default */]();
    }

    /**
     * Fetch all relevant data for the form.
     */


    _createClass(Form, [{
        key: 'data',
        value: function data() {
            var data = {};

            for (var property in this.originalData) {
                data[property] = this[property];
            }

            return data;
        }

        /**
         * Reset the form fields.
         */

    }, {
        key: 'reset',
        value: function reset() {
            var force_reset = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : false;

            if (this.formType == 'create') {
                for (var field in this.originalData) {
                    this[field] = this.originalData[field];
                }
            }

            this.errors.clear();
        }

        /**
         * Send a POST request to the given URL.
         * .
         * @param {string} url
         */

    }, {
        key: 'post',
        value: function post(url) {
            return this.submit('post', url);
        }

        /**
         * Send a PUT request to the given URL.
         * .
         * @param {string} url
         */

    }, {
        key: 'put',
        value: function put(url) {
            return this.submit('put', url);
        }

        /**
         * Send a PATCH request to the given URL.
         * .
         * @param {string} url
         */

    }, {
        key: 'patch',
        value: function patch(url) {
            return this.submit('patch', url);
        }

        /**
         * Send a DELETE request to the given URL.
         * .
         * @param {string} url
         */

    }, {
        key: 'delete',
        value: function _delete(url) {
            return this.submit('delete', url);
        }

        /**
         * Submit the form.
         *
         * @param {string} requestType
         * @param {string} url
         */

    }, {
        key: 'submit',
        value: function submit(requestType, url) {
            var _this = this;

            return new Promise(function (resolve, reject) {
                axios[requestType](url, _this.data()).then(function (response) {
                    _this.onSuccess(response.data);

                    resolve(response.data);
                }).catch(function (error) {
                    _this.onFail(error.response.data);
                    reject(error.response);
                });
            });
        }

        /**
         * Handle a successful form submission.
         *
         * @param {object} data
         */

    }, {
        key: 'onSuccess',
        value: function onSuccess(data) {
            this.reset();
        }

        /**
         * Handle a failed form submission.
         *
         * Only record if an error bag is returned. This allows us to defer
         * to the caller to handle things like authorization errors.
         *
         * @param {object} errors
         */

    }, {
        key: 'onFail',
        value: function onFail(errors) {
            if (errors.hasOwnProperty('errors')) {
                this.errors.record(errors.errors);
            }
        }
    }]);

    return Form;
}();

/* harmony default export */ __webpack_exports__["a"] = (Form);

/***/ }),

/***/ 40:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Errors = function () {
    /**
     * Create a new Errors instance.
     */
    function Errors() {
        _classCallCheck(this, Errors);

        this.errors = {};
    }

    /**
     * Determine if an errors exists for the given field.
     *
     * @param {string} field
     */


    _createClass(Errors, [{
        key: "has",
        value: function has(field) {
            return this.errors.hasOwnProperty(field);
        }

        /**
         * Determine if we have any errors.
         */

    }, {
        key: "any",
        value: function any() {
            return Object.keys(this.errors).length > 0;
        }

        /**
         * The number of errors.
         *
         * @returns {Number}
         */

    }, {
        key: "count",
        value: function count() {
            return Object.keys(this.errors).length;
        }

        /**
         * Retrieve the error message for a field.
         *
         * @param {string} field
         */

    }, {
        key: "get",
        value: function get(field) {
            if (this.errors[field]) {
                return this.errors[field][0];
            }
        }

        /**
         * Record the new errors.
         *
         * @param {object} errors
         */

    }, {
        key: "record",
        value: function record(errors) {
            this.errors = errors;
        }

        /**
         * Clear one or all error fields.
         *
         * @param {string|null} field
         */

    }, {
        key: "clear",
        value: function clear(field) {
            if (field) {
                delete this.errors[field];

                return;
            }

            this.errors = {};
        }
    }]);

    return Errors;
}();

/* harmony default export */ __webpack_exports__["a"] = (Errors);

/***/ }),

/***/ 41:
/***/ (function(module, exports, __webpack_require__) {

var render = function() {
  var _vm = this
  var _h = _vm.$createElement
  var _c = _vm._self._c || _h
  return _c("div", { staticClass: "flex mt-8" }, [
    _c(
      "form",
      {
        staticClass: "w-full max-w-md",
        attrs: { method: "POST", action: "/register" },
        on: {
          submit: function($event) {
            $event.preventDefault()
            return _vm.onSubmit($event)
          },
          keydown: function($event) {
            _vm.form.errors.clear($event.target.name)
          }
        }
      },
      [
        _c("div", { staticClass: "flex flex-wrap -mx-3 mb-6" }, [
          _c("div", { staticClass: "w-full px-3" }, [
            _c(
              "label",
              {
                staticClass:
                  "block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",
                class: { "text-red": _vm.form.errors.has("username") },
                attrs: { for: "grid-username" }
              },
              [_vm._v("\n                    Username\n                ")]
            ),
            _vm._v(" "),
            _c("input", {
              directives: [
                {
                  name: "model",
                  rawName: "v-model",
                  value: _vm.form.username,
                  expression: "form.username"
                }
              ],
              staticClass:
                "appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey",
              class: { "border border-red": _vm.form.errors.has("username") },
              attrs: {
                id: "grid-username",
                type: "password",
                placeholder: "Username"
              },
              domProps: { value: _vm.form.username },
              on: {
                input: function($event) {
                  if ($event.target.composing) {
                    return
                  }
                  _vm.$set(_vm.form, "username", $event.target.value)
                }
              }
            }),
            _vm._v(" "),
            _vm.form.errors.has("username")
              ? _c("p", {
                  staticClass: "text-red text-xs italic",
                  domProps: {
                    textContent: _vm._s(_vm.form.errors.get("username"))
                  }
                })
              : _vm._e()
          ])
        ]),
        _vm._v(" "),
        _c("div", { staticClass: "flex flex-wrap -mx-3 mb-6" }, [
          _c("div", { staticClass: "w-full md:w-1/2 px-3 mb-6 md:mb-0" }, [
            _c(
              "label",
              {
                staticClass:
                  "block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",
                attrs: { for: "grid-first-name" }
              },
              [_vm._v("\n                    First Name\n                ")]
            ),
            _vm._v(" "),
            _c("input", {
              directives: [
                {
                  name: "model",
                  rawName: "v-model",
                  value: _vm.form.first_name,
                  expression: "form.first_name"
                }
              ],
              staticClass:
                "appearance-none block w-full bg-grey-lighter text-grey-darker border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
              attrs: {
                id: "grid-first-name",
                type: "text",
                placeholder: "Jane"
              },
              domProps: { value: _vm.form.first_name },
              on: {
                input: function($event) {
                  if ($event.target.composing) {
                    return
                  }
                  _vm.$set(_vm.form, "first_name", $event.target.value)
                }
              }
            })
          ]),
          _vm._v(" "),
          _c("div", { staticClass: "w-full md:w-1/2 px-3" }, [
            _c(
              "label",
              {
                staticClass:
                  "block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",
                attrs: { for: "grid-last-name" }
              },
              [_vm._v("\n                    Last Name\n                ")]
            ),
            _vm._v(" "),
            _c("input", {
              directives: [
                {
                  name: "model",
                  rawName: "v-model",
                  value: _vm.form.last_name,
                  expression: "form.last_name"
                }
              ],
              staticClass:
                "appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-grey",
              attrs: { id: "grid-last-name", type: "text", placeholder: "Doe" },
              domProps: { value: _vm.form.last_name },
              on: {
                input: function($event) {
                  if ($event.target.composing) {
                    return
                  }
                  _vm.$set(_vm.form, "last_name", $event.target.value)
                }
              }
            })
          ])
        ]),
        _vm._v(" "),
        _c("div", { staticClass: "flex flex-wrap -mx-3 mb-6" }, [
          _c("div", { staticClass: "w-full px-3" }, [
            _c(
              "label",
              {
                staticClass:
                  "block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",
                class: { "text-red": _vm.form.errors.has("email") },
                attrs: { for: "grid-email" }
              },
              [_vm._v("\n                    Email\n                ")]
            ),
            _vm._v(" "),
            _c("input", {
              directives: [
                {
                  name: "model",
                  rawName: "v-model",
                  value: _vm.form.email,
                  expression: "form.email"
                }
              ],
              staticClass:
                "appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey",
              class: { "border border-red": _vm.form.errors.has("email") },
              attrs: { id: "grid-email", placeholder: "name@domain.com" },
              domProps: { value: _vm.form.email },
              on: {
                input: function($event) {
                  if ($event.target.composing) {
                    return
                  }
                  _vm.$set(_vm.form, "email", $event.target.value)
                }
              }
            }),
            _vm._v(" "),
            _vm.form.errors.has("email")
              ? _c("p", {
                  staticClass: "text-red text-xs italic",
                  domProps: {
                    textContent: _vm._s(_vm.form.errors.get("email"))
                  }
                })
              : _vm._e()
          ])
        ]),
        _vm._v(" "),
        _c("div", { staticClass: "flex flex-wrap -mx-3 mb-6" }, [
          _c("div", { staticClass: "w-full px-3" }, [
            _c(
              "label",
              {
                staticClass:
                  "block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",
                class: {
                  "text-red":
                    _vm.form.errors.has("password") ||
                    _vm.form.errors.has("password_confirm")
                },
                attrs: { for: "grid-password" }
              },
              [_vm._v("\n                    Password\n                ")]
            ),
            _vm._v(" "),
            _c("input", {
              directives: [
                {
                  name: "model",
                  rawName: "v-model",
                  value: _vm.form.password,
                  expression: "form.password"
                }
              ],
              staticClass:
                "appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey",
              class: { "border border-red": _vm.form.errors.has("password") },
              attrs: {
                id: "grid-password",
                type: "password",
                placeholder: "Password"
              },
              domProps: { value: _vm.form.password },
              on: {
                input: function($event) {
                  if ($event.target.composing) {
                    return
                  }
                  _vm.$set(_vm.form, "password", $event.target.value)
                }
              }
            }),
            _vm._v(" "),
            _vm.form.errors.has("password")
              ? _c("p", {
                  staticClass: "text-red text-xs italic mb-4",
                  domProps: {
                    textContent: _vm._s(_vm.form.errors.get("password"))
                  }
                })
              : _vm._e(),
            _vm._v(" "),
            _c("input", {
              directives: [
                {
                  name: "model",
                  rawName: "v-model",
                  value: _vm.form.password_confirm,
                  expression: "form.password_confirm"
                }
              ],
              staticClass:
                "appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey",
              class: {
                "border border-red": _vm.form.errors.has("password_confirm")
              },
              attrs: {
                id: "grid-password-confirm",
                type: "password",
                placeholder: "Confirm password"
              },
              domProps: { value: _vm.form.password_confirm },
              on: {
                input: function($event) {
                  if ($event.target.composing) {
                    return
                  }
                  _vm.$set(_vm.form, "password_confirm", $event.target.value)
                }
              }
            }),
            _vm._v(" "),
            _vm.form.errors.has("password_confirm")
              ? _c("p", {
                  staticClass: "text-red text-xs italic",
                  domProps: {
                    textContent: _vm._s(_vm.form.errors.get("password_confirm"))
                  }
                })
              : _vm._e()
          ])
        ]),
        _vm._v(" "),
        _vm._m(0)
      ]
    )
  ])
}
var staticRenderFns = [
  function() {
    var _vm = this
    var _h = _vm.$createElement
    var _c = _vm._self._c || _h
    return _c("div", { staticClass: "flex flex-wrap mb-6" }, [
      _c(
        "button",
        {
          staticClass:
            "flex-no-shrink bg-blue-darker hover:bg-blue-darkest border-blue-darker hover:border-blue-darkest text-sm border-4 text-white py-1 px-2 rounded"
        },
        [_vm._v("\n                Sign Up\n            ")]
      )
    ])
  }
]
render._withStripped = true
module.exports = { render: render, staticRenderFns: staticRenderFns }
if (false) {
  module.hot.accept()
  if (module.hot.data) {
    require("vue-hot-reload-api")      .rerender("data-v-4936d4e0", module.exports)
  }
}

/***/ }),

/***/ 42:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ })

},[12]);