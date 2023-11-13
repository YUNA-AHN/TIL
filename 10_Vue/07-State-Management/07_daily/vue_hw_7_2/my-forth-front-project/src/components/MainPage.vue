<template>
  <div>
    <h1>pinia 연습하기</h1>
    <ParentPage v-for="family in store.familyinfo" :family="family" />
  </div>
</template>

<script setup>
import { useFamilyStore } from "@/stores/family";
import ParentPage from "@/components/ParentPage.vue";

const store = useFamilyStore();
</script>

<style scoped></style>
