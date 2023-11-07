<template>
  <div class="singerbox card">
    <h1>{{ name }}</h1>
    <img class="singerimg" src="@/assets/singer.jpg" alt="" />
    <p>{{ description }}</p>
    <SingerAlbum />
    <SingerAlbum />
  </div>
</template>

<script setup>
import { ref } from "vue";
import SingerAlbum from "./SingerAlbum.vue";
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

.albumcard {
  display: inline-block;
  width: 40%;
  margin: 10px;
  background-color: ivory;
  border: 1px soild lightgray;
  border-radius: 20%;
}
</style>

<!-- <style>
h1 {
  color: green;
}
</style> -->
