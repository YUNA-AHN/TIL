<template>
  <div>
    <!-- 카운트 버튼 -->
    <div>
      <input ref="myInput" />
      <ListComponent />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import ListComponent from "@/components/ListComponent.Vue";

const myInput = ref(null);
console.log(myInput.value);
</script>

<style scoped></style>

