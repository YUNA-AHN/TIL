<template>
  <div class="parent-card">
    <h1>부모 컴포넌트</h1>
    <div>{{ props.family.father }}</div>
    <div>{{ props.family.mother }}</div>
    <ChildPage v-for="child in children" :child="child" />
  </div>
</template>

<script setup>
import ChildPage from "@/components/ChildPage.vue";
const props = defineProps({
  family: Object,
});

const children = props.family.children;

// console.log(children);
</script>

<style scoped>
.parent-card {
  border: 1px solid gray;
  text-align: center;
  background-color: #f9f9f9;
  margin: 10px;
}
</style>
