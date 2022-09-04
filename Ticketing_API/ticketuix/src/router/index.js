import Vue from 'vue'
import Router from 'vue-router'
import formulario from '@/components/formulario'
import viewAgent from '@/components/viewAgent'
import homepage from '@/components/homepage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: homepage
    },
    {
      path: '/form',
      name: 'formulario',
      component: formulario
    },
    {
      path: '/list',
      name: 'viewAgent',
      component: viewAgent
    }
  ],
  mode: 'history'
})
