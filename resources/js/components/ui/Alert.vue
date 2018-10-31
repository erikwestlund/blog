<template>
    <div>
        <transition name="fade">
            <div role="alert"
                 class="alert mb-4"
                 :class="'alert-' + category"
                 v-show="show"
                 :show.sync="visible"
            >
                <div class="flex">
                    <!--<button type="button" class="close float-right" v-if="!important" @click="hide()">-->
                        <!--<fa-icon :class="'alert-' + category" :icon="['far', 'times']"/>-->
                    <!--</button>-->

                    <slot></slot>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
    export default {
        props: {
            category: {
                type: String,
                default: 'info'
            },
            duration: {
                type: Number,
                default: 5000
            },
            important: {
                type: Boolean,
                default: false
            },
            show: {
                type: Boolean,
                default: false
            },
            temporary: {
                type: Boolean,
                default: true
            },
        },
        data() {
            return {
                visible: false,
            }
        },
        methods: {
            hide() {
                this.$emit('update:show', false);
            }
        },
        mounted() {
            this.$nextTick(() => {

                if (this.temporary) {
                    setTimeout(
                        () => hide(),
                        this.duration
                    )
                }
            })
        }
    }
</script>

<style scoped>
</style>