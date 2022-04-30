<template>
  <div id="app">
    <nav>
      <router-link to="/welcome">Welcome</router-link>
      <router-link to="/config">Configuration</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
html, body {
  height:100%;
  width:100%;
}

* {
  margin:0;
  padding:0;
}
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  background-color: rgb(235, 235, 235);
}

nav a {
  text-decoration: none;
  font-size: 1.3em;
  font-weight: 500;
  color:dimgrey;
  margin:2%;
}

nav a.router-link-exact-active {
  color: goldenrod;
  text-decoration: underline;
}
</style>
