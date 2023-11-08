<template>
  <div class="app">
    <header class="header">
      <h1>명함 관리 페이지</h1>
    </header>
    <main class="main">
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </main>
    <article class="article">
      <BusinessCard />
    </article>
    <footer class="footer">
      <p>&copy; 2023 My Business Cards</p>
    </footer>
  </div>
</template>

<script setup>
import BusinessCard from "./components/BusinessCard.vue";
</script>

<style scoped>
.app {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  width: 300px;
  background-color: #007acc;
  color: white;
  height: 80px;
}

.main {
}

.article {
  justify-content: center;
}

.footer {
  background-color: #f0f0f0;
  width: 100%;
  height: 60px;
  text-align: center;
  position: fixed;
  bottom: 0;
}
</style>
