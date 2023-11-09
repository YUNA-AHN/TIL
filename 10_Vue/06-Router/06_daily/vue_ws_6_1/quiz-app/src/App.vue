<template>
  <div class="app">
    <div class="header">
      <div class="header-box">
        <h1 class="header-title">Quiz 퀴즈</h1>
        <p class="header-desp">
          여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로
          도전해보세요.
        </p>
      </div>
      <header class="nav-bar">
        <nav>
          <RouterLink :to="{ name: 'home' }">Home</RouterLink>
        </nav>
      </header>
    </div>
  </div>
  <RouterView />
</template>

<script setup></script>

<style scoped>
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.header {
  /* border: 1px solid lightgray; */
  background-color: #f5f5f5;
}

.header-box {
  border: 1px solid darkgray;
  border-radius: 3%;
  margin: 5%;
}

.header-title {
  color: white;
  background-color: #ff922b;
  margin: 0;
  padding: 10px;
}
.header-desp {
  background-color: white;
  margin: 0;
  padding: 5%;
}

.nav-bar {
  background-color: #333333;
  color: white;
  margin: 25px;
}
</style>

