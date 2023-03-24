import { Quasar, Notify, Dialog, Loading } from "quasar";
import langRu from "quasar/lang/ru";
import "quasar/src/css/index.sass";
import "@quasar/extras/material-icons/material-icons.css";

// Глобольная конфигурация Loading (Quasar)
Loading.setDefaults({
  boxClass: "bg-grey-2 text-grey-9",
  spinnerColor: "primary",
  backgroundColor: "transparent",
});

export default {
  install(app) {
    app.use(Quasar, { plugins: { Notify, Dialog, Loading }, lang: langRu });
  },
};