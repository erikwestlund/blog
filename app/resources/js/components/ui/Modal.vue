<template>
    <div>
        <transition name="modal">
            <div class="modal-mask" @click="$emit('close')">
                <div class="modal-wrapper">
                    <div class="modal-container"
                         :class="{'lg': large, 'sm':small}"
                         @click.stop
                    >

                        <div class="modal-header">
                            <slot name="header">
                                default header
                            </slot>
                        </div>

                        <div class="modal-body mt-10">
                            <slot name="body">
                                default body
                            </slot>
                        </div>

                        <div class="modal-footer mt-10 flex content-end flex-wrap">
                            <div class="w-3/4 m-auto text-sm">
                                <slot name="footer">

                                </slot>
                            </div>
                            <div class="w-1/4 text-right">
                                <button class="btn btn-grey hover:bg-grey-darkest hover:border-grey-darkest"
                                        @click="$emit('close')">
                                    <fa-icon class="mr-2" :icon="['far', 'times']"/>
                                    {{ doneText }}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
    export default {
        created() {
            document.addEventListener('keyup', this.escapeKeyListener);
        },
        destroyed() {
            document.removeEventListener('keyup', this.escapeKeyListener);
        },
        data() {
            return {
                showModal: false,
            }
        },
        methods: {
            escapeKeyListener(event) {
                if (event.keyCode === 27) {
                    this.$emit('close');
                }
            },
        },
        props: {
            doneText: {
                type: String,
                default: 'OK',
            },
            doneIcon: {
                type: String,
                default: 'times',
            },
            large: {
                type: Boolean,
                default: false
            },
            small: {
                type: Boolean,
                default: false
            }
        }
    }
</script>

<style scoped>
    .modal-mask {
        position: fixed;
        z-index: 9998;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .5);
        display: table;
        transition: opacity .3s ease;
    }

    .modal-wrapper {
        display: table-cell;
        vertical-align: middle;
    }

    .modal-container {
        width: 500px;
        margin: 0px auto;
        padding: 20px 30px;
        background-color: #fff;
        border-radius: 2px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
        transition: all .3s ease;
    }

    .modal-container.lg {
        width: 90%;
    }

    .modal-container.sm {
        width: 350px;
    }

    .modal-header h3 {
        margin-top: 0;
        color: #42b983;
    }

    .modal-enter {
        opacity: 0;
    }

    .modal-leave-active {
        opacity: 0;
    }

    .modal-enter .modal-container,
    .modal-leave-active .modal-container {
        -webkit-transform: scale(1.1);
        transform: scale(1.1);
    }
</style>