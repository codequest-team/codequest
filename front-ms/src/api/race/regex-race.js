import api from "./api";

const EDN_POINT = "/regex-race";

export default {
  Learn: {
    list(params = {}) {
      return api.get(`${EDN_POINT}/learn`, { params: params });
    },
    validateAnswer(data) {
      return api.post(`${EDN_POINT}/learn/`, data);
    },
    // create(data) {
    //   return api.post(`${EDN_POINT}/educations/`, data);
    // },
    // update(id, data) {
    //   return api.patch(`${EDN_POINT}/educations/${id}/`, data);
    // },
    // delete(id) {
    //   return api.delete(`${EDN_POINT}/educations/${id}/`);
    // },
  },
};
