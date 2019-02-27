<template>
    <nav class="flex items-center justify-between flex-wrap">
        <div class="flex items-center flex-no-shrink mr-12">
            <span class="text-4xl">
                <a class="text-black" href="/">Erik Westlund</a>
            </span>
        </div>
        <div class="block lg:hidden">
            <button
                class="flex items-center px-3 py-2 border rounded border-blue-dark bg-white hover:border-blue-darker"
                @click="toggleMobileNav()"
            >
                <svg
                    class="fill-current h-3 w-3"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <title>Menu</title>
                    <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
                </svg>
            </button>
        </div>
        <div
            class="w-full block flex-grow lg:flex lg:items-center lg:w-auto lg:block"
            :class="{
                'hidden sm:hidden md:hidden' : ! showMobileNav,
                'sm:block md:block' : showMobileNav,
            }"
        >
            <div class="text-lg lg:flex-grow">
                <a
                    href="/"
                    class="block mt-4 lg:inline-block lg:mt-0 mr-6"
                >
                    Blog
                </a>
                <!--<a-->
                    <!--href="#"-->
                    <!--class="block mt-4 lg:inline-block lg:mt-0 mr-6"-->
                <!--&gt;-->
                    <!--About-->
                <!--</a>-->
                <!--<a-->
                    <!--href="#"-->
                    <!--class="block mt-4 lg:inline-block lg:mt-0 mr-6"-->
                <!--&gt;-->
                    <!--CV-->
                <!--</a>-->
                <a
                    href="mailto:edbwestlund@gmail.com"
                    class="block mt-4 lg:inline-block lg:mt-0"
                >
                    Contact Me
                </a>
            </div>
            <div class="font-lighter">
                <div v-if="loggedIn">
                    <a
                        href="/admin/posts/create"
                        title="Create Post"
                        class="inline-block mt-4 lg:inline-block lg:mt-0 mr-6"
                    >
                        <fa-icon
                            class="mr-1"
                            :icon="['far', 'pencil']"
                        />
                    </a>
                    <a
                        href="/account"
                        title="Your Account"
                        class="inline-block mt-4 lg:inline-block lg:mt-0 mr-6"
                    >
                        <fa-icon
                            class="mr-1"
                            :icon="['far', 'user']"
                        />
                    </a>
                    <a
                        href="/logout"
                        title="Log Out"
                        class="inline-block mt-4 lg:inline-block lg:mt-0 mr-6"
                    >
                        <fa-icon
                            class="mr-1"
                            :icon="['far', 'sign-out']"
                        />
                    </a>
                    <admin-menu-dropdown v-if="state.user.is_admin" />
                </div>
                <div v-else>
                    <a
                        href="/login"
                        title="Log In"
                        class="inline-block mt-4 lg:inline-block lg:mt-0 mr-6"
                        @click.prevent
                        @click.exact="showLoginModal = true"
                    >
                        <fa-icon
                            class="mr-1"
                            :icon="['far', 'sign-in']"
                        />
                    </a>
                    <a
                        href="/register"
                        title="Register"
                        class="inline-block mt-4 lg:inline-block lg:mt-0"
                    >
                        <fa-icon
                            class="mr-1"
                            :icon="['far', 'user-plus']"
                        />
                    </a>
                </div>
            </div>
        </div>
        <!--Modals-->
        <modal
            v-if="showLoginModal"
            done-text="Close"
            @close="showLoginModal = false"
        >
            <h3 slot="header">
                <fa-icon
                    class="mr-2"
                    :icon="['far', 'sign-in']"
                />
                Log In
            </h3>

            <div slot="body">
                <login-user />
            </div>

            <div slot="footer">
                <fa-icon
                    class="mr-2 text-grey-dark"
                    :icon="['far', 'key']"
                />
                <a
                    class="text-blue-dark  pt-4"
                    href="/users/reset-password"
                >
                    Reset
                    Password
                </a>
            </div>
        </modal>
    </nav>
</template>

<script>
import AdminMenuDropdown from './AdminMenuDropdown'
import LoginUser from '../users/LoginUser'
import Modal from './Modal'

export default {
    name: 'NavigationBar',
    components: {
        'admin-menu-dropdown': AdminMenuDropdown,
        'modal': Modal,
        'login-user': LoginUser
    },
    data () {
        return {
            state: State,
            showLoginModal: false,
            showMobileNav: false
        }
    },
    computed: {
        loggedIn () {
            return this.state.user.logged_in
        }
    },
    created () {
        Event.listen('closeLoginModal', () => {
            this.showLoginModal = false
        })
    },
    methods: {
        toggleMobileNav () {
            this.showMobileNav = !this.showMobileNav
        }
    }
}
</script>

<style scoped>

</style>
