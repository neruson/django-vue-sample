<template>
  <div class="row">
    <label class="col-md-3">{{ field.name }}</label>
    <div class="col-md-9">
      <TextField v-if="field.field_type === 'text'" v-model="value"></TextField>
      <NumberField v-else-if="field.field_type === 'number'" v-model="value"></NumberField>
      <Datepicker v-else-if="field.field_type === 'date'" v-model="value"></Datepicker>
      <EnumField
        v-else-if="field.field_type === 'enum'"
        v-model="value"
        v-bind:options="field.options"
      ></EnumField>
    </div>
  </div>
</template>

<script>
import TextField from "./TextField.vue";
import NumberField from "./NumberField.vue";
import Datepicker from "vuejs-datepicker";
import EnumField from "./EnumField.vue";

export default {
  name: "CustomField",
  components: {
    TextField,
    NumberField,
    Datepicker,
    EnumField
  },
  data() {
    return {
      value: null
    };
  },
  props: {
    field: Object
  }
};
</script>

<style scoped>
</style>
