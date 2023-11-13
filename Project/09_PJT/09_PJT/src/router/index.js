import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SearchView from "../views/SearchView.vue";
import DetailView from "../views/DetailView.vue";
import LaterView from "../views/LaterView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/search",
      name: "search",
      component: SearchView,
    },
    {
      path: "/search/:id",
      name: "detail",
      component: DetailView,
    },
    {
      path: "/later",
      name: "later",
      component: LaterView,
    },
  ],
});

export default router;

