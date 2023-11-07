<template>
  <div>
    <!-- 카운트 버튼 -->
    <div>
      <button @click="incremnt">count : {{ count }}</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
const count = ref(0);
const incremnt = function () {
  count.value++;
};
</script>

<style scoped></style>
