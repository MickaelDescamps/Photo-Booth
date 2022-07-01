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
  height:90%;
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#message
{
  width: 80%;
  height: 80%;
  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;
  align-self: center;
  padding:5%;
}

h1
{
  font-size:5em;
}
h2
{
  font-size:3em;
}
</style>
