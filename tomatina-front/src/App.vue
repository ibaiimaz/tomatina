<template>
  <div id="app">
    <md-toolbar>
    <h1 class="md-title" style="flex: 1">TOMATINA</h1>
    <md-button class="md-icon-button">
      <md-icon>more_vert</md-icon>
    </md-button>
  </md-toolbar>
  <md-layout md-gutter>
    <md-layout md-flex-xsmall="100" md-flex-small="50" md-flex-medium="33">
      <router-view :user="user"></router-view>
    </md-layout>
  </md-layout>
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
