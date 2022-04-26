<template>
  <div id="page">
    <div id="message">
      <h1>{{main_title}}</h1>
      <h2>{{sub_title}}</h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'WelcomeView',
  data() {
    return {
      main_title: '',
      sub_title: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/welcome';
      axios.get(path)
        .then((res) => {
          this.main_title = res.data.main_title;
          this.sub_title = res.data.sub_title;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};

</script>
