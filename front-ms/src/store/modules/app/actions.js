import { Auth } from "../../../api";
import router from "@/router";

export const getUser = async (ctx) => {

  await Auth.getCredentials()
    .then((r) => ctx.commit("SET_USER", r.data))
    .catch((e) => {});
};

export const logout = async (ctx) => {
  ctx.commit("RESET_STATE");
  router.push("/log-in");
};
