<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useAuthStore } from "@/stores/counter";
import ArticleListItem from "@/components/ArticleListItem.vue";

const store = useAuthStore();
console.log(store.articles);
</script>
