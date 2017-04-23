<template>
  <div>
    <h2>Dashboard</h2>
    <md-layout md-gutter md-align="center">
      <md-layout md-flex-xsmall="100" md-flex-small="50" md-flex="25">
        <pomodoro :stats="user.stats"></pomodoro>
      </md-layout>
      <md-layout md-flex-xsmall="100" md-flex-small="50" md-flex="50">
        <div>
          <h3>Your teams</h3>
        </div>
        <md-list>
          <md-list-item v-for="team in teams" :key="team.id">
            <router-link :to="{ name: 'Team', params: { teamId: team.id }}">{{team.name}}</router-link>
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
    methods: {

    },
    data() {
      return {
        teams: []
      };
    },
    created() {
      TeamService.getUserTeams(this.user.username).then(
        (teams) => { this.teams = teams; }
      );
      // UserStatsService.getUserStats().then(
      //   (stats) => { this.stats = stats; }
      // );
    }
  };

</script>

<style scoped>

</style>
