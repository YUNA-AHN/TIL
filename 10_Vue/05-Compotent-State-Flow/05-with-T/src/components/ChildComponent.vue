<template>
  <div>
    {{ myPhone }}
    <button v-on:click="buttonClick">버튼 클릭</button>
  </div>
</template>

<script setup>
import { computed } from "vue";
const props = defineProps({
  // 1. 객체 형태로 props를 선언 (권장)
  message: String,
});
console.log(props);
console.log(props.message);
// const myString = '메시지 : ' + props.message

// computed, watch <----
// const myString = computed(() => {
//   return '메시지 : ' + props.message
// })

const myPhone = computed(() => {
  return (
    props.message.substring(0, 3) +
    "-" +
    props.message.substring(3, 7) +
    "-" +
    props.message.substring(7)
  );
});

// 상위 컴포넌트에게 이벤트를 전달..
const emit = defineEmits(["myEvent"]);
const buttonClick = function () {
  emit("myEvent");
};

//  Props 유효성 검사
// import { computed } from 'vue'
// const props = defineProps({
//   // 1. 문자열 형태로 데이터 전달
//   message: String
//   // 2. 여러 타입으로 데이터 전달
//   propA : [String, Number],
//   // 3. 해당 props를 반드시 받아야하는 경우 명시
//   propB : {
//      type: String,
//      required: true // 반드시 전달받아야하는 값임을 명시
//   },
//   // 4. 기본값을 명시
//   propC : {
//      type: Number,
//      default: 100
//   },
//   // 5. 유효성 검사를 데이터를 검증
//   propD: {
//      validator(value) {
// 			   return value.includes("SSAFY")
// 		 }
//   }
// })

// Emits 유효성 검사
// const emit = defineEmits({
//    /* null 인 경우에 유효성 검사 x */
//    click: null,
//    myEvent: function(value){
//      if (value !== ""){
// 	     // 비어있는 문자열이 아닌 경우 유효성 OK!
//        return true;
//      }
// 		 return false; // 유효성 실패...
//    }
//   // submit 이벤트 유효성 검사
//   submit: ({ email, password }) => {
//     if (email && password) {
//       return true
//     } else {
//       console.warn('submit 이벤트 페이로드가 옳지 않음!')
//       return false
//     }
//   }
// })

// emit('myEvent', ''); // 유효성 검사 실패 (이벤트 상위 X)
// emit('myEvent', '안녕!"); // 유효성 검사 성공! (이벤트 상위 O)

// const submitForm = function(email, password) {
//   emit('submit', { email, password })
// }

// defineProps(['message']) // 2. 문자열 배열 형태로 props 선언
</script>

<style scoped></style>
