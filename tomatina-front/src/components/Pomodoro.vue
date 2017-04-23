<template>
  <div>
    <md-card>
        <md-card-header>
          <md-icon :class="getImageSize(size)">account_box</md-icon>
          <md-card-header-text>
            <div class="md-subhead" v-if="stats">{{stats.name}}</div>
            <countdown class="countdown" :stats="stats" v-if="stats"></countdown>
            <div v-if="stats && stats.status == 'working'">
              <md-icon class="md-primary">alarm_on</md-icon>
            </div>
            <div v-else>
              <md-icon class="md-warn">alarm_off</md-icon>
            </div>
          </md-card-header-text>
        </md-card-header>
        <md-card-actions>
            <div v-if="isFinished()">
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
        isFinished: () => !this.stats || this.stats.hasExpired(),
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
  .countdown {
    margin: 10px 0;
  }

</style>

