<template>
  <div>
    <h2>Team</h2>
    <md-layout md-gutter md-align="center">
      <md-layout md-flex-xsmall="100" md-flex-small="50" md-flex="50">
        <md-list>
          <md-list-item v-for="status in teamMembers" :key="status.name">
            <team-member-status :status="status"></team-member-status>
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

  import UserStatsService from '../services/user-stats.service';

  export default {
    name: 'team',
    props: ['user'],
    components: {
      Pomodoro,
      TeamMemberStatus
    },
    methods:{

    },
    data() {
      return {
        teamMembers: [],
        stats: new UserStats({start: moment().subtract(15, 'minute')})
      };
    },
    created() {
      UserStatsService.getTeamStats().then(
        (members) => { this.teamMembers = members; }
      );
    }
  };

</script>

<style scoped>

</style>
