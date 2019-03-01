<template>
    <div>
        <transition name="trx-slide-fade">
            <table
                    v-if="hasObjects"
                    class="table w-full overflow-scroll"
            >
                <tr>
                    <th>Username</th>
                    <th class="hidden md:table-cell">
                        Email
                    </th>
                    <th class="hidden md:table-cell">
                        Registered
                    </th>
                    <th/>
                </tr>
                <tr
                        v-for="user in data.data"
                        :key="user.id"
                >
                    <td v-text="user.username"/>
                    <td
                            class="hidden md:table-cell"
                            v-text="user.email"
                    />
                    <td class="hidden md:table-cell">
                        {{ user.created_at | ago }} ago
                    </td>
                    <td>
                        <a :href="`/users/${user.id}`">
                            <fa-icon :icon="['far', 'edit']"/>
                        </a>
                    </td>
                </tr>
            </table>
            <div v-else-if="ready">
                No users have been registered! <a href="/register">Register</a>.
            </div>
            <paginate
                    class="mt-8"
                    name="users"
                    :data="paginationMeta"
            />
        </transition>
    </div>
</template>

<script>
    import AdminPanel from '../ui/AdminPanel'

    export default {
        name: 'UsersAdminPanel',
        extends: AdminPanel
    }
</script>

<style scoped>

</style>
