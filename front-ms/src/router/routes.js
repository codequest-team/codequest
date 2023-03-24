import Home from "@/pages/home.vue";
import Games from "@/pages/games/games.vue";
import RegexRace from "@/pages/games/regex-race/game.vue";

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
    component: RegexRace,
    meta: { layout: "default", needsAuthorization: true },
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: () => import("../pages/log-in/log-in.vue"),
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
