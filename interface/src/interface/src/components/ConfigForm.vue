<template>
    <div class="form">
        <form>
        <p>
            <label for="main_title">Titre Principal :
                <input name="main_title"
                v-model="personnalized_main_title"/><br/>
                </label>
            <label for="sub_title">Sous titre principal :
                <input name="sub_title"
                v-model="personnalized_sub_title"/>
                </label>
        </p>
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
      personnalized_sub_title: '',
      personnalized_main_title: '',
    };
  },
  methods: {
    submitConfig() {
      const path = 'http://localhost:5000/config';
      axios.post(path, {
        main_title: this.personnalized_main_title,
        sub_title: this.personnalized_sub_title,
      })
        .then((res) => {
          if (res === true) {
            this.getConfig();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getConfig() {
      const path = 'http://localhost:5000/config';
      axios.get(path)
        .then((res) => {
          this.personnalized_main_title = res.data.main_title;
          this.personnalized_sub_title = res.data.sub_title;
          console.info(res.data);
          return true;
        })
        .catch((error) => {
          console.error(error);
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
