import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useCounterStore = defineStore("counter", () => {
  let id = 0;
  const ProductList = ref([
    {
      id: id++,
      name: "상품 1",
      imagePath: "src/assets/product1.png",
      price: 10000,
      isFavorite: false,
    },
    {
      id: id++,
      name: "상품 2",
      imagePath: "src/assets/product2.png",
      price: 20000,
      isFavorite: false,
    },
    {
      id: id++,
      name: "상품 3",
      imagePath: "src/assets/product3.png",
      price: 30000,
      isFavorite: false,
    },
    {
      id: id++,
      name: "상품 4",
      imagePath: "src/assets/product4.png",
      price: 40000,
      isFavorite: false,
    },
  ]);
  return { ProductList };
});
