import axios from 'axios';
import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

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
              this.$router.push({ name: 'ConfirmPhoto' });
            }
          }
        });
    },
    loop() {
      this.intervalId2 = window.setInterval(() => {
        this.getState();
      }, (500));
    },
  },
  created() {
    this.loop();
  },
}).$mount('#app');
