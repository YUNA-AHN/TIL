<template>
  <div>
    <h1>상세 페이지</h1>
    <div v-if="product" class="product-card">
      <img :src="product.image" alt="" />
      <strong>{{ product.title }}</strong>
      <p>가격 : ${{ product.price }}</p>
    </div>
    <div v-else>
      <strong>로딩 중...</strong>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const product = ref("");
const productId = route.params.productId;
const storeURL = `https://fakestoreapi.com/products/${productId}`;

axios
  .get(storeURL)
  .then((response) => {
    // console.log(response.data)
    product.value = response.data;
  })
  .catch((error) => {
    console.error(error);
  });
</script>

<style scoped></style>
