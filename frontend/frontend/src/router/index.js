import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../views/LoginPage.vue';
import TablePage from "../views/TablePage";
import store from "../store/index";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/table-page',
    name: 'TablePage',
    component: TablePage
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  let isAuthenticated = store.getters.isAuthenticated
  if (to.name !== 'Login' && !isAuthenticated) next({ name: 'Login' })
  else next()
})

export default router
