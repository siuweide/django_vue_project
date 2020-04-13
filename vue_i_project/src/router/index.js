import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import home from '@/views/home'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
      props: {
          menu:'service'
      },
      children:[
          {
              path: 'service',
              name: 'service',
              component: () => import('../views/service/index.vue'),
          },
          {
              path: '/',
              name: '/',
              component: () => import('../views/service/index.vue'),
          },
      ]
    },
    {
      path: '/',
      name: 'home',
      component: home,
      props: {
          menu:'task'
      },
      children:[
          {
              path: 'task',
              name: 'task',
              component: () => import('../views/task/index.vue'),
          },
      ]
    },
    {
      path: '/',
      name: 'home',
      component: home,
      props: {
          menu:'interface'
      },
      children:[
          {
              path: 'interface',
              name: 'interface',
              component: () => import('../views/interface/index.vue'),
          },
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/login/index.vue'),
    },
  ]
})
