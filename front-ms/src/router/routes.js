import Home from "@/pages/home.vue";
import Games from "@/pages/games/games.vue";

export default [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { layout: "empty", needsAuthorization: true },
  },
  {
    path: "/games",
    name: "Games",
    component: Games,
    meta: { layout: "default", needsAuthorization: true },
  },
  {
    path: "/regex-race",
    name: "RegexRace",
    component: () => import("../pages/games/regex-race/game.vue"),
    meta: { layout: "default", needsAuthorization: true },
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: () => import("../pages/log-in/log-in.vue"),
    meta: { layout: "empty", needsAuthorization: false },
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: () => import("../pages/sign-up/sign-up.vue"),
    meta: { layout: "empty", needsAuthorization: false },
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../pages/about.vue"),
    meta: { layout: "default", needsAuthorization: true },
  },
  {
    path: "/faqs",
    name: "FAQs",
    component: () => import("../pages/faqs/faqs.vue"),
    meta: { layout: "default", needsAuthorization: true },
  },
];
