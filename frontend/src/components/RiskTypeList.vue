<template>
  <div class="container" id="mylist">
    <h2>Risk Types</h2>
    <div class="card" v-for="riskType in riskTypes" v-bind:key="riskType.id">
      <h3 class="card-header" v-on:click="clickType(riskType.id)">
        <span
          v-bind:class="['fa', selectedType === riskType.id ? 'fa-angle-down' : 'fa-angle-right']"
        ></span>
        {{ riskType.name }}
      </h3>
      <RiskTypeForm v-if="selectedType === riskType.id" v-bind:riskType="riskType"></RiskTypeForm>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import RiskTypeForm from "./RiskTypeForm.vue";

export default {
  name: "RiskTypeList",
  components: {
    RiskTypeForm
  },
  data() {
    return {
      riskTypes: [],
      selectedType: null
    };
  },
  methods: {
    clickType(id) {
      if (this.selectedType !== id) {
        this.selectedType = id;
      } else {
        this.selectedType = null;
      }
    }
  },
  mounted() {
    axios.get("/api/risks/").then(response => (this.riskTypes = response.data));
  }
};
</script>

<style scoped>
.card {
  margin-bottom: 5px;
}
</style>
