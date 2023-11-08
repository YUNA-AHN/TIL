<template>
  <div class="child">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ childInfo.name }}</p>
    <p>나이 : {{ childInfo.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  childInfo: String,
});
</script>

<style scoped></style>
