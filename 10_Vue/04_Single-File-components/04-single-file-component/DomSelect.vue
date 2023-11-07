<template>
  <div>
    <input type="text" ref="ssafy" />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const ssafy = ref();

onMounted(() => {
  console.log(ssafy.value);
});
</script>

<style lang="scss" scoped></style>
