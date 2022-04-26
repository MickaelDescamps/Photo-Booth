<template>
  <div>
    <p>{{msg}}</p>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'PingPong',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    loop() {
      window.setInterval(() => {
        console.info('Call');
        this.getMessage();
      }, 500);
    },
  },
  created() {
    this.getMessage();
    this.loop();
  },
};
</script>
