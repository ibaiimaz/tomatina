<template>
  <div>
    <md-card>
        <md-card-header>
          <md-icon class="md-size-4x">account_box</md-icon>
          <md-card-header-text>
            <div class="md-title" style="font-size: 3em" v-if="stats">{{ remaining }}</div>
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

