<template>
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo : {{ store.TodosCount }}</h2>
    <TodoList/>
    <TodoForm/>
</div>
</template>

<script setup>
import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()


</script>

<style scoped>
</style>
