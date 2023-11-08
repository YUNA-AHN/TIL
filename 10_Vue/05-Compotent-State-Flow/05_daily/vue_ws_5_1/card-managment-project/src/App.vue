<template>
  <div class="warp">
    <h1 class="header">명함 관리 페이지</h1>
    <div class="main">
      명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.
    </div>
    <div class="article"></div>
    <div class="footer">ⓒ 2023 My Business Cards</div>
  </div>
</template>

<script setup></script>

<style scoped>
.warp {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}

.header {
  background-color: #007acc;
  color: white;
  padding: 40px;
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

