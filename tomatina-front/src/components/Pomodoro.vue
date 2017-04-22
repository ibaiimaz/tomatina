<template>
  <div>
    <md-card>
        <md-card-header>
          <md-icon :class="getImageSize(size)">account_box</md-icon>
          <md-card-header-text>
            <div class="md-title" style="font-size: 3em" v-if="stats && !isFinished()">{{ remaining }}</div>
            <div class="md-subhead" v-if="stats">Status</div>
          </md-card-header-text>
        </md-card-header>

        <md-card-actions>
          <md-button>Action</md-button>
          <md-button>Action</md-button>
        </md-card-actions>
      </md-card>
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

  const getImageSize = (size) => { return size == 's' ? 'md-size-2x' : 'md-size-4x' };
  const getFontSize = (size) => { return size == 's' ? 'small' : 'normal' };

  export default {
    name: 'pomodoro',
    props: ['stats', 'size'],
    data() {
      return {
        remaining: '',
         isFinished: () => this.stats.finish.isBefore(moment()),
         getImageSize: getImageSize,
        getFontSize: getFontSize
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
  .normal {
    font-size: 3em;
  }
  .small {
    font-size: 1.5em;
  }

</style>

