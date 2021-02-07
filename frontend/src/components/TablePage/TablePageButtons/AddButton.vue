<template>
    <div>
        <input class="btn" type="button" value="Add row" @click="AddRow">
    </div>
</template>

<script>
    export default {
        name: "AddButton",
        methods: {
            AddRow() {
                this.$store.dispatch("ADD_ROW_IN_DB");
            }
        }
    }
</script>

<style scoped>

</style>