<template>
  <on-click-outside :do="handleClickOutside">
    <span class="relative">
      <span
        href="/admin"
        title="Admin Tools"
        class="inline-block mt-4 lg:inline-block lg:mt-0 text-blue-dark hover:text-blue-darker cursor-pointer"
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
                  :icon="['far', 'user']"
                />
                <a
                  href="/admin/users"
                  class="text-blue-dark hover:text-blue-darker"
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
