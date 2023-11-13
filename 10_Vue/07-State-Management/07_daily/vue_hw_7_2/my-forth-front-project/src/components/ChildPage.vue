<template>
  <div class="child-card">
    <h1>자식 페이지</h1>
    <div>{{ child.name }}</div>
  </div>
</template>

<script setup>
defineProps({
  child: Object,
});

// console.log(childprops);
</script>

<style scoped>
.child-card {
  border: 1px solid lightgray;
  margin: 10px;
  background-color: white;
}
</style>
