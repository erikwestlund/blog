webpackJsonp([1],{"+dUj":function(e,t,r){(e.exports=r("FZ+f")(!1)).push([e.i,".alert-flash[data-v-53f42613]{position:fixed;right:25px;bottom:25px}",""])},0:function(e,t,r){r("F1kH"),e.exports=r("KqWi")},"7W6c":function(e,t,r){var n=r("VU/8")(r("8JzK"),r("kwhv"),!1,null,null,null);e.exports=n.exports},"8JzK":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=function(){function e(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}return function(t,r,n){return r&&e(t.prototype,r),n&&e(t,n),t}}();var s=function(){function e(){!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,e),this.errors={}}return n(e,[{key:"has",value:function(e){return this.errors.hasOwnProperty(e)}},{key:"any",value:function(){return Object.keys(this.errors).length>0}},{key:"count",value:function(){return Object.keys(this.errors).length}},{key:"get",value:function(e){if(this.errors[e])return this.errors[e][0]}},{key:"record",value:function(e){this.errors=e}},{key:"clear",value:function(e){e?delete this.errors[e]:this.errors={}}}]),e}(),a=function(){function e(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}return function(t,r,n){return r&&e(t.prototype,r),n&&e(t,n),t}}();var o=function(){function e(t){var r=arguments.length>1&&void 0!==arguments[1]&&arguments[1];for(var n in function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,e),this.originalData=_.cloneDeep(t),t)this[n]=t[n];this.formType=r?"update":"create",this.errors=new s}return a(e,[{key:"data",value:function(){var e={};for(var t in this.originalData)e[t]=this[t];return e}},{key:"reset",value:function(){arguments.length>0&&void 0!==arguments[0]&&arguments[0];if("create"==this.formType)for(var e in this.originalData)this[e]=this.originalData[e];this.errors.clear()}},{key:"post",value:function(e){return this.submit("post",e)}},{key:"put",value:function(e){return this.submit("put",e)}},{key:"patch",value:function(e){return this.submit("patch",e)}},{key:"delete",value:function(e){return this.submit("delete",e)}},{key:"submit",value:function(e,t){var r=this;return new Promise(function(n,s){axios[e](t,r.data()).then(function(e){r.onSuccess(e.data),n(e.data)}).catch(function(e){r.onFail(e.response.data),s(e.response)})})}},{key:"onSuccess",value:function(e){this.reset()}},{key:"onFail",value:function(e){e.hasOwnProperty("errors")&&this.errors.record(e.errors)}}]),e}();t.default={data:function(){return{form:new o({username:"",first_name:"",last_name:"",email:"",password:"",retype_password:""})}},methods:{onSubmit:function(){this.form.post("/register").then(function(e){setTimeout(function(){flash("User registration successful!")},2e3),window.location.replace("/")}).catch(function(e){flash("User registration failed.","danger")})}}}},AnTi:function(e,t,r){var n=r("+dUj");"string"==typeof n&&(n=[[e.i,n,""]]),n.locals&&(e.exports=n.locals);r("rjj0")("69694888",n,!0,{})},"Dlg+":function(e,t,r){window._=r("M4fF"),window.axios=r("mtWM");var n=document.head.querySelector('meta[name="csrf-token"]');n?window.axios.defaults.headers.common["X-CSRF-TOKEN"]=n.content:console.error("CSRF token not found.")},F1kH:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=function(){function e(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}return function(t,r,n){return r&&e(t.prototype,r),n&&e(t,n),t}}();var s=function(){function e(){!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,e),this.vue=new Vue}return n(e,[{key:"fire",value:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null;this.vue.$emit(e,t)}},{key:"listen",value:function(e,t){this.vue.$on(e,t)}}]),e}(),a=r("cK6X"),o=r.n(a),i=r("KGu1"),l=r.n(i),u=r("7W6c"),c=r.n(u);r("Dlg+"),window.Vue=r("I3G/"),window.Event=new s,window.flash=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"success",r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:3;window.Event.fire("flash",{message:e,level:t,timeout:r})};new Vue({el:"#app",components:{flash:o.a,"navigation-bar":l.a,"register-user":c.a}})},"FZ+f":function(e,t){e.exports=function(e){var t=[];return t.toString=function(){return this.map(function(t){var r=function(e,t){var r=e[1]||"",n=e[3];if(!n)return r;if(t&&"function"==typeof btoa){var s=(o=n,"/*# sourceMappingURL=data:application/json;charset=utf-8;base64,"+btoa(unescape(encodeURIComponent(JSON.stringify(o))))+" */"),a=n.sources.map(function(e){return"/*# sourceURL="+n.sourceRoot+e+" */"});return[r].concat(a).concat([s]).join("\n")}var o;return[r].join("\n")}(t,e);return t[2]?"@media "+t[2]+"{"+r+"}":r}).join("")},t.i=function(e,r){"string"==typeof e&&(e=[[null,e,""]]);for(var n={},s=0;s<this.length;s++){var a=this[s][0];"number"==typeof a&&(n[a]=!0)}for(s=0;s<e.length;s++){var o=e[s];"number"==typeof o[0]&&n[o[0]]||(r&&!o[2]?o[2]=r:r&&(o[2]="("+o[2]+") and ("+r+")"),t.push(o))}},t}},K4pD:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={props:{initialMessage:{required:!0,default:""},initialLevel:{default:"success"},initialDuration:{default:3}},data:function(){return{message:this.initialMessage,level:this.initialLevel,duration:this.initialDuration,show:!1}},created:function(){var e=this;Event.listen("flash",function(t){return e.flash(t)})},mounted:function(){this.$nextTick(function(){this.initialMessage&&this.flash({message:this.initialMessage,level:this.initialLevel,duration:this.initialDuration})})},methods:{flash:function(e){this.message=e.message||this.message,this.level=e.level||this.level;var t=e.duration||this.duration;this.show=!0,this.hide(t)},hide:function(e){var t=this;setTimeout(function(){t.show=!1},1e3*e)}}}},KGu1:function(e,t,r){var n=r("VU/8")(r("OaT9"),r("pGWO"),!1,function(e){r("SbzV")},"data-v-54a43a2a",null);e.exports=n.exports},KqWi:function(e,t){},OaT9:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={name:"NavigationBar",computed:{loggedIn:function(){return this.state.user.logged_in}},data:function(){return{state:State,showMobileNav:!1}},methods:{toggleMobileNav:function(){this.showMobileNav=!this.showMobileNav}}}},SbzV:function(e,t,r){var n=r("aJYv");"string"==typeof n&&(n=[[e.i,n,""]]),n.locals&&(e.exports=n.locals);r("rjj0")("4973beff",n,!0,{})},SxeD:function(e,t){e.exports={render:function(){var e=this.$createElement,t=this._self._c||e;return t("transition",{attrs:{name:"fade"}},[t("div",{directives:[{name:"show",rawName:"v-show",value:this.show,expression:"show"}],staticClass:"alert alert-flash",class:"alert-"+this.level,attrs:{role:"alert"},domProps:{innerHTML:this._s(this.message)}})])},staticRenderFns:[]}},"VU/8":function(e,t){e.exports=function(e,t,r,n,s,a){var o,i=e=e||{},l=typeof e.default;"object"!==l&&"function"!==l||(o=e,i=e.default);var u,c="function"==typeof i?i.options:i;if(t&&(c.render=t.render,c.staticRenderFns=t.staticRenderFns,c._compiled=!0),r&&(c.functional=!0),s&&(c._scopeId=s),a?(u=function(e){(e=e||this.$vnode&&this.$vnode.ssrContext||this.parent&&this.parent.$vnode&&this.parent.$vnode.ssrContext)||"undefined"==typeof __VUE_SSR_CONTEXT__||(e=__VUE_SSR_CONTEXT__),n&&n.call(this,e),e&&e._registeredComponents&&e._registeredComponents.add(a)},c._ssrRegister=u):n&&(u=n),u){var d=c.functional,f=d?c.render:c.beforeCreate;d?(c._injectStyles=u,c.render=function(e,t){return u.call(t),f(e,t)}):c.beforeCreate=f?[].concat(f,u):[u]}return{esModule:o,exports:i,options:c}}},aJYv:function(e,t,r){(e.exports=r("FZ+f")(!1)).push([e.i,"",""])},cK6X:function(e,t,r){var n=r("VU/8")(r("K4pD"),r("SxeD"),!1,function(e){r("AnTi")},"data-v-53f42613",null);e.exports=n.exports},kwhv:function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"flex mt-8"},[r("form",{staticClass:"w-full max-w-md",attrs:{method:"POST",action:"/register"},on:{submit:function(t){return t.preventDefault(),e.onSubmit(t)},keydown:function(t){e.form.errors.clear(t.target.name)}}},[r("div",{staticClass:"flex flex-wrap -mx-3 mb-6"},[r("div",{staticClass:"w-full px-3"},[r("label",{staticClass:"block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",class:{"text-red":e.form.errors.has("username")},attrs:{for:"grid-username"}},[e._v("\n                    Username\n                ")]),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.form.username,expression:"form.username"}],staticClass:"appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey",class:{"border border-red":e.form.errors.has("username")},attrs:{id:"grid-username",placeholder:"Username"},domProps:{value:e.form.username},on:{input:function(t){t.target.composing||e.$set(e.form,"username",t.target.value)}}}),e._v(" "),e.form.errors.has("username")?r("p",{staticClass:"text-red text-xs italic",domProps:{textContent:e._s(e.form.errors.get("username"))}}):e._e()])]),e._v(" "),r("div",{staticClass:"flex flex-wrap -mx-3 mb-6"},[r("div",{staticClass:"w-full md:w-1/2 px-3 mb-6 md:mb-0"},[r("label",{staticClass:"block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",attrs:{for:"grid-first-name"}},[e._v("\n                    First Name\n                ")]),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.form.first_name,expression:"form.first_name"}],staticClass:"appearance-none block w-full bg-grey-lighter text-grey-darker border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",attrs:{id:"grid-first-name",type:"text",placeholder:"Jane"},domProps:{value:e.form.first_name},on:{input:function(t){t.target.composing||e.$set(e.form,"first_name",t.target.value)}}})]),e._v(" "),r("div",{staticClass:"w-full md:w-1/2 px-3"},[r("label",{staticClass:"block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",attrs:{for:"grid-last-name"}},[e._v("\n                    Last Name\n                ")]),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.form.last_name,expression:"form.last_name"}],staticClass:"appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-grey",attrs:{id:"grid-last-name",type:"text",placeholder:"Doe"},domProps:{value:e.form.last_name},on:{input:function(t){t.target.composing||e.$set(e.form,"last_name",t.target.value)}}})])]),e._v(" "),r("div",{staticClass:"flex flex-wrap -mx-3 mb-6"},[r("div",{staticClass:"w-full px-3"},[r("label",{staticClass:"block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",class:{"text-red":e.form.errors.has("email")},attrs:{for:"grid-email"}},[e._v("\n                    Email\n                ")]),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.form.email,expression:"form.email"}],staticClass:"appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey",class:{"border border-red":e.form.errors.has("email")},attrs:{id:"grid-email",placeholder:"name@domain.com"},domProps:{value:e.form.email},on:{input:function(t){t.target.composing||e.$set(e.form,"email",t.target.value)}}}),e._v(" "),e.form.errors.has("email")?r("p",{staticClass:"text-red text-xs italic",domProps:{textContent:e._s(e.form.errors.get("email"))}}):e._e()])]),e._v(" "),r("div",{staticClass:"flex flex-wrap -mx-3 mb-6"},[r("div",{staticClass:"w-full px-3"},[r("label",{staticClass:"block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2",class:{"text-red":e.form.errors.has("password")||e.form.errors.has("retype_password")},attrs:{for:"grid-password"}},[e._v("\n                    Password\n                ")]),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.form.password,expression:"form.password"}],staticClass:"appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey",class:{"border border-red":e.form.errors.has("password")},attrs:{id:"grid-password",type:"password",placeholder:"Password"},domProps:{value:e.form.password},on:{input:function(t){t.target.composing||e.$set(e.form,"password",t.target.value)}}}),e._v(" "),e.form.errors.has("password")?r("p",{staticClass:"text-red text-xs italic mb-4",domProps:{textContent:e._s(e.form.errors.get("password"))}}):e._e(),e._v(" "),r("input",{directives:[{name:"model",rawName:"v-model",value:e.form.retype_password,expression:"form.retype_password"}],staticClass:"appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-grey",class:{"border border-red":e.form.errors.has("retype_password")},attrs:{id:"grid-password-confirm",type:"password",placeholder:"Confirm password"},domProps:{value:e.form.retype_password},on:{input:function(t){t.target.composing||e.$set(e.form,"retype_password",t.target.value)}}}),e._v(" "),e.form.errors.has("retype_password")?r("p",{staticClass:"text-red text-xs italic",domProps:{textContent:e._s(e.form.errors.get("retype_password"))}}):e._e()])]),e._v(" "),e._m(0)])])},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"flex flex-wrap mb-6"},[t("button",{staticClass:"flex-no-shrink bg-blue-darker hover:bg-blue-darkest border-blue-darker hover:border-blue-darkest text-sm border-4 text-white py-1 px-2 rounded"},[this._v("\n                Sign Up\n            ")])])}]}},pGWO:function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("nav",{staticClass:"flex items-center justify-between flex-wrap"},[e._m(0),e._v(" "),r("div",{staticClass:"block lg:hidden"},[r("button",{staticClass:"flex items-center px-3 py-2 border rounded text-blue-dark border-blue-dark bg-white  hover:border-blue-darker hover:text-blue-darker",on:{click:function(t){e.toggleMobileNav()}}},[r("svg",{staticClass:"fill-current h-3 w-3",attrs:{viewBox:"0 0 20 20",xmlns:"http://www.w3.org/2000/svg"}},[r("title",[e._v("Menu")]),e._v(" "),r("path",{attrs:{d:"M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"}})])])]),e._v(" "),r("div",{staticClass:"w-full block flex-grow lg:flex lg:items-center lg:w-auto lg:block",class:{"hidden sm:hidden md:hidden":!e.showMobileNav,"sm:block md:block":e.showMobileNav}},[e._m(1),e._v(" "),r("div",{staticClass:"text-lg"},[e.loggedIn?r("div",[r("a",{staticClass:"inline-block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6",attrs:{href:"/account"}},[e._v("\n                    My Account\n                ")])]):r("div",[r("a",{staticClass:"inline-block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6",attrs:{href:"#"}},[e._v("\n                    Login\n                ")]),e._v(" "),r("a",{staticClass:"inline-block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker ",attrs:{href:"/register"}},[e._v("\n                    Register\n                ")])])])])])},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"flex items-center flex-no-shrink mr-12"},[t("span",{staticClass:"text-4xl"},[this._v("Erik Westlund")])])},function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"text-lg lg:flex-grow"},[t("a",{staticClass:"block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6",attrs:{href:"#responsive-header"}},[this._v("\n                Blog\n            ")]),this._v(" "),t("a",{staticClass:"block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6",attrs:{href:"#responsive-header"}},[this._v("\n                About\n            ")]),this._v(" "),t("a",{staticClass:"block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6",attrs:{href:"#responsive-header"}},[this._v("\n                CV\n            ")]),this._v(" "),t("a",{staticClass:"block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker",attrs:{href:"#responsive-header"}},[this._v("\n                Contact Me\n            ")])])}]}},rjj0:function(e,t,r){var n="undefined"!=typeof document;if("undefined"!=typeof DEBUG&&DEBUG&&!n)throw new Error("vue-style-loader cannot be used in a non-browser environment. Use { target: 'node' } in your Webpack config to indicate a server-rendering environment.");var s=r("tTVk"),a={},o=n&&(document.head||document.getElementsByTagName("head")[0]),i=null,l=0,u=!1,c=function(){},d=null,f="data-vue-ssr-id",p="undefined"!=typeof navigator&&/msie [6-9]\b/.test(navigator.userAgent.toLowerCase());function m(e){for(var t=0;t<e.length;t++){var r=e[t],n=a[r.id];if(n){n.refs++;for(var s=0;s<n.parts.length;s++)n.parts[s](r.parts[s]);for(;s<r.parts.length;s++)n.parts.push(v(r.parts[s]));n.parts.length>r.parts.length&&(n.parts.length=r.parts.length)}else{var o=[];for(s=0;s<r.parts.length;s++)o.push(v(r.parts[s]));a[r.id]={id:r.id,refs:1,parts:o}}}}function h(){var e=document.createElement("style");return e.type="text/css",o.appendChild(e),e}function v(e){var t,r,n=document.querySelector("style["+f+'~="'+e.id+'"]');if(n){if(u)return c;n.parentNode.removeChild(n)}if(p){var s=l++;n=i||(i=h()),t=x.bind(null,n,s,!1),r=x.bind(null,n,s,!0)}else n=h(),t=function(e,t){var r=t.css,n=t.media,s=t.sourceMap;n&&e.setAttribute("media",n);d.ssrId&&e.setAttribute(f,t.id);s&&(r+="\n/*# sourceURL="+s.sources[0]+" */",r+="\n/*# sourceMappingURL=data:application/json;base64,"+btoa(unescape(encodeURIComponent(JSON.stringify(s))))+" */");if(e.styleSheet)e.styleSheet.cssText=r;else{for(;e.firstChild;)e.removeChild(e.firstChild);e.appendChild(document.createTextNode(r))}}.bind(null,n),r=function(){n.parentNode.removeChild(n)};return t(e),function(n){if(n){if(n.css===e.css&&n.media===e.media&&n.sourceMap===e.sourceMap)return;t(e=n)}else r()}}e.exports=function(e,t,r,n){u=r,d=n||{};var o=s(e,t);return m(o),function(t){for(var r=[],n=0;n<o.length;n++){var i=o[n];(l=a[i.id]).refs--,r.push(l)}t?m(o=s(e,t)):o=[];for(n=0;n<r.length;n++){var l;if(0===(l=r[n]).refs){for(var u=0;u<l.parts.length;u++)l.parts[u]();delete a[l.id]}}}};var g,b=(g=[],function(e,t){return g[e]=t,g.filter(Boolean).join("\n")});function x(e,t,r,n){var s=r?"":n.css;if(e.styleSheet)e.styleSheet.cssText=b(t,s);else{var a=document.createTextNode(s),o=e.childNodes;o[t]&&e.removeChild(o[t]),o.length?e.insertBefore(a,o[t]):e.appendChild(a)}}},tTVk:function(e,t){e.exports=function(e,t){for(var r=[],n={},s=0;s<t.length;s++){var a=t[s],o=a[0],i={id:e+":"+s,css:a[1],media:a[2],sourceMap:a[3]};n[o]?n[o].parts.push(i):r.push(n[o]={id:o,parts:[i]})}return r}}},[0]);