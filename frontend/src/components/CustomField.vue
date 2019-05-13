<template>
  <div>
    <label >{{ field.name }}</label>
    <div>
      <TextField
        v-if="field.type === 'text'"
        v-model="value">
      </TextField>
      <NumberField
        v-else-if="field.type === 'number'"
        v-model="value">
      </NumberField>
      <Datepicker
        v-else-if="field.type === 'date'"
        v-model="value">
      </Datepicker>
      <EnumField
        v-else-if="field.type === 'enum'"
        v-model="value"
        v-bind:choices="field.choices">
      </EnumField>
    </div>
  </div>
</template>

<script>
import TextField from './TextField.vue'
import NumberField from './NumberField.vue'
import Datepicker from 'vuejs-datepicker'
import EnumField from './EnumField.vue'

export default {
  name: 'CustomField',
  components: {
      TextField,
      NumberField,
      Datepicker,
      EnumField
  },
  data() {
    return {
      'value': null
    }
  },
  props: {
    field: Object
  }
}
</script>

<style scoped>
</style>
