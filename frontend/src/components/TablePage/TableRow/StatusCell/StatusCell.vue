<template>
    <td class="cell">
        <input type="text" v-model="getValue"/>
    </td>
</template>

<script>
    export default {
        name: "StatusCell",
        props: ["index"],
        computed: {
            getValue: {
                get() {
                    return this.$store.state.table[this.index].status
                },
                set(value) {
                    this.$store.dispatch("SAVE_MANY_CELLS_IN_DB", {"index": this.index,"value": value})
                }
            }
        }
    }
</script>

<style scoped>

</style>