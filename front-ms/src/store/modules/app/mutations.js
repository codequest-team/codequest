import { api } from "@/api/auth";

export function SET_USER(state, user) {
  state.user = user;
  state.isAuthenticated = true;
}

export function RESET_STATE(state) {
  state.user = null;
  state.isAuthenticated = false;
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  api.defaults.headers.Authorization = "";
}
