import axios from 'axios';
import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

new Vue({
  router,
  data() {
    return {
      current_state: 'WAIT',
      intervalId2: 1,
    };
  },
  render: (h) => h(App),
  methods: {
    getState() {
      const path = 'http://localhost:5000/api/get_state';
      axios.get(path)
        .then((res) => {
          if (res.data.state !== this.current_state) {
            if (res.data.state === 'WAIT') {
              this.current_state = res.data.state;
              this.$router.push({ name: 'WelcomeView' });
            } else if (res.data.state === 'TAKE_PICTURE') {
              this.current_state = res.data.state;
              this.$router.push({ name: 'TakePhotoView' });
            } else if (res.data.state === 'REVIEW') {
              this.current_state = res.data.state;
              console.log(res.data.photo_name);
              this.$router.push({ name: 'ConfirmPhoto', params: { photoPath: res.data.photo_name } });
            }
          }
        });
    },
    loop() {
      this.intervalId2 = window.setInterval(() => {
        this.getState();
      }, (100));
    },
  },
  created() {
    this.loop();
  },
}).$mount('#app');
