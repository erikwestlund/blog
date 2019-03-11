<template>
    <div>
        <transition name="trx-slide-fade">
            <table
                v-if="hasObjects"
                class="table w-full"
            >
                <tr>
                    <th>Title</th>
                    <th>Updated</th>
                    <th />
                </tr>
                <tr
                    v-for="page in data.data"
                    :key="page.id"
                >
                    <td>
                        <a :href="`/admin/pages/${page.id}`">
                            {{ page.title }}
                        </a>
                    </td>
                    <td>{{ page.updated_at | ago }} ago</td>
                    <td class="text-right">
                        <a :href="`/admin/pages/${page.id}`">
                            <fa-icon :icon="['far', 'edit']" />
                        </a>
                    </td>
                </tr>
            </table>
            <div v-else-if="ready">
                No pages have been yet! <a href="/admin/pages/create">Make One</a>.
            </div>
        </transition>
        <paginate
            class="mt-8"
            name="pages"
            :data="paginationMeta"
        />
    </div>
</template>

<script>
import AdminPanel from '../ui/AdminPanel'

export default {
    name: 'PagesAdminPanel',
    extends: AdminPanel

}
</script>

<style scoped>

</style>
