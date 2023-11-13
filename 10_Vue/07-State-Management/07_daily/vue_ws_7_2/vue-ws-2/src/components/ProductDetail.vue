<template>
  <div class="product-card">
    <div>
      <strong>{{ product.name }}</strong>
    </div>
    <img :src="product.imagePath" alt="" />
    <div>\{{ product.price }}</div>
    <div v-if="product.isFavorite">❤️</div>
    <div v-else>🤍</div>
  </div>
</template>

<script setup>
// const props = defineProps({
//   product: Object,
// });

defineProps({
  product: Object,
});

// console.log(props);
</script>

<style scoped>
.product-card {
  width: 300px;
  border: 1px solid lightgray;
  margin: 10px;
  padding: 10px;
  text-align: center;
}
img {
  width: 80%;
  height: 60%;
}
</style>
