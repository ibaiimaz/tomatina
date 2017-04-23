<template>
  <div>
    <md-card>
        <md-card-header>
          <md-icon :class="getImageSize(size)">account_box</md-icon>
          <md-card-header-text>
            <countdown :stats="stats" v-if="stats"></countdown>
            <div class="md-subhead" v-if="stats">Status</div>
          </md-card-header-text>
        </md-card-header>
        <md-card-actions>
            <div v-if="isFinished()">
              <md-button>Start</md-button>
            </div>
            <div v-else>
              <md-button>Stop</md-button>
            </div>
        </md-card-actions>
      </md-card>
  </div>
</template>

<script>
  import moment from 'moment';

  import Countdown from './Countdown';

  const getImageSize = (size) => { return size == 's' ? 'md-size-2x' : 'md-size-4x' };
  const getFontSize = (size) => { return size == 's' ? 'small' : 'normal' };

  export default {
    name: 'pomodoro',
    props: ['stats', 'size'],
    data() {
      return {
        remaining: '',
         isFinished: () => this.stats && this.stats.finish.isBefore(moment()),
         getImageSize: getImageSize,
        getFontSize: getFontSize
      };
    },
    created() {

    },
    components: {
      Countdown
    },
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

