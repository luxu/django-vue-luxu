import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import Pavilhao1 from '@/components/Pavilhao1'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: VueDemo
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages
    },
    {
      path: '/pavilhao1',
      name: 'pavilhao1',
      component: Pavilhao1
    }
  ]
})
