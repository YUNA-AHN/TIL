<template>
  <div>{{ store.count }}</div>
  <div>{{ count }}</div>
  <div>{{ doubleCount }}</div>
</template>

<script setup>
import { toRefs } from "vue";
import { storeToRefs } from "pinia";
import { useCounterStore } from "@/stores";

const info = ref({
  name: "홍길동",
  age: 20,
});

// 구조 분해 할당으로 반응형을 살리면서 가지고 오고 싶다...
const { name, age } = toRefs(info.value);

const store = useCounterStore();

store.increment();

// functions는 구조 분해 할당해도 됨
const { increment, decrement } = store;

// states, getters 에 대해서는 구조 분해 할당을 하게 되면 반응형이 언래핑된다...!
const { count, doubleCount } = storeToRefs(store);
</script>

<style scoped></style>