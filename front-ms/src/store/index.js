import { createStore } from "vuex";
import app from "./modules/app/";
import CONF from "../config/";

export default createStore({
  strict: CONF.VUEX_STRICT,
  state: app.state,
  getters: app.getters,
  actions: app.actions,
  mutations: app.mutations,
  modules: {},
});
