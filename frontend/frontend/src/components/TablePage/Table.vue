<template>
    <table>
        <tr>
            <th class="cell"><input type="checkbox" @change="commitChanges"/></th>
            <th class="cell">Номер</th>
            <th class="cell">Название</th>
            <th class="cell">Дата</th>
            <th class="cell">Статус</th>
        </tr>
        <TableRow v-for="(row, index) in this.$store.state.table" :index="index"/>
    </table>
</template>

<script>
    import TableRow from "./TableRow/TableRow";
    import {mapMutations} from "vuex";

    export default {
        components:
            {
                TableRow
            },
        methods: {
            commitChanges(e) {
                this.CHANGE_ALL_CHECKBOX(e.target.checked)
            },
            ...mapMutations(['CHANGE_ALL_CHECKBOX'])
        }
    }
</script>

<style scoped>
    table {
        margin: 0 auto;
        border-collapse: collapse;
        border: 3px solid darkslategray;
        width: 80%;
    }

    >>> .cell {
        padding: 5px;
        border: 3px solid darkslategray;
    }
</style>