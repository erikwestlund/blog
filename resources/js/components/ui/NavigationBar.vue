<template>
    <nav class="flex items-center justify-between flex-wrap">
        <div class="flex items-center flex-no-shrink mr-12">
            <span class="text-4xl">Erik Westlund</span>
        </div>
        <div class="block lg:hidden">
            <button class="flex items-center px-3 py-2 border rounded text-blue-dark border-blue-dark bg-white  hover:border-blue-darker hover:text-blue-darker" @click="toggleMobileNav()">
                <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <title>Menu</title>
                    <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                </svg>
            </button>
        </div>
        <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto lg:block"
                 :class="{
                    'hidden sm:hidden md:hidden' : ! showMobileNav,
                    'sm:block md:block' : showMobileNav,
                  }"
        >
            <div class="text-lg lg:flex-grow">
                <a href="#responsive-header"
                   class="block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6">
                    Blog
                </a>
                <a href="#responsive-header"
                   class="block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6">
                    About
                </a>
                <a href="#responsive-header"
                   class="block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6">
                    CV
                </a>
                <a href="#responsive-header"
                   class="block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker">
                    Contact Me
                </a>
            </div>
            <div class="text-lg">
                <div v-if="loggedIn">
                    <a href="/account"
                       class="inline-block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6">
                        My Account
                    </a>
                </div>
                <div v-else>
                    <a href="#"
                       class="inline-block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker mr-6">
                        Login
                    </a>
                    <a href="/register"
                       class="inline-block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker ">
                        Register
                    </a>
                </div>

            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'NavigationBar',
        computed: {
          loggedIn() {
              return this.state.user.logged_in;
          }
        },
        data() {
            return {
                state: State,
                showMobileNav: false,
            }
        },
        methods: {
            toggleMobileNav() {
                this.showMobileNav = ! this.showMobileNav;
            }
        },
    }
</script>

<style scoped>

</style>