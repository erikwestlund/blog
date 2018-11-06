<template>
    <div>
        <table class="table">
            <tr>
                <th>Username</th>
                <th>Email</th>
                <th></th>
            </tr>
            <tr v-for="user in users.data" :key="user.id">
                <td v-text="user.username"></td>
                <td v-text="user.email"></td>
                <td>
                    <a :href="`/users/${user.id}/edit`">
                        <fa-icon :icon="['far', 'edit']" />
                    </a>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
    export default {
        name: "UsersAdminPanel",
        data() {
          return {
              users: [],
          }
        },
        created() {
            axios.get('/admin/users.json')
                .then(response => {
                    this.users = response.data;
                })
                .catch(errors => {
                    flash('Could not get users', 'danger')
                })
        }
    }
</script>

<style scoped>

</style>