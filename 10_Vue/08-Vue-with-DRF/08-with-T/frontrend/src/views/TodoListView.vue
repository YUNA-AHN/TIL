<template>
    <div>
        <h1>Todo</h1>
    <div v-for="todo in todos" :key="todo.id">
      {{ todo.title }} - {{ todo.description }}
      <hr />
    </div>
    </div>
</template>

<script setup>
const todos = ref([]);

axios({
  url: "http://127.0.0.1:8000/api/v1/todos/",
  method: "GET",
}).then((response) => {
  const data = response.date;
  todos.value = data;
});
</script>

<stylescoped>

</style>