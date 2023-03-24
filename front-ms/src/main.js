import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";
import store from "@/store";
import quasar from "../quasar";
import "@/style.css";

const app = createApp(App);

app.use(quasar);
app.use(store);
app.use(router);
app.mount("#app");