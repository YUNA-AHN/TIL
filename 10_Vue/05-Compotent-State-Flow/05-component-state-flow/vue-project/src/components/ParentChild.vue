<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild :my-msg="myMsg" @update-name="updateName" />
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from "@/components/ParentGrandChild.vue";
// 1. 문자열 배열을 사용한 선언
// defineProps(["myMsg"]);

// 2. 객체 선언 방식
// defineProps({
//   myMsg: String,
// });

// 3. 다양한 객체 선언 방식
// defineProps({
//     // 유효성 검증을 위해 이렇게 작성하기도 한다!
//   myMsg: {
//     type: String,
//     required: true
//   }
// })

// props 데이터를 script에서 사용하려면
const props = defineProps({
  myMsg: String,
  dynamicProps: String,
});

console.log(props);
console.log(props.myMsg);

// emit 선언 방식
const emit = defineEmits(["someEvent", "emitArgs", "updateName"]);

const buttonClick = function () {
  emit("someEvent");
};

const emitArgs = function () {
  emit("emitArgs", 1, 2, 3);
};

const updateName = function () {
  emit("updateName");
};
</script>

<style scoped></style>
