import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

// Vue Router를 사용하기 위해 전역으로 등록하겠다.
app.use(router);

app.mount("#app");
