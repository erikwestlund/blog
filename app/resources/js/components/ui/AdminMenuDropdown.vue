<template>
    <on-click-outside :do="handleClickOutside">
        <span class="relative">
            <span
                href="/admin"
                title="Admin Tools"
                class="inline-block mt-4 lg:inline-block lg:mt-0 cursor-pointer text-blue-darker hover:text-blue-dark"
                @click="open = !open"
            >
                <fa-icon
                    class="mr-1"
                    :icon="['far', 'lock']"
                />

                <transition name="trx-slide-fade">
                    <div
                        v-show="open"
                        class="shadow absolute w-48 pin-r mt-1 text-md text-grey-darker leading-normal rounded bg-white border p-3"
                    >
                        <ul class="list-reset">
                            <li>
                                <fa-icon
                                    class="mr-2 text-grey"
                                    :icon="['far', 'file-edit']"
                                />
                                <a
                                    href="/admin/posts"
                                >
                                    Posts
                                </a>
                            </li>
                            <li class="mt-2">
                                <fa-icon
                                    class="mr-2 text-grey"
                                    :icon="['far', 'file-alt']"
                                />
                                <a
                                    href="/admin/pages"
                                >
                                    Pages
                                </a>
                            </li>
                            <li class="mt-2">
                                <fa-icon
                                    class="mr-2 text-grey"
                                    :icon="['far', 'user']"
                                />
                                <a
                                    href="/admin/users"
                                >
                                    Users
                                </a>
                            </li>
                        </ul>
                    </div>
                </transition>
            </span>
        </span>
    </on-click-outside>
</template>

<script>
import OnClickOutside from '../utils/OnClickOutside.vue'

export default {
    name: 'AdminMenuDropdown',
    components: {
        OnClickOutside
    },
    data () {
        return {
            open: false
        }
    },
    methods: {
        handleClickOutside () {
            if (this.open) {
                this.open = false
            }
        }
    }
}
</script>
