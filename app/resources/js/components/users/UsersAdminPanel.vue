<template>
    <div>
        <table class="table">
            <tr>
                <th>Username</th>
                <th>Email</th>
                <th></th>
            </tr>
            <tr v-for="user in data.data" :key="user.id">
                <td v-text="user.username"></td>
                <td v-text="user.email"></td>
                <td>
                    <a :href="`/users/${user.id}/edit`">
                        <fa-icon :icon="['far', 'edit']" />
                    </a>
                </td>
            </tr>
        </table>
        <paginate class="mt-8"
                  name="users"
                  :data="paginationMeta"
        />
    </div>
</template>

<script>
    import AdminPanel from '../ui/AdminPanel'

    export default {
        name: "UsersAdminPanel",
        extends: AdminPanel,
    }
</script>

<style scoped>

</style>