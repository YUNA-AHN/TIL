<template>
  <div>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }} 유저의 페이지 입니다.</h2>
    <h2>{{ userID }} 유저의 페이지 입니다.</h2>
    <button @click="goHome">홈으로!</button>
    <button @click="goAnotherUser">100번 유저 페이지로!</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import {
  useRoute,
  useRouter,
  onBeforeRouteLeave,
  onBeforeRouteUpdate,
} from "vue-router";

const route = useRoute();
const userID = ref(route.params.id);

// 프로그래밍 방식 네비게이션
const router = useRouter();
const goHome = function () {
  // router.push({ name: "home" });
  router.replace({ name: "home" });
};

// In-component guard
// 1. onBeforeRouteLeave
onBeforeRouteLeave((to, from) => {
  const answer = window.confirm("정말 떠나실 건가요?");
  if (answer === false) {
    return false;
  }
});

// 2.
// onBeforeRouteUpdate
const goAnotherUser = function () {
  router.push({ name: "user", params: { id: 100 } });
};

onBeforeRouteUpdate((to, from) => {
  userID.value = to.params.id;
});
</script>

<style scoped></style>
