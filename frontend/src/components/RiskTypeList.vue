<template>
  <div id="mylist">
    <div v-for="riskType in riskTypes" v-bind:key="riskType.id">
      <p v-on:click="clickType(riskType.id)">{{ riskType.name }}</p>
      <RiskTypeForm
        v-if="selectedType === riskType.id"
        v-bind:riskType="riskType"
      ></RiskTypeForm>
    </div>
  </div>
</template>

<script>
import RiskTypeForm from './RiskTypeForm.vue'

export default {
  name: 'RiskTypeList',
  components: {
      RiskTypeForm
  },
  data() {
    return {
      'riskTypes': [
        {
          'id': 1,
          'name': 'test type',
          'fields': [
            {
              'name': 'Field1',
              'type': 'text'
            },
            {
              'name': 'Field2',
              'type': 'date'
            }
          ]
        },
        {
          'id': 2,
          'name': 'test type2',
          'fields': [
            {
              'name': 'Field2',
              'type': 'text'
            },
            {
              'name': 'Field3',
              'type': 'number'
            },
            {
              'name': 'Beverage',
              'type': 'enum',
              'choices': ['Coffee', 'Tea', 'Water']
            }
          ]
        }
      ],
      'selectedType': null
    }
  },
  methods: {
    clickType(id) {
      this.selectedType = id;
    }
  }
}
</script>
