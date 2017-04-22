<template>
  <div>
    Dashboard
    <div>
      {{ user.username }}
      <pomodoro user="user"></pomodoro>
    </div>
    <md-list>
      <md-list-item v-for="status in teamMembers">
        <team-member-status :status="status"></team-member-status>
      </md-list-item>
    </md-list>

  </div>
</template>

<script>
  import Pomodoro from './Pomodoro';
  import TeamMemberStatus from './TeamMemberStatus';

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
        teamMembers: []
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
