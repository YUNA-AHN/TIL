<template>
  <div @click="goback()">뒤로가기</div>
  <div class="videobox">
    <h1>{{ video.snippet.title }}</h1>
    <p>업로드 날짜 : {{ video.snippet.publishedAt.slice(0, 10) }}</p>

    <iframe width="420" height="500" :src="videoSrc" class="video-main">
    </iframe>

    <div class="content">
      {{ video.snippet.description }}
    </div>
  </div>
  <button @click="addlater(video)">동영상 저장</button>
</template>

<script setup>
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const route = useRoute();
const video = ref("");

const videoId = route.params.id;
const videoSrc = ref(`https://www.youtube.com/embed/${videoId}`);

const youtubeURL = `https://youtube.googleapis.com/youtube/v3/videos`;

const api_key = "AIzaSyDDV83u8u0QxwWY-oesNML_HNz5XBX1Gw0";

const params = {
  key: api_key,
  id: videoId,
  part: "snippet",
};

axios
  .get(youtubeURL, { params })
  .then((response) => {
    // console.log(response.data.items[0]);
    video.value = response.data.items[0];
  })
  .catch((error) => {
    console.log(error);
  });

const router = useRouter();
const goback = () => {
  router.go(-1);
};

const addlater = (later) => {
  // 여러 데이터 저장하기
  // 현재 localStorage 에 저장된 데이터 가져오기
  // 만약 없다면 비어있는 리스트로 초기화
  const existingLater = JSON.parse(localStorage.getItem("video")) || [];

  // 중복된 동영상이 있는지 확인
  const isDuplicate =
    // existingLater.length > 0 &&
    // id
    existingLater.find((item) => item.id === later.id);

  // 중복이 아니라면 추가
  if (!isDuplicate) {
    alert("나중에 볼 영상에 추가합니다");
    existingLater.push(video);
  } else {
    alert("나중에 볼 영상에서 제거합니다.");
  }

  // 수정된 나중에 볼 동영상 데이터를 localStorage 에 저장
  localStorage.setItem("video", JSON.stringify(existingLater));
};
</script>

<style scoped>
.videobox {
  display: flex;
  flex-direction: column;
  align-items: center;
}
h1 {
  margin: 20px;
  text-align: center;
  font-weight: bolder;
  font-size: xx-large;
}
p {
  margin: 10px;
  background-color: rgb(202, 219, 219);
  width: 100%;
  height: 30px;
  font-weight: bold;
  padding-left: 10px;
}
.video-main {
  margin: 20px;
  width: 90%;
}
.content {
  padding: 50px;
  font-weight: bold;
  font-size: large;
  border-top: 4px solid rgb(202, 219, 219);
  border-bottom: 4px solid rgb(202, 219, 219);
}
</style>
