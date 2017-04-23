<template>
  <div>
    <div class="md-title" v-if="stats && !isFinished()">{{ remaining }}</div>
  </div>
</template>

<script>
  import moment from 'moment';

  const getTimeDifference = (stats) => {
    let isPast = false;
    let start = moment();
    let finish = stats.finish;
    if (finish.isBefore(start)) {
      isPast = true;
      start = stats.finish;
      finish = moment();
    }

    return `${(isPast)? '-' : ''}${moment(finish.diff(start)).format('mm:ss')}`;
  };

  export default {
    name: 'countdown',
    props: ['stats'],
    data() {
      return {
        remaining: '',
         isFinished: () => this.stats && this.stats.finish.isBefore(moment())
      };
    },
    created() {
      if (!!this.stats && !this.stats.isFinished()) {
        setInterval(() => {
          this.remaining = getTimeDifference(this.stats);
        }, 1000);
      }
    }
  };

</script>

<style scoped>
  .md-title {
    font-size: 3em;
  }

</style>

