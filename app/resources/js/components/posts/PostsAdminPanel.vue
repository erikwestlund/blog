<template>
    <div>
        <transition name="trx-slide-fade">
            <table
                    v-if="hasObjects"
                    class="table w-full"
            >
                <tr>
                    <th>Title</th>
                    <th>Author</th>
                    <th>Updated</th>
                    <th/>
                </tr>
                <tr
                        v-for="post in data.data"
                        :key="post.id"
                >
                    <td v-text="post.title"/>
                    <td v-text="getUsername(post)"/>
                    <td>{{ post.updated_at | ago }} ago</td>
                    <td>
                        <a :href="`/admin/posts/${post.id}`">
                            <fa-icon :icon="['far', 'edit']"/>
                        </a>
                    </td>
                </tr>
            </table>
            <div v-else-if="ready">
                No posts have been yet! <a href="/admin/posts/create">Make One</a>.
            </div>
        </transition>
        <paginate
                class="mt-8"
                name="posts"
                :data="paginationMeta"
        />
    </div>
</template>

<script>
    import AdminPanel from '../ui/AdminPanel'

    export default {
        name: 'PostsAdminPanel',
        extends: AdminPanel,
        methods: {
            getUsername(post) {
                return !_.isEmpty(post.user) && post.user.username
                    ? post.user.username
                    : ''
            }
        }
    }
</script>

<style scoped>

</style>
