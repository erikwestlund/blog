<template>
    <div>
        <transition name="trx-fade">
            <div role="alert"
                 class="alert mb-4"
                 :class="'alert-' + category"
                 v-show="show"
            >
                <button type="button" class="float-right" v-if="!important" @click="hide()">
                    <fa-icon :class="'alert-x-' + category" :icon="['far', 'times']"/>
                </button>

                <slot></slot>
            </div>
        </transition>
    </div>
</template>

<script>
    export default {
        name: "Alert",
        created() {
            Event.listen('hideAlert', () => this.hide())
        },
        props: {
            category: {
                type: String,
                default: 'message'
            },
            duration: {
                type: Number,
                default: 3000,
            },
            important: {
                type: Boolean,
                default: false
            },
            initShow: {
                type: Boolean,
                default: true
            },
            temporary: {
                type: Boolean,
                default: true
            },
        },
        data() {
            return {
                show: this.initShow,
            }
        },
        methods: {
            hide() {
                this.show = false;
            }
        },
        mounted() {
            this.$nextTick(() => {

                if (this.temporary) {
                    setTimeout(() => {
                            Event.fire('hideAlert')
                        },
                        this.duration);
                }
            })
        }
    }
</script>

<style scoped>
</style>