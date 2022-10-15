import Vue from 'vue'
import Router from 'vue-router'
import LoginRegister from "../components/LoginRegister";
import HelloWorld from "../components/HelloWorld";
import demo from "../components/demo";
import Login from "../components/Login";
import Main from "../components/Main";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/main',
      name: 'Main',
      component: Main
    },
    {
      path: '/hello-world',
      name: 'HelloWorld',
      component: HelloWorld
    },
  ],
  mode: 'history'

})
