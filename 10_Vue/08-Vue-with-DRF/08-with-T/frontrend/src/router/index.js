import { createRouter, createWebHistory } from "vue-router";
import TodoListView from "@/views/TodoListView";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "todo-list",
      component: TodoListView,
    },
    {
      path: "/:id",
      name: "todo-list",
      component: TodoListView,
    },
    {
      path: "/:id",
      name: "todo-list",
      component: TodoCreateView,
    },
  ],
});

export default router;
