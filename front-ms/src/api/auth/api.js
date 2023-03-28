import axios from "axios";
import humps from "humps";
// import qs from "qs";
import CONF from "@/config";
import router from "@/router";
import store from "@/store";
import { Notify } from "quasar";
import User from "./user";

const api = axios.create({
  baseURL: `${CONF.AUTH_BASE_URL}/`,
  headers: {
    Authorization: localStorage.getItem("access_token") ? localStorage.getItem("access_token") : "",
  },
  transformResponse: [
    function (data) {
      // Конвертируем все имена переменных в camelKeys
      if (data && typeof data === "string") {
        return humps.camelizeKeys(JSON.parse(data));
      }

      return data;
    },
  ],
  // transformRequest: [
  //   function (data, headers) {
  //     if (data && typeof data === "object") {
  //       // Конвертируем все имена переменных в snake_case
  //       if (data instanceof FormData) {
  //         const formData = new FormData();

  //         for (const [key, value] of data.entries()) {
  //           formData.append(humps.decamelize(key, { split: /(?=[A-Z0-9])/ }), value);
  //         }

  //         return formData;
  //       }

  //       return humps.decamelizeKeys(data, { split: /(?=[A-Z0-9])/ });
  //     }

  //     return data;
  //   },
  //   ...axios.defaults.transformRequest,
  // ],
  // paramsSerializer: {
  //   serialize: (params) => {
  //     const decamelizedParams = humps.decamelizeKeys(params, { split: /(?=[A-Z0-9])/ });
  //     return qs.stringify(decamelizedParams, { indices: false });
  //   },
  // },
});

api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response) {
      // for (const property in error.response.data) {
      //   Notify.create({ type: "warning", timeout: 5000, message: error.response.data[property] });
      // }

      if (error.response.status === 401) {
        if (localStorage.getItem("refresh_token")) {
          User.refreshToken()
            .then((r) => {
              localStorage.setItem("access_token", r.data.accessToken);
              localStorage.setItem("refresh_token", r.data.refreshToken);
              router.push("/");
            })
            .catch((e) => {});
          store.commit("RESET_STATE");
          router.push("/log-in");
        }
      }
    }

    // Если сервер недоступен
    if (error.request.status === 0) {
      Notify.create({ timeout: 3000, message: "Не удалось установить соединение с сервером" });
    }

    return Promise.reject(error);
  }
);

export default api;
