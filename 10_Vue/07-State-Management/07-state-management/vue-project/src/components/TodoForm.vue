<template>
    <div>
        <form @submit.prevent="createTodo()" ref="formElem">
            <input type="text" v-model="todoText">
            <input type="submit">
        </form>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import {ref} from 'vue'

const todoText = ref('')
const store = useCounterStore()

const forElem = ref(null)

// v-model이 있어서 굳이 인자 넣어주지 않아도 된당
const createTodo = function () {
    store.addTodo(todoText.value)
    forElem.value.reset()
    todoText.value=''
}

</script>

<style scoped>

</style>