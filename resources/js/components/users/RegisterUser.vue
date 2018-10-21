<template>
    <div>
        <button @click="register()">Register</button>
    </div>
</template>

<script>
    export default {
        mounted() {
            console.log('Component mounted.')
        },
        methods: {
            register() {
                axios.post('/register')
                    .then(response => {
                        console.log(response.data);
                    })
            }
        }
    }
</script>