<template>
    <div>
        <input class="btn" type="button" value="Delete selected rows" @click="DeleteRows">
    </div>
</template>

<script>
    export default {
        name: "DeleteButton",
        methods: {
            DeleteRows () {
                this.$store.dispatch("DELETE_ROWS_FROM_DB")
            }
        }
    }
</script>

<style scoped>

</style>