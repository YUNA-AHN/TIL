<template>
  <div class="business-card-detail">
    <h4>이름 : {{ card.name }}</h4>
    <p>직함 : {{ card.title }}</p>
    <button @click="deleteCardFunc">명함 삭제</button>
  </div>
</template>

<script setup>
// defineProps({
//   card: Object,
// });

const emit = defineEmits(["deleteCardEvent"]);
const props = defineProps({
  card: Object,
});

const deleteCardFunc = function () {
  emit("deleteCardEvent", props.card);
};
</script>

<style scoped>
.business-card-detail {
  background-color: #f9f9f9;
  border: 1px solid lightgrey;
  margin: 20px;
  padding: 10px;
  width: 40%;
}
</style>
