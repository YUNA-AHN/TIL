<template>
  <div>
    <header class="header">
      <div>
        <nav class="nav">
          <RouterLink class="nav-link" :to="{ name: 'home' }">HOME</RouterLink>
        </nav>
      </div>
    </header>
    <main class="main">
      <RouterView />
    </main>
  </div>
</template>

<script setup></script>

<style scoped>
.header {
  background-color: #333333;
  color: white;
}
.nav {
  display: flex;
  justify-content: center;
}
.main {
  text-align: center;
}

.nav-link {
  color: #f7f7f7;
  text-decoration: none;
  margin: 10px;
}
</style>
