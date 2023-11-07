<template>
  <div class="info">
    <h1>{{ msgInfo1 }}</h1>
    <div>{{ msgInfo2 }}</div>
    <img class="infoimg" src="@/assets/microphone.jpg" alt="" />
  </div>
</template>

<script setup>
import { ref } from "vue";
const msgInfo1 = ref("가수 정보 페이지에 오신 것을 환영합니다");
const msgInfo2 = ref(
  "여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요."
);
</script>

<style scoped>
.info {
  text-align: center;
}

.infoimg {
  width: 200px;
}
</style>
