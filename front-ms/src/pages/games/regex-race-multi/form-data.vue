<template>
  <q-form
    @submit="onSubmit()"
    v-if="currentTask != null"
    class="lg:w-1/2 md:w-1/2 bg-slate-100 flex flex-col md:ml-auto w-full mx-2 md:py-8 md:mt-2 rounded-lg p-4"
  >
    <p class="uppercase pb-2 font-bold md:text-lg">{{ currentTaskTitle }}</p>

    <div class="py-1 w-full">
      <p class="text-gray-500 truncate font-bold md:text-lg">Задача</p>
      <div v-html="marked(currentTask.taskDescription)"></div>
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
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { RegexRace } from "@/api/race";
import { Notify, Platform } from "quasar";
import { required, maxLength } from "@/utils/validators";
import { marked } from "marked";

const props = defineProps({
  currentUser: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(["onTaskSolved"]);

const tasks = ref([]);
const currentTask = ref(null);
const form = ref({
  regex: "",
});

const currentTaskTitle = computed(() => {
  const indexOfCurLevel = tasks.value.findIndex((t) => t.level === currentTask.value.level);
  return `${indexOfCurLevel + 1} / ${tasks.value.length} - ${currentTask.value.title}`;
});

const response = ref(null);

const isGameOver = ref(false);

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
        emit("onTaskSolved", props.currentUser.username);
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
