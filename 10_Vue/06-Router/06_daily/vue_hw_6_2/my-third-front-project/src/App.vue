<script setup>
import { RouterLink, RouterView } from "vue-router";
import MainPage from "./components/MainPage.vue";
</script>

<template>
  <header>
    <div>
      <MainPage />
      <nav>
        <RouterLink :to="{ name: 'some' }">Some</RouterLink>
        |
        <RouterLink :to="{ name: 'other' }">Other</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style scoped></style>

