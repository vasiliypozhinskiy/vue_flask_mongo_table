<template>
    <td class="cell">
        <input type="text" v-model="getValue"/>
    </td>
</template>

<script>
    export default {
        name: "NameCell",
        props: ["index"],
        computed: {
            getValue: { get() {return this.$store.state.table[this.index].title},
                set(value) {this.$store.dispatch("SAVE_ONE_CELL_IN_DB", {"index": this.index, "value": {"title": value}})}
            }
        }
    }
</script>

<style scoped>

</style>