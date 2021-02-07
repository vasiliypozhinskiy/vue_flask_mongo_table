<template>
  <div id="app">
    <div id="nav">
      <Header/>
    </div>
    <router-view/>
  </div>
</template>

<style>
.btn {
  margin: 5px;
  border-radius: 5px;
  background-color: darkgray;
}
.btn:hover {
  background-color: gray;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
<script>
  import Header from "./components/Header/Header";
  export default {
    components: {Header}
  }
</script>