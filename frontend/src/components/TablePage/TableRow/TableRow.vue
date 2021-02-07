<template>
    <tr>
        <CheckBoxCell :index="index"/>
        <IdCell :index="index"/>
        <NameCell :index="index"/>
        <DateCell :index="index"/>
        <StatusCell :index="index"/>
    </tr>
</template>

<script>
    import IdCell from "./NumberCell/NumberCell";
    import NameCell from "./TitleCell/TitleCell";
    import DateCell from "./DateCell/DateCell";
    import StatusCell from "./StatusCell/StatusCell";
    import CheckBoxCell from "./CheckBoxCell/CheckBoxCell";
    export default {
        name: "TableRow",
        props: ["index"],
        components: {StatusCell, DateCell, NameCell, IdCell, CheckBoxCell}
    }
</script>

<style scoped>

</style>