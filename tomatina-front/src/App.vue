<template>
  <div id="app">
    <md-toolbar>
      <h1 class="md-title" style="flex: 1">TOMATINA</h1>
      <md-button class="md-icon-button">
        <md-icon>more_vert</md-icon>
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
        username: ''
      }
    };
  }
};
</script>

<style>
#app {

}
</style>
