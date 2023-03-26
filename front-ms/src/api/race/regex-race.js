import api from "./api";

const EDN_POINT = "/regex-race";

export default {
  Learn: {
    list(params = {}) {
      return api.get(`${EDN_POINT}/learn`, { params: params });
    },
    validateAnswer(id, data) {
      return api.post(`${EDN_POINT}/learn/${id}`, data);
    },
    validateAnswer(id, data) {
      return api.post(`${EDN_POINT}/learn/${id}`, data);
    },
    // update(id, data) {
    //   return api.patch(`${EDN_POINT}/educations/${id}/`, data);
    // },
    // delete(id) {
    //   return api.delete(`${EDN_POINT}/educations/${id}/`);
    // },
  },
  Lobby: {
    create() {
      return api.post(`${EDN_POINT}/lobby`);
    },
    get(lobbyId) {
      return api.get(`${EDN_POINT}/lobby/${lobbyId}`);
    },
  },
};
