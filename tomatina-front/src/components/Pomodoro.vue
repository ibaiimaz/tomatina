<template>
  <div>
    <span v-if="stats">{{ remaining }}</span>
  </div>
</template>

<script>
  import moment from 'moment';

  const getTimeDifference = (stats) => {
    const diff = moment(moment(stats.finish).diff(moment()));

    return moment(diff).format('mm:ss');
  };

  export default {
    name: 'pomodoro',
    props: ['stats'],
    // methods:{

    // },
    data() {
      return {
        remaining: ''
      };
    },
    created() {
      if (!this.stats.isFinished()) {
        setInterval(() => {
          this.remaining = getTimeDifference(this.stats);
        }, 1000);
      }
    }
  };

</script>

<style scoped>

</style>
