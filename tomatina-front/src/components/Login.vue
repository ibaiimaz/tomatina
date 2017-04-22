<template>
  <form>
    <md-input-container>
      <label>Login</label>
      <md-input type="text" v-model="user.username" />
    </md-input-container>

    <md-input-container>
      <label>Passowrd</label>
      <md-input type="password" v-model="password"/>
    </md-input-container>
    <div>
      <md-button class="md-raised" v-on:click.native="doLogin"> login </md-button>
    </div>
  </form>
</template>

<script>
  export default {
    name: 'login',
    methods:{
      doLogin: function(){
        this.$router.push('/dashboard')
      }
    },
    props: ['user'],
    data() {
      return {
        password: ''
      };
    },
  };

</script>

<style scoped>

</style>
