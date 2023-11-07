<template>
  <div class="singerbox">
    <h2>{{ name }}</h2>
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
  width: 200px;
  border-radius: 50%;
}

.singerbox {
  border: 1px solid black;
}
</style>
