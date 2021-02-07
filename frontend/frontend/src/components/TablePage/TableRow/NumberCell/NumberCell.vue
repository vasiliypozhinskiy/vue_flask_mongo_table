<template>
    <td class="cell">
        <input class="number" type="number" v-model="getValue" @keydown="check_number($event)"/>
    </td>
</template>

<script>
    export default {
        name: "IdCell",
        props: ['index'],
        computed: {
            getValue: { get() {return this.$store.state.table[this.index].number},
                set(value) {this.$store.dispatch("SAVE_ONE_CELL_IN_DB", {"index": this.index, "value": {"number": value}})}
            }
        },
        methods: {
            check_number: (e) => {
                if (e.keyCode === 69) {
                    e.preventDefault()
                }
            }
        }
    }
</script>

<style scoped>
    .number::-webkit-outer-spin-button,
    .number::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    .number[type=number] {
        -moz-appearance: textfield;
    }
</style>