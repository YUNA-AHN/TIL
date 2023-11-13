<template>
  <div>
    <h1>나중에 볼 영상</h1>
    <div v-if="laterVideo" class="video-list">
      <div v-for="video in laterVideo" :key="video.id" class="video-card">
        <img 
          @click="goDetail(video)"
          :src="video._rawValue.snippet.thumbnails.high.url"
          alt=""
          class="imgtag" 
          />
        <div class="textbox">
          <strong>{{ video._rawValue.snippet.title }}</strong>
        </div>
      </div>
    </div>
    <div v-else>
      <strong>등록된 비디오 없음</strong>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const laterVideoRaw  = ref(null)
laterVideoRaw.value = JSON.parse(localStorage.getItem('video'))

const laterVideo = ref(null)
laterVideo.value = laterVideoRaw._rawValue

// console.log(laterVideo)

const goDetail = (video) => {
  router.push(`/search/${video._rawValue.id}`);
};

// console.log(laterVideo._rawValue[0]._rawValue.id)
</script>

<style scoped>

h1 {
  margin: 30px;
  font-weight: bolder;
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
