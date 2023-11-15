<template>
  <div>
    <h1>게시물 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title" /> <br />
      <label for="content">내용 : </label>
      <input type="text" id="content" v-model.trim="content" />
      <input type="submit" name="" id="" />
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { useArticleStore } from "@/stores/articles";
import { useRouter } from "vue-router";
import { ref } from "vue";

const title = ref(null);
const content = ref(null);
const store = useArticleStore();
const router = useRouter();

const createArticle = function () {
  console.log(title.value);
  console.log(content.value);
  axios({
    method: "post",
    url: "http://127.0.0.1:8000/api/v1/articles/",
    data: {
      title: title.value,
      content: content.value,
    },
  })
    .then(() => {
      router.push({ name: "home" });
    })
    .catch((err) => console.log(err));
};
</script>

<style scoped></style>
