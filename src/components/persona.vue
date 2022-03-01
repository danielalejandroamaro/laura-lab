<template>
  <li style="display: flex; flex-direction: row; padding: 1em">
    <button @click="removeItem(persona.name)">remove</button>
    <div
      style="flex-grow: 1; padding-left: 1em"
      :style="[
        persona.sex == 'M'
          ? 'border: blue solid 2px'
          : 'border: pink solid  2px',
      ]"
    >
      {{ persona.name }} ({{ persona.sex }})
    </div>
  </li>
</template>
<script>
export default {
  props: ["persona"],
  methods: {
    removeItem(name) {
      this.$emit("removeItem", name);
    },
  },
};
</script>