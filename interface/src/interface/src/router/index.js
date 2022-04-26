import Vue from 'vue';
import VueRouter from 'vue-router';
import PingPong from '../components/PingPong.vue';
import WelcomeView from '../views/WelcomeView.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/ping',
    name: 'PingPong',
    component: PingPong,
  },
  {
    path: '/welcome',
    name: 'WelcomeView',
    component: WelcomeView,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
