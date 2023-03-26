import { createRouter, createWebHistory } from "vue-router";
import store from "@/store";
import routes from "./routes";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  if (to.matched.some((record) => record.meta.needsAuthorization)) {
    if (store.getters["isAuthenticated"]) {
      next();
    } else if (localStorage.getItem("access_token")) {
      await store.dispatch("getUser");
      next();
    } else {
      console.log(to)
      next("/log-in?target=/regex-race-multi?lobby=DbTdp");
    }
  } else {
    next();
  }
});

export default router;
