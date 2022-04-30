<template>
  <div id="page">
    <h1>Configurations</h1>
    <ConfigForm/>
  </div>
</template>

<script>
import ConfigForm from '@/components/ConfigForm.vue';

export default {
  name: 'ConfigView',
  components: {
    ConfigForm,
  },
};
</script>
