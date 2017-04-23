<template>
  <div>
    Dashboard
    <md-layout md-gutter md-align="center">
      <md-layout md-flex-xsmall="100" md-flex-small="50" md-flex="25">
        <pomodoro :stats="stats"></pomodoro>
      </md-layout>
      <md-layout md-flex-xsmall="100" md-flex-small="50" md-flex="50">
        <!--<md-list>
          <md-list-item v-for="status in teamMembers" :key="status.name">
            <team-member-status size="s" :status="status"></team-member-status>
          </md-list-item>
        </md-list>-->
        <md-list class="collection">
          <md-header class="header">Your teams</md-header>
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
        teams: [],
        stats: new UserStats({ start: moment().subtract(15, 'minute') })
      };
    },
    created() {
      TeamService.getUserTeams(this.user.username).then(
        (teams) => { this.teams = teams; }
      );
    }
  };

</script>

<style scoped>
  .teams-list {
    border: 1px solid rgba(0,0,0,.12);
  }
  .collection {
    margin: 0.5rem 0 1rem 0;
    border: 1px solid #e0e0e0;
    border-radius: 2px;
    overflow: hidden;
    position: relative;
  }
  .collection .header {
    text-align: center;
  }
</style>
