<template>
  <div class="business-card-detail">
    <h4>이름 : {{ name }}</h4>
    <p>직함 : {{ title }}</p>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  title: String,
});
</script>

<style scoped>
.business-card-detail {
  background-color: #f9f9f9;
  border: 1px solid lightgrey;
  margin: 20px;
  width: 40%;
}
</style>
