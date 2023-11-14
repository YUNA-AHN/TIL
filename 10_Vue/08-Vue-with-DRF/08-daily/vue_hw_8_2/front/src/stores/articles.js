import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles'
    })
    .then(res => console.log(res))
  }

  return { articles, getArticles }
})
