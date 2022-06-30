import Vue from 'vue';
import VueRouter from 'vue-router';
import PingPong from '../components/PingPong.vue';
import WelcomeView from '../views/WelcomeView.vue';
import ConfigView from '../views/ConfigView.vue';
import TakePhotoView from '../views/TakePhotoView.vue';
import ConfirmPhotoView from '../views/ConfirmPhotoView.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    redirect: '/welcome',
  },
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
  {
    path: '/config',
    name: 'ConfigView',
    component: ConfigView,
  },
  {
    path: '/take_photo',
    name: 'TakePhotoView',
    component: TakePhotoView,
  },
  {
    path: '/confirm_photo/:photoPath',
    name: 'ConfirmPhoto',
    component: ConfirmPhotoView,
    props: true,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
