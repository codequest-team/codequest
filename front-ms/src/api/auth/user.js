import api from "./api";

export default {
  getCredentials() {
    const ACCESS_TOKEN = localStorage.getItem("access_token");
    api.defaults.headers.Authorization = ACCESS_TOKEN;
    return api.get(`/get-credentials`);
  },
  login(data) {
    api.defaults.headers.Authorization = "";
    return api.post(`/login`, data);
  },
  refreshToken() {
    api.defaults.headers.Authorization = localStorage.getItem("refresh_token");
    return api.get(`/refresh`);
  },
};
