<template>
  <ul>
    <ListComponentItem singer="아이유" />
    <ListComponentItem v-bind:singer="name" />
    <ListComponentItem singer="10cm" />
  </ul>
</template>

<script setup>
import { ref } from "vue";
import ListComponentItem from "@/components/ListComponentItem.vue";
const name = ref("유후앤아하");
</script>

<style scoped></style>
