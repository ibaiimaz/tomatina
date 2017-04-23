<template>
  <div>
    <div class="md-title" v-if="!isFinished()">{{ remaining }}</div>
    <audio ref="audio" src="/static/Sound-of-a-peacock.mp3"></audio>
  </div>
</template>

<script>
  import moment from 'moment';

  let interval;

  const checkIfIsJustExpired = (stats) => {
    const start = moment();
    const finish = stats.finish;
    const diff = moment(finish.diff(start));
    const remainingSeconds = parseInt(diff/1000, 10);

    return (remainingSeconds === 0);
  };

  const getTimeDifference = (stats) => {
    let isPast = false;
    let start = moment();
    let finish = stats.finish;
    if (!finish) {
      return;
    }
    if (finish.isBefore(start)) {
      isPast = true;
      start = stats.finish;
      finish = moment();
    }

    return (isPast)? '' : `${moment(finish.diff(start)).format('mm:ss')}`;
  };

  export default {
    name: 'countdown',
    props: ['stats', 'audio'],
    data() {
      return {
        remaining: '',
         isFinished: () => !this.stats || this.stats.hasExpired(),
         play: false
      };
    },
    created() {
      if (!!this.stats && !this.stats.isFinished()) {
        interval = setInterval(() => {
          this.remaining = getTimeDifference(this.stats);
          if (this.audio && checkIfIsJustExpired(this.stats)) {
            this.$refs.audio.play();
          }
        }, 1000);
      }
    },
    destroyed() {
      clearInterval(interval);
    }
  };

</script>

<style scoped>
  .md-title {
    font-size: 3em;
  }

</style>

