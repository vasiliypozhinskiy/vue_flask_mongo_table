<template>
  <div class="table-page">
    <Table/>
    <AddButton/>
    <DeleteButton/>
  </div>
</template>

<script>
import AddButton from "../components/TablePage/TablePageButtons/AddButton";
import DeleteButton from "../components/TablePage/TablePageButtons/DeleteButton";
import Table from "../components/TablePage/Table";
export default {
  name: "TablePage",
  components: {
    DeleteButton,
    AddButton,
    Table
  },
  created() {
    this.$store.dispatch('LOAD_TABLE');
  }
}
</script>
