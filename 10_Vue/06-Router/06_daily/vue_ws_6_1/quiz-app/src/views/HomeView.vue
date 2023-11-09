<template>
  <div class="manual">
    <h2>퀴즈 앱 사용 방법</h2>
    <h1>1. 퀴즈 목록 확인하기</h1>
    <p>퀴즈 목록 페이지에서 다양한 퀴즈를 확인하세요</p>
    <img src="@/assets/quizList.png" alt="" />
    <h1>2. 퀴즈 생성하기</h1>
    <p>퀴즈는 직접 생성 할 수도 있어요</p>
    <img src="@/assets/quizCreate.png" alt="" />
    <h1>3. 정답 페이지</h1>
    <p>작성한 답안이 정답인지 확인하세요</p>
    <img src="@/assets/quizAnswer.png" alt="" />
  </div>
</template>

<script setup></script>

<style scoped>
.manual {
  display: flex;
  flex-direction: column;
  align-items: center;
}

img {
  width: 700px;
  border: 1px solid lightgray;
}
</style>
