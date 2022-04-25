import { createRouter, createWebHashHistory } from 'vue-router'
import StartPage from '../views/StartPage.vue'
import ConfigView from '../views/ConfigView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: StartPage
  },
  {
    path: '/config',
    name: 'config',
    component: ConfigView
    
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
