<template>
    <div id="page">
        <h1> La photos va être prise dans</h1>
        <p id="timeout">{{count}}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TakePhotoView',
  data() {
    return {
      count: 10,
      intervalId: 0,
    };
  },
  methods: {
    getCount() {
      const path = 'http://localhost:5000/api/count';
      axios.get(path)
        .then((res) => {
          if (res.data.count === true || res.data.count === 1) {
            if (this.$route.path !== this.$router.resolve({ name: 'ConfirmPhoto' })) {
              window.clearInterval(this.intervalId);
              this.$router.push({ name: 'ConfirmPhoto' });
            }
          } else if (res.data.count !== false) {
            this.count = res.data.count;
          } else {
            this.count = 10;
          }
        });
    },
    loop() {
      this.intervalId = window.setInterval(() => {
        this.getCount();
      }, 500);
    },
  },
  created() {
    this.loop();
  },
};
</script>
