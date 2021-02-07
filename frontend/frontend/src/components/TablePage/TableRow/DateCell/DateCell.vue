<template>
    <td class="cell">
        <input type="date" v-model="getValue"/>
    </td>
</template>

<script>
    export default {
        name: "DateCell",
        props: ["index"],
        computed: {
            getValue: { get() {return this.$store.state.table[this.index].date},
                set(value) {
                    if (value) {
                        this.$store.dispatch("SAVE_ONE_CELL_IN_DB", {"index": this.index, "value": {"date": value}})
                    }
                    else {
                        this.$forceUpdate();
                    }
                }
            }
        }
}
</script>

<style scoped>

</style>