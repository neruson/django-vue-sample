<template>
  <input
    type="number"
    v-bind:value="value"
    v-on:input="$emit('input', $event.target.value)"
  >
</template>

<script>
export default {
  'name': 'NumberField',
  'props': {
      'value': Number
  },
}
</script>
