import api from "@/api/index.js";

const fetchArticleList = function () {
  api({
    method: "get",
    url: `${API_URL}/api/v1/articles/`,
    headers: {
      Authorization: `Token ${token.value}`,
    },
  })
    .then((res) => {
      // console.log(res)
      articles.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
};
