<template>
    <div>
        <router-link to="/">Login</router-link>
        |
        <router-link to="/table-page">Table</router-link>
        <div>
            <div v-if="getUsername">Logged in as {{getUsername}}</div>
        </div>
        <input class="btn" type="button" value="Logout" @click="logout" v-if="getUsername"/>
    </div>
</template>

<script>
    export default {
        name: "Header",
        computed: {
            getUsername: {
                get() {
                    return this.$store.state.username
                }
            }
        },
        methods: {
            logout: function () {
                this.$store.dispatch("AUTH_LOGOUT").then(() => {
                    if (this.$router.currentRoute.name !== "Login") {
                        this.$router.push('/')
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>