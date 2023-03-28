<template>
  <section class="text-gray-600 body-font relative">
    <div class="container mx-auto flex sm:flex-nowrap flex-wrap">
      <div
        v-show="isLobbyCreated"
        class="lg:w-2/3 md:w-1/2 bg-slate-100 rounded-lg overflow-hidden m-2 p-3 flex justify-center relative"
      >
        <game-canvas
          ref="gameCanvasRef"
          :width="300"
          :height="400"
          :num-players="numPlayers"
          :num-tasks="numTasks"
          :current-user="currentUser"
        />
      </div>

      <template v-if="isGameStarted">
        <formDataVue
          class="lg:w-1/2 md:w-1/2 bg-slate-100 flex flex-col md:ml-auto w-full mx-2 md:py-8 md:mt-2 rounded-lg p-4"
          @on-task-solved="moveCarUp"
          :current-user="currentUser"
        />
      </template>
      <template v-else>
        <lobyy-gen
          class="lg:w-1/2 md:w-1/2 bg-slate-100 flex flex-col md:ml-auto w-full mx-2 md:py-8 md:mt-2 rounded-lg p-4"
          @on-lobby-created="() => (isLobbyCreated = true)"
          @on-new-user-connected="onNewUserConnected"
          @on-game-started="() => isGameStarted = true"
        />
      </template>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, computed, watch } from "vue";
import gameCanvas from "./game-canvas.vue";
import { RegexRace } from "@/api/race";
import { required, maxLength } from "@/utils/validators";
import { Notify, Platform } from "quasar";
import { useStore } from "vuex";

import formDataVue from "./form-data.vue";
import lobyyGen from "./lobyy-gen.vue";

const store = useStore();

const isGameStarted = ref(false);
const isLobbyCreated = ref(false);

const currentUser = computed(() => store.getters["user"]);

const gameCanvasRef = ref(null);

const numPlayers = ref(1);
const numTasks = ref(5);

const increaseNumberOfPlayers = () => (numPlayers.value += 1);

const onNewUserConnected = (data) => {
  gameCanvasRef.value.addCar(data);
}

// const tasks = ref([]);
// const currentTask = ref(null);
// const form = ref({
//   regex: "",
// });

// const currentTaskTitle = computed(() => {
//   const indexOfCurLevel = tasks.value.findIndex((t) => t.level === currentTask.value.level);
//   return `${indexOfCurLevel + 1} / ${tasks.value.length} - ${currentTask.value.title}`;
// });

// const response = ref(null);

// const isGameOver = ref(false);

// const restartGame = () => {
//   currentTask.value = tasks.value[0];
//   isGameOver.value = false;
//   form.value.regex = "";
// };

const moveCarUp = (playerUsername) => {
  gameCanvasRef.value.moveCarUp(playerUsername);
};

const nextTask = () => {
  const nextTask = tasks.value.find((t) => t.level === currentTask.value.level + 1);

  if (nextTask) {
    currentTask.value = nextTask;
    form.value.regex = "";
    response.value = null;
  } else {
    Notify.create({
      color: "green",
      message: "Вы успешно прошли игру.",
    });
    isGameOver.value = true;
  }
};

const onSubmit = async () => {
  response.value = null;

  const formData = new FormData();
  formData.append("regex", form.value.regex);

  await RegexRace.Learn.validateAnswer(currentTask.value.level, formData)
    .then((r) => {
      response.value = r.data;

      if (response.value.isTrue) {
        gameCanvasRef.value.moveCarUp(1);
      }
    })
    .catch((e) => {});
};

// watch(isLobbyCreated, () => {
//   if (isLobbyCreated.value) {
//     gameCanvasRef.value.addCar(currentUser.value.username);
//   }
// });

onMounted(async () => {
  await RegexRace.Learn.list()
    .then((r) => {
      tasks.value = r.data;
      currentTask.value = tasks.value[0];
      numTasks.value = tasks.value.length;
    })
    .catch((e) => {});
});
</script>
