<template>
  <div>
    <li>{{ msg }}</li>
    <!-- <li>{{ props.singer }}</li> -->
  </div>
</template>

<script setup>
const props = defineProps(["singer"]);
const msg = props.singer;
</script>

<style scoped></style>
