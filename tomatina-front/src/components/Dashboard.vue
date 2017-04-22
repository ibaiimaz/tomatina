<template>
  <div>
    Dashboard
    <div>
      {{ user.username }}
      <pomodoro user="user"></pomodoro>
    </div>
    <md-list>
      <md-list-item v-for="member in teamMembers">{{ member.name }}</md-list-item>
    </md-list>

  </div>
</template>

<script>
  import Pomodoro from './Pomodoro';

  import TeamService from '../services/team.service';

  export default {
    name: 'dashboard',
    props: ['user'],
    components: {
      Pomodoro
    },
    methods:{

    },
    data() {
      return {
        teamMembers: []
      };
    },
    created() {
      TeamService.getTeam().then(
        (members) => { this.teamMembers = members; }
      );
    }
  };

</script>

<style scoped>

</style>
