<template>
  <div>
    <h2>Dashboard</h2>
    <md-layout md-gutter md-align="center">
      <md-layout md-flex-xsmall="100" md-flex-small="50" md-flex="25">
        <pomodoro :stats="user.stats" :userid="user.id" :audio="true"></pomodoro>
      </md-layout>
      <md-layout md-flex-xsmall="100" md-flex-small="50" md-flex="30">
        <md-list class="collection">
          <div class="header">Your teams</div>
          <md-list-item class="collection-item" v-for="team in teams" :key="team.id">
            <md-icon>group</md-icon> <span>
            <router-link :to="{ name: 'Team', params: { teamId: team.id }}">{{team.name}}</router-link></span>
          </md-list-item>
        </md-list>
      </md-layout>
    </md-layout>
  </div>
</template>

<script>
  import moment from 'moment';

  import Pomodoro from './Pomodoro';
  import TeamMemberStatus from './TeamMemberStatus';

  import UserStats from '../models/userStats';

  import TeamService from '../services/team.service';
  import UserStatsService from '../services/user-stats.service';

  export default {
    name: 'dashboard',
    props: ['user'],
    components: {
      Pomodoro,
      TeamMemberStatus
    },
    data() {
      return {
        teams: []
      };
    },
    created() {
      // this.user.stats = new UserStats({});
      UserStatsService.getUserStats(this.user.id)
        .then(
          (stats) => {
            this.user.stats = stats;
            this.user = this.user;
          }
        );
      TeamService.getUserTeams()
        .then(
          (teams) => {  this.teams = teams; }
        );
    }
  };

</script>

<style scoped>
  .teams-list {
    border: 1px solid rgba(0,0,0,.12);
  }
  .collection {
    border: 1px solid #e0e0e0;
    border-radius: 2px;
    overflow: hidden;
    position: relative;
  }
  .collection .header {
    text-align: center;
  }
</style>
