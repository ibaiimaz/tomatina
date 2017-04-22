<template>
  <div>
    Dashboard
    <div>
      {{ user.username }}
      <pomodoro :stats="stats"></pomodoro>
    </div>
    <md-list>
      <md-list-item v-for="status in teamMembers" :key="status.name">
        <team-member-status :status="status"></team-member-status>
      </md-list-item>
    </md-list>

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
    methods:{

    },
    data() {
      return {
        teamMembers: [],
        stats: new UserStats({start: moment().subtract(15, 'minute')})
      };
    },
    created() {
      TeamService.getTeamStats().then(
        (members) => { this.teamMembers = members; }
      );
    }
  };

</script>

<style scoped>

</style>
