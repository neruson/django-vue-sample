<template>
  <div class="card-body">
    <CustomField v-for="field in riskType.fields" v-bind:key="field.id" v-bind:field="field"></CustomField>
    <input type="submit" value="Submit">
  </div>
</template>

<script>
import CustomField from "./CustomField.vue";

export default {
  name: "RiskTypeForm",
  components: {
    CustomField
  },
  props: {
    riskType: Object
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
