import { version } from '../../package.json';

const CONF = Object.freeze({
  VERSION: version,
  VUEX_STRICT: import.meta.env.VITE_APP_VUEX_STRICT === "true",
  AUTH_BASE_URL: import.meta.env.VITE_APP_AUTH_BASE_URL,
  RACE_BASE_URL: import.meta.env.VITE_APP_RACE_BASE_URL,
  RACE_BASE_URL_WS: import.meta.env.VITE_APP_RACE_BASE_URL_WS,
  HOST: import.meta.env.VITE_APP_HOST,
});

export default CONF;
