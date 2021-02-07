<template>
    <form class="login" @submit.prevent="login">
        <div>
            <div>Username</div>
            <input required v-model="username" class="textarea" type="text">
        </div>
        <div>
            <div>Password</div>
            <input required v-model="password" class="textarea" type="password">
            <div>
                <input class="btn" type="submit" value="Sign in">
            </div>
        </div>
    </form>
</template>

<script>
    export default {
        name: "LoginForm",
        data() {
            return {
                username: "",
                password: ""
            }
        },
        methods: {
            login: function () {
                const { username, password } = this
                this.$store.dispatch("AUTH_REQUEST", { username, password }).then(() => {
                    this.$router.push('/table-page')
                })
            }
        }
    }
</script>

<style scoped>
    .textarea {
        resize: none;
        border-radius: 5px;
        text-align: center;
    }
</style>