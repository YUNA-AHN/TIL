<template>
  <div>
    <!-- 속성값을 통해서 자식 컴포넌트에게 데이터를 넘겨줄 수 있음 = props -->
    <!-- 정적인 방식의 props 데이터 전달 -->
    <ChildComponent message="안녕하세요!" v-on:my-event="emitButtonClick" />
    <!-- 동적인 방식의 props 데이터 전달 -->
    <ChildComponent v-bind:message="myMsg" @my-event="emitButtonClick" />
    <input type="text" v-model="myMsg" />
  </div>
</template>

<script setup>
import { ref } from "vue";
import ChildComponent from "./components/ChildComponent.vue";

const myMsg = ref("누구세요?");
const emitButtonClick = function () {
  alert("클릭되었어요!");
};
</script>

<style lang="scss" scoped></style>
