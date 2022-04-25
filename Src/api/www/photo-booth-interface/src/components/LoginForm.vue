<template>
  <form>
    <p v-if="errorMessage" class="error"></p>
    <input type="username" v-model="username" />
    <input type="password" v-model="password" />
    <button type="button" v-on:click="submit">Connexion</button>
  </form>
</template>

<script>
export default {
  props: {
      errorMessage: {
          type: String,
          default: ""
      }
  },
  methods: {
    submit() {
      console.log("Submit is call !!!");
      this.$emit("submit", {
        username: this.username,
        password: this.password
      });
    }
  }
};
</script>

<style scoped>
.error { color: tomato; }
</style>