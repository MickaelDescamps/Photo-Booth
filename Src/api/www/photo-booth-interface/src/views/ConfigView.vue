<template>
  <div>
    <div v-if="access == 'true'">
      <h1>Tu est connecté</h1>
      <config-form/>
    </div>
    <LoginForm v-else @submit="login" />
  </div>
</template>

<script>
import ConfigForm from '../components/ConfigForm.vue';
import LoginForm from "../components/LoginForm";

export default {
  data() {
      return {
          access: false
      }
  },

  methods: {
    login({ username, password }) {

        console.log("Username : " + username);
        console.log("Password : " + password);

        if(username=="admin" && password=="password")
        {
            console.log("Hello world 1");
            this.access = 'true';
        }
        else
        {
            console.log("Hello world 2");
            this.access = false;
        }

        console.log("Access : " + this.access);

        return this.access;
    }
  },

  components: { ConfigForm, LoginForm }
};
</script>