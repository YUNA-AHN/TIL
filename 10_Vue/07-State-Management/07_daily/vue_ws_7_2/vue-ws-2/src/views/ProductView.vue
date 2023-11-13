<template>
  <div>
    <h1>상품 목록 페이지</h1>
    <div class="product-card-list">
      <ProductDetail
        v-for="product in store.ProductList"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/products";
import ProductDetail from "@/components/ProductDetail.vue";

const store = useCounterStore();
// console.log(store.ProductList);
</script>

<style scoped>
.product-card-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  display: inline-block;
  border: 1px solid black;
  width: 30%;
  margin: 10px;
}
</style>
