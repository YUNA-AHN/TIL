<template>
  <div class="singer">
    <h1>{{ title }}</h1>
    <div class="singerlist">
      <SingerDetail v-for="singer in singerslist" />
    </div>
  </div>
</template>

<script setup>
import SingerDetail from "@/components/singers/SingerDetail.vue";
import { ref } from "vue";
const title = ref("가수 목록");
const singerslist = [
  { name: "adele" },
  { name: "maroon5" },
  { name: "Dua Lipa" },
];
</script>

<style scoped>
.singer {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.card {
  display: inline-block;
  width: 40%;
  margin: 20px;
  text-align: center;
}

.singerlist {
  width: 100%;
  text-align: center;
}

h1 {
  color: orangered;
}
</style>
