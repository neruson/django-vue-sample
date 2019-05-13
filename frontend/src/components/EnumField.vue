<template>
  <select
    v-bind:value="value"
    v-on:input="$emit('input', $event.target.value)"
  >
    <option v-for="choice in choices" v-bind:key="choice">{{ choice }}</option>
  </select>
</template>

<script>
export default {
  'name': 'EnumField',
  'props': {
      'choices': Array
  },
}
</script>
