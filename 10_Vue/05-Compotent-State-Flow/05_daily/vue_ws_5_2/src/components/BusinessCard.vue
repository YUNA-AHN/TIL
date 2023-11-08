<template>
  <div class="app">
    <header class="header">
      <h1>명함 관리 페이지</h1>
    </header>
    <main class="main">
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </main>
    <h3>보유 명함 목록</h3>
    <article class="article">
      <!-- 카드가 들어갈 자리 -->
      <BusinessCardDetail
        v-for="card in businessCards"
        :name="card.name"
        :title="card.title"
        :key="card.name"
      />
    </article>
    <footer class="footer">
      <p>&copy; 2023 My Business Cards</p>
    </footer>
  </div>
</template>

<script setup>
import BusinessCardDetail from "@/components/BusinessCardDetail.vue";

const businessCards = [
  {
    name: "일론 머스크",
    title: "테슬라 테크노킹",
  },
  {
    name: "래리 엘리슨",
    title: "오라클 창업주",
  },
  {
    name: "빌 게이츠",
    title: "마이크로소프트 공동창업주",
  },
  {
    name: "래리 페이지",
    title: "구글 공동 창업주",
  },
  {
    name: "세르게이 브린",
    title: "구글 공동 창업주",
  },
];
</script>

<style scoped>
.app {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  width: 300px;
  background-color: #007acc;
  color: white;
  height: 80px;
}

.main {
}

.article {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.footer {
  background-color: #f0f0f0;
  width: 100%;
  height: 60px;
  text-align: center;
  position: fixed;
  bottom: 0;
}
</style>
