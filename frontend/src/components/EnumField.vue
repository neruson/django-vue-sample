<template>
  <select v-bind:value="value" v-on:input="$emit('input', $event.target.value)">
    <option v-for="option in options" v-bind:key="option.value">{{ option.value }}</option>
  </select>
</template>

<script>
export default {
  name: "EnumField",
  props: {
    options: Array
  }
};
</script>
