<template>
  <div>
    <!-- Vue Router 사용하는 대표적인 템플릿 -->
    <!-- 1. router-link 태그 -->
    <!-- 페이지간의 링크를 생성하는데 사용하는 태그
      기본적으로는 a 태그로 렌더링(*실질적 페이지x, 
      내부 페이지 전환은 javascript 기반으로 전환이 수행된다! = 
      페이지 전환은 컴포넌트의 변경으로 이루어진다!)
    -->
    <!-- <RouterLink to="/">Home</RouterLink> -->
    <RouterLink :to="{ name: 'home' }">Home</RouterLink>
    <router-link to="/about">About</router-link>
    <router-link to="/users/1">User 1</router-link>
    <router-link to="/users/2">User 2</router-link>
    <router-link :to="{ name: 'profile', params: { id: 1 } }"
      >User1</router-link
    >
    <router-link :to="{ name: 'profile', params: { id: 2 } }"
      >User1</router-link
    >
    <!-- 2. router-view 태그 -->
    <!-- 현재 경로에 따라서 동적으로 컴포넌트를 렌더링하는 역할을 수행...-->
    <RouterView />
  </div>
</template>

<script setup></script>

<style scoped></style>

