<template>
  <div class="box">
    <h1>유튜브 검색</h1>
    <div class="inputbox">
      <form method="post" @submit.prevent="searchVideo">
        <input
          class="inputtag"
          v-model="searchInput"
          type="text"
          name="search"
          id="search"
          placeholder="검색어를 입력하세요"
        />
        <button type="submit" class="inputbtn">검색</button>
      </form>
    </div>
    <div v-if="keywordIsEmpty" class="video-list">
      <div v-for="video in videos" :key="video.id" class="video-card">
        <img
          @click="goDetail(video)"
          :src="video.snippet.thumbnails.high.url"
          alt=""
          class="imgtag"
        />
        <div class="textbox">
          <strong>{{ video.snippet.title }}</strong>
        </div>

        <!-- <button @click="goDetail(product)">상세페이지로 이동</button> -->
      </div>
    </div>
    <!-- <div v-else>
      <strong>검색어를 입력하세요.</strong>
    </div> -->
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();
const videos = ref([]);
// const youtubeURL = `https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=${keyword}&type=video&key=${api_key}`

// const youtubeURL = `https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=${keyword}&type=video&key=AIzaSyBJ_pP-yNFqw4Mm5priBQFx67SIF91TZoU`;

const youtubeURL = "https://www.googleapis.com/youtube/v3/search";

const api_key = "AIzaSyDDV83u8u0QxwWY-oesNML_HNz5XBX1Gw0";

const searchInput = ref("");

// const params = {
//   key: api_key,
//   q: searhInput.value,
//   //   fields: "items",
//   maxResults: 25,
// };

const searchVideo = () => {
  axios
    .get(youtubeURL, {
      params: {
        key: api_key,
        q: searchInput.value,
        type: "video",
        part: "snippet",
        maxResults: 25,
      },
    })
    .then((response) => {
      //   console.log(response.data.items.length);
      videos.value = response.data.items;
    })
    .catch((error) => {
      console.log(error);
    });
};

const keywordIsEmpty = computed(() => {
  return videos.value.length > 0 ? true : false;
});

const goDetail = (video) => {
  router.push(`/search/${video.id.videoId}`);
};
</script>

<style scoped>
h1 {
  margin: 30px;
  font-weight: bolder;
}
.inputtag {
  width: 60%;
  height: 40px;
  margin: 0px 10px 20px;
}
.inputbtn {
  height: 40px;
}
.video-list {
  display: flex;
  flex-direction: row;
  align-items: center;
  flex-wrap: wrap;
  justify-content: space-around;
}
.video-card {
  border: 1px solid lightgray;
  padding: 20px;
  margin: 10px 0px;
  width: 300px;
  height: 400px;
  text-align: center;
  border-radius: 60px;
}
.imgtag {
  width: 100%;
  margin-bottom: 30px;
  border-radius: 60px;
}
</style>
