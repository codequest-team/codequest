import CONF from "@/config/";
import humps from "humps";

let socket = null;

const connect = (lobby, fn) => {
  if (socket) socket.close();

  const ACCESS_TOKEN = localStorage.getItem("access_token");

  const params = new URLSearchParams({ token: ACCESS_TOKEN });


  socket = new WebSocket(`${CONF.RACE_BASE_URL_WS}/lobby/${lobby}/ws?${params.toString()}`);

  socket.addEventListener("message", (e) => fn(humps.camelizeKeys(JSON.parse(e.data))));

  // socket.addEventListener("close", (e) => {
  //   if (e.code !== 1000) {
  //     setTimeout(() => connect(planId, userId, fn), 5000);
  //   }
  // });
};

const disconnect = () => socket?.close();

const send = (message) => {
  // const decamelizedMessage = JSON.stringify(humps.decamelizeKeys(message, { split: /(?=[A-Z0-9])/ }));

  // if (socket.readyState === WebSocket.OPEN) {
  //   socket.send(decamelizedMessage);
  //   return;
  // }

  // socket.addEventListener("open", () => {
  //   socket.send(decamelizedMessage, { once: true });
  // });
};

export default {
  connect,
  disconnect,
  send,
};


//ws://localhost:8000/GTPKB/?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjgwMDBiN2VkLTVlZWItNDIzNy05YjU0LTE2MDk4ZGY4ZWM0MSIsInVzZXJuYW1lIjoibWF4aW0iLCJleHAiOjE2Nzk4MTY0MzQsInRva2VuX3R5cGUiOiJhY2Nlc3MifQ.0loT5X9-NHEgJtztzFgibljaW3Ee6x9gxoPMDJ-coFc/ws/.
//ws://127.0.0.1:8000/lobby/ipeYW/ws