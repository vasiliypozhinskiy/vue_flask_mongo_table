<template>
    <td class="cell">
        <input type="checkbox" v-model="getValue"/>
    </td>
</template>

<script>
    export default {
        name: "CheckBoxCell",
        props: ["index"],
        computed: {
            getValue: { get() {return this.$store.state.table[this.index].isChecked},
                set(value) {this.$store.commit("CHANGE_CHECKBOX", {"index": this.index, 'value': value})}
            }
        }
    }
</script>

<style scoped>

</style>