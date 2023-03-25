<template>
  <section class="text-gray-600 body-font relative">
    <div class="container mx-auto flex sm:flex-nowrap flex-wrap">
      <div class="lg:w-2/3 md:w-1/2 bg-slate-100 rounded-lg overflow-hidden m-2 p-3 flex justify-center relative">
        <div class="flex flex-row flex-nowrap">
          <div class="md:w-1/4 mr-1">
            <game-canvas
              ref="gameCanvasRef"
              :width="100"
              :height="400"
              :num-players="numPlayers"
              :num-tasks="numTasks"
              @add-new-player="increaseNumberOfPlayers"
              :current-user="currentUser"
            />
          </div>

          <div class="md:w-3/4 mx-2">
            <div
              v-if="currentTask !== null"
              class="w-full max-h-96 border rounded border-gray-300 p-4 overflow-auto"
              v-html="marked(currentTask.theoryText)"
            ></div>
          </div>
        </div>
      </div>

      <q-form
        @submit="onSubmit()"
        v-if="currentTask != null"
        class="lg:w-1/2 md:w-1/2 bg-slate-100 flex flex-col md:ml-auto w-full mx-2 md:py-8 md:mt-2 rounded-lg p-4"
      >
        <p class="uppercase pb-2 font-bold md:text-lg">{{ currentTask.title }}</p>

        <div class="py-1 w-full">
          <p class="text-gray-500 truncate font-bold md:text-lg">Задача</p>
          {{ currentTask.taskDescription }}
        </div>

        <div class="py-1 w-full">
          <p class="text-gray-500 truncate font-bold md:text-lg">Текст</p>
          {{ currentTask.text }}
        </div>

        <div class="py-1 w-full">
          <p class="text-gray-500 truncate font-bold md:text-lg">Ожидаемый результат</p>
          {{ currentTask.expectedResult }}
        </div>

        <div class="py-1 w-full">
          <p class="text-gray-500 truncate font-bold md:text-lg">Регулярное выражение</p>
          <q-input
            dense
            outlined
            v-model.trim="form.regex"
            autogrow
            lazy-rules="ondemand"
            :rules="[required, (val) => maxLength(val, 255)]"
          />
        </div>

        <div class="py-1 w-full">
          <p class="text-gray-500 truncate font-bold md:text-lg">Результат</p>
          <q-banner
            rounded
            :class="{
              'bg-green-4 text-white': response?.isTrue === true,
              'bg-red-4 text-white': response?.isTrue === false,
              'bg-blue-grey-2': response === null,
            }"
          >
            <template v-slot:avatar>
              <q-icon name="done" size="md" color="white" v-if="response?.isTrue === true" />
              <q-icon name="close" size="md" color="white" v-else-if="response?.isTrue === false" />
            </template>
            {{ response?.result }}
          </q-banner>
        </div>

        <q-btn
          class="py-1 my-2 w-full"
          label="Проверить"
          type="submit"
          color="primary"
          v-if="response?.isTrue !== true && isGameOver !== true"
        />

        <q-btn
          class="py-1 my-2 w-full"
          label="Следующая"
          color="primary"
          v-if="response?.isTrue === true && isGameOver !== true"
          @click.stop="nextTask()"
        />

        <q-btn
          class="py-1 my-2 w-full"
          label="Начать с начала"
          color="primary"
          v-if="isGameOver === true"
          @click.stop="restartGame()"
        />
      </q-form>

      <div></div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import gameCanvas from "./game-canvas.vue";
import { RegexRace } from "@/api/race";
import { required, maxLength } from "@/utils/validators";
import { Notify, Platform } from "quasar";
import { useStore } from "vuex";
import { marked } from "marked";

const store = useStore();

const currentUser = computed(() => store.getters["user"]);

const gameCanvasRef = ref(null);

const numPlayers = ref(1);
const numTasks = ref(5);

const increaseNumberOfPlayers = () => (numPlayers.value += 1);

const tasks = ref([]);
const currentTask = ref(null);
const form = ref({
  regex: "хохо",
});

const response = ref(null);

const isGameOver = ref(false);

const restartGame = () => {
  currentTask.value = tasks.value[0];
  isGameOver.value = false;
  form.value.regex = "";
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
