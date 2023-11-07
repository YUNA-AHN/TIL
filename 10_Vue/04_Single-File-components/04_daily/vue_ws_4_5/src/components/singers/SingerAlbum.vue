<template>
  <div class="albumcard">
    <h3>{{ albumtitle }}</h3>
    <div class="song">
      <p>{{ albumsong1 }}</p>
      <p>{{ albumsong2 }}</p>
      <p>{{ albumsong3 }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
const albumtitle = ref("앨범 제목");
const albumsong1 = ref("노래 목록 1");
const albumsong2 = ref("노래 목록 2");
const albumsong3 = ref("노래 목록 3");
</script>

<style scoped>
.song {
  color: coral;
}
</style>
