<template>
  <div>
      {{status.name}}
      {{status.status}}
      {{status.start}}
  </div>
</template>

<script>

  export default {
    name: 'team-member-status',
    props: ['status'],
    components: {
    },
    methods:{

    },
    data() {
      return {
      };
    }
  };

</script>

<style scoped>

</style>
