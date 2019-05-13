<template>
  <div id="app">
    <RiskTypeList></RiskTypeList>
  </div>
</template>

<script>
import RiskTypeList from './components/RiskTypeList.vue'

export default {
  name: 'app',
  components: {
    RiskTypeList
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 30px;
}
</style>
