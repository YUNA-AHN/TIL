<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<!-- <template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink :to="{ name: 'search' }">Search</RouterLink>
    </nav>
  </header>

  <RouterView />
</template> -->

<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg bg-success-subtle">
      <div class="container-fluid">
        <span class="navbar-brand">myTube</span>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink class="nav-link active" aria-current="page" to="/"
                >Home</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink
                class="nav-link active"
                aria-current="page"
                :to="{ name: 'search' }"
                >Search</RouterLink
              >
            </li>
            <li class="nav-item">
              <RouterLink
                class="nav-link active"
                aria-current="page"
                :to="{ name: 'later' }"
                >Later</RouterLink
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <RouterView />
  </div>
</template>

<style scoped>
.container {
  padding: 0px;
}
.navbar-brand {
  font-weight: bolder;
  margin: 0px;
}
</style>

