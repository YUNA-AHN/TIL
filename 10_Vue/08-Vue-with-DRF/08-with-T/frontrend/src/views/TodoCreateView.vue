<template>
  <div>
    <h1>CREATE</h1>
    <form>
      <div>
        <label for="title">제목 : </label>
        <input type="text" id="title" name="title" />
      </div>
      <div>
        <label for="description">내용 : </label>
        <input type="text" id="description" name="description" />
      </div>

      <button>CREATE</button>
    </form>
    <RouterLink :to="{ name: 'todo-list' }">[BACK]</RouterLink>
  </div>
</template>

<script setup>
import { ref } from "vue";

const title = ref("");
const description = ref("");
const creatTodo = function () {
  const data = {
    title: title.value,
    description: description.value,
  };
  axios({
    url: "/api/v1/todos",
    method: "POST",
    data: data,
  }).then();
};
</script>

<style scoped></style>
