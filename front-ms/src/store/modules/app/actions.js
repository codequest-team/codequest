import { User } from "@/api/auth";
import router from "@/router";

export const getUser = async (ctx) => {
  await User.getCredentials()
    .then((r) => ctx.commit("SET_USER", r.data))
    .catch((e) => {});
};

export const logout = async (ctx) => {
  await User.logout()
    .then((r) => {})
    .catch((e) => {});
  ctx.commit("RESET_STATE");
  router.push("/log-in");
};
