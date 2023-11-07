<template>
  <div class="singer">
    <h1>{{ title }}</h1>
    <SingerDetail />
  </div>
</template>

<script setup>
import SingerDetail from "@/components/singers/SingerDetail.vue";
import { ref } from "vue";
const title = ref("가수 목록");
</script>

<style scoped>
.singer {
  text-align: center;
}
</style>
