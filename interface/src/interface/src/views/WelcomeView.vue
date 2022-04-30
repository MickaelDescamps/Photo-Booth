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

<style>
#app
{
  height:100%;
}
#page
{
  width:100%;
  height:100%;
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#message
{
  width: fit-content;
  align-self: center;
  padding:5%;
  background-color: rgb(235, 235, 235);
  border: 0.5em darkblue solid;
}
</style>
