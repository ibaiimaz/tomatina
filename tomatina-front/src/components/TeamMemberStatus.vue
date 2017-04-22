<template>
  <div>
    <pomodoro :stats="status"></pomodoro>
  </div>
</template>

<script>

  import Pomodoro from './Pomodoro';

  export default {
    name: 'team-member-status',
    props: ['status'],
    components: {
      Pomodoro
    },
    methods: {
    },
    data() {
      return {
      };
    }
  };

</script>

<style scoped>

</style>
