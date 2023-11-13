import { createApp } from "vue";
import { createPinia } from "pinia";
import PiniaPluginPersistedstate from "pinia-plugin-persistedstate";
import App from "./App.vue";

const app = createApp(App);

const pinia = createPinia();
pinia.use(PiniaPluginPersistedstate);

app.use(pinia);

app.mount("#app");