import { version } from '../../package.json';

const CONF = Object.freeze({
  VERSION: version,
  VUEX_STRICT: import.meta.env.VITE_APP_VUEX_STRICT === "true",
  WSGI_BASE_URL: import.meta.env.VITE_APP_WSGI_BASE_URL,
  ASGI_BASE_URL: import.meta.env.VITE_APP_ASGI_BASE_URL,
});

export default CONF;
