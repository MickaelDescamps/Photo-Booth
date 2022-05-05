<template>
    <div class="form">
        <form>
          <h2>Section welcome</h2>
            <label for="main_title">Titre Principal :
                <input name="main_title"
                v-model="config.welcome.main_title"/><br/>
                </label>
            <label for="sub_title">Sous titre principal :
                <input name="sub_title"
                v-model="config.welcome.sub_title"/>
                </label>
          <h2>Section confirm photo</h2>
            <label for="message">Message :
                <input name="message"
                v-model="config.confirm_photo.message"/>
                </label><br/>
            <label for="message_suite">Message suite :
                <input name="message_suite"
                v-model="config.confirm_photo.message_suite"/>
                </label>
        <p>
            <input type="button" v-on:click="submitConfig" value="Submit">
        </p>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ConfigForm',
  data() {
    return {
      config: {},
    };
  },
  methods: {
    submitConfig() {
      const path = 'http://localhost:5000/config';
      axios.post(path, {
        config: this.config,
      })
        .then((res) => {
          if (res === true) {
            this.getConfig();
          }
        });
    },
    getConfig() {
      const path = 'http://localhost:5000/config';
      axios.get(path)
        .then((res) => {
          this.config = res.data;
          return true;
        });
    },
  },
  created() {
    this.getConfig();
  },
};
</script>

<style>
input
{
font-size:1em;
width:20em;
}
</style>
