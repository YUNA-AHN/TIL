<template>
  <div v-for="article in store.articles">
    <h3>{{ article.id }}번 게시글</h3>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <hr />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useArticleStore } from "@/stores/articles";
const store = useArticleStore();

onMounted(() => {
  store.getArticles();
});

console.log(store.articles);
</script>

<style scoped></style>
