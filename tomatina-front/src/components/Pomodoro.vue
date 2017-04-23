<template>
  <div>
    <md-card>
        <md-card-header>
          <md-icon :class="getImageSize(size)">account_box</md-icon>
          <md-card-header-text>
            <div class="md-subhead" v-if="stats">{{stats.name}}</div>
            <countdown :stats="stats" v-if="stats"
              class="countdown"></countdown>
            <div v-if="stats && stats.status == 'working'">
              <md-icon>alarm_on</md-icon>
            </div>
            <div v-if="stats && stats.status == 'resting'">
              <md-icon>alarm_off</md-icon>
            </div>
            <div v-else="stats && stats.status == 'resting'">
              <md-icon>alarm</md-icon>
            </div>
            <div class="md-subhead" >{{stats.status}}</div>
          </md-card-header-text>
        </md-card-header>
        <md-card-actions>
           <div v-if="stats.isFirstPomodoro">
             Start working!
           </div>
            <div v-if="canStart()">
              <md-button v-on:click.native="startPomodoro">Start</md-button>
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

  import PomodoroService from '../services/pomodoro.service';

  const getImageSize = (size) => { return size == 's' ? 'md-size-2x' : 'md-size-4x' };
  const getFontSize = (size) => { return size == 's' ? 'small' : 'normal' };

  export default {
    name: 'pomodoro',
    props: ['stats', 'size'],
    data() {
      return {
        remaining: '',
        canStart: () => !this.stats || this.stats.hasExpired() || this.stats.isFirstPomodoro,
        getImageSize: getImageSize,
        getFontSize: getFontSize
      };
    },
    methods: {
      startPomodoro: () => {
        PomodoroService.createPomodoro();
      }
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
  .countdown{
    margin: 10px 0;
  }

</style>

