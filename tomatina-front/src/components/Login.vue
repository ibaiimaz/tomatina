<template>
  <div>
    <div>
      <label>Login</label>
      <input type="text" v-model="login" />
    </div>

    <div>
      <label>Passowrd</label>
      <input type="password" v-model="password"/>
    </div>
    <div>
      <button v-on:click="doLogin"> login </button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'login',
    methods:{
      doLogin: function(){
        this.$router.push('/dashboard')
      }
    },
    data() {
      return {
        login: '',
        password: ''
      };
    },
  };

</script>

<style scoped>

</style>