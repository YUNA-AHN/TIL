<template>
  <div class="parents">
    <h1>부모 페이지입니다.</h1>
    <div v-for="child in children">
      <ChildPage :child-info="child" />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import ChildPage from "@/components/ChildPage.vue";
const children = ref([
  {
    name: "김하나",
    age: 30,
  },
  {
    name: "김두리",
    age: 20,
  },
  {
    name: "김서이",
    age: 10,
  },
]);
</script>

<style scoped>
.child {
  border: 1px solid lightgray;
  padding: 1%;
  margin: 1%;
}
</style>
