<template>
  <div>
    <header class="header">
      <div>
        <nav class="nav">
          <RouterLink class="nav-link" :to="{ name: 'home' }">Home</RouterLink>
          <RouterLink class="nav-link" :to="{ name: 'products' }"
            >Products</RouterLink
          >
          <RouterLink class="nav-link" :to="{ name: 'favorite' }"
            >Favorite</RouterLink
          >
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
  background-color: black;
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
  color: white;
  text-decoration: none;
  margin: 10px;
}
</style>
