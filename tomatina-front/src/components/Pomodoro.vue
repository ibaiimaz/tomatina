<template>
  <div>
    <md-card>
        <md-card-header>
          <md-icon class="md-size-4x">account_box</md-icon>
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

  export default {
    name: 'pomodoro',
    props: ['stats'],
    data() {
      return {
         isFinished: () => this.stats && this.stats.finish.isBefore(moment())
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


</style>

