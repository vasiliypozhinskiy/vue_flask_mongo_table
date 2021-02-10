import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSocketIO from 'vue-socket.io'
import host from './store'

Vue.config.productionTip = false

Vue.use(new VueSocketIO({
  debug: true,
  connection: host,
  vuex: {
    store,
    actionPrefix: 'SOCKET_',
    mutationPrefix: 'SOCKET_'
  },
  options: { path: "/socket" }
}))

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
