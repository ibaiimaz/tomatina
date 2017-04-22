<template>
  <div>
    <div>{{status.name}}</div>

    <div v-if="status.status == 'working'">
      <md-icon class="md-primary">build</md-icon>
    </div>
    <div v-else>
      <md-icon class="md-primary">pan_tool</md-icon>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'team-member-status',
    props: ['status'],
    components: {
    },
    methods: {

    },
    data() {
      return {
      };
    }
  };

</script>

<style scoped>

</style>
