<template>
  <div id="app">
    <md-toolbar>
      <h1 class="md-title" style="flex: 1"><router-link :to="{ path: '/dashboard' }">TOMATINA</router-link></h1>      
      <span v-if="user.logged"><b>Welcome</b> {{user.username}}</span>      
      <md-button class="md-icon-button">
      </md-button>
    </md-toolbar>
    <div style="margin: 0 15px">
      <router-view :user="user"></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      user: {
        username: '',
        logged: false
      },
      logged: false
    };
  }
};
</script>

<style>
#app {

}
.md-title a, .md-title a:hover {
  color: #fff !important;
  text-decoration: none !important;
}
</style>
