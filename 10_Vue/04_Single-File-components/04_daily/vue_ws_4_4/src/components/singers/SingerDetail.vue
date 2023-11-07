<template>
  <div class="singerbox card">
    <h1>{{ name }}</h1>
    <img class="singerimg" src="@/assets/singer.jpg" alt="" />
    <p>{{ description }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
const name = ref("가수 이름");
const description = ref("가수 소개글");
</script>

<style scoped>
.singerimg {
  width: 50%;
  border-radius: 50%;
}

.singerbox {
  border: 1px solid black;
}
</style>

<!-- <style>
h1 {
  color: green;
}
</style> -->
