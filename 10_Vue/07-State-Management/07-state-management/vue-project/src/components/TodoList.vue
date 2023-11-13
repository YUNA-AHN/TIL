<template>
    <div>
        <TodoListItem
        v-for="todo in store.todos"
        :key="todo.id"
        :todo="todo"
        />
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import TodoListItem from '@/components/TodoListItem.vue';

const store = useCounterStore()

</script>

<style scoped>

</style>