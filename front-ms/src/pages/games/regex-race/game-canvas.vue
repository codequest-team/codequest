<template>
  <div class="flex flex-col">
    <canvas id="canvas" class="bg-gray-600 rounded-md" :width="`${width}px`" :height="`${height}px`" />
    <div class="flex flex-col border mt-2 rounded-md bg-slate-500">
      <button class="bg-gray-700 rounded text-white p-1 m-1" @click.stop="shuffleCars">Рандом</button>
      <button class="bg-gray-700 rounded text-white p-1 m-1" @click.stop="moveRandomCarForward">
        Сдвинуть случайную машину вперед
      </button>
      <button class="bg-gray-700 rounded text-white p-1 m-1" @click.stop="emit('addNewPlayer')">Добавить машину</button>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from "vue";
import { drawRoad, drawCars, drawUsernames } from "./helpers";

const props = defineProps({
  width: { type: Number, required: true },
  height: { type: Number, required: true },
  numPlayers: { type: Number, required: true },
  numTasks: { type: Number, required: true },
});

const emit = defineEmits(["addNewPlayer"]);

const canvas = ref(null);
const ctx = ref(null);

const players = ref([]);

const laneWidth = computed(() => props.width / props.numPlayers);

const stepSize = computed(() => canvas.value?.height / (props.numTasks + 1));

const randInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

const shuffleCars = () => {
  for (let i = 0; i < props.numPlayers; i++) {
    players.value[i].position = randInt(1, props.numTasks + 1);
  }
};

const moveRandomCarForward = () => {
  players.value[randInt(0, props.numPlayers - 1)].targetPosition += 1;
};

const addCar = () => {
  const player = {
    id: players.value.length + 1,
    position: 1,
    targetPosition: 1,
    username: `user_${players.value.length + 1}`,
    carImage: new Image(),
  };

  player.carImage.src = `/src/assets/cars/car-${player.id % 6}.svg`;

  players.value.push(player);
};

const updateField = async () => {
  ctx.value.clearRect(0, 0, canvas.value.width, canvas.value.height);
  drawRoad(ctx.value, canvas.value.width, canvas.value.height, props.numPlayers, laneWidth.value, stepSize.value);
  await drawCars(ctx.value, canvas.value.width, canvas.value.height, laneWidth.value, stepSize.value, players.value);
  drawUsernames(ctx.value, canvas.value.width, canvas.value.height, laneWidth.value, players.value);
};

const initPlayers = () => {
  players.value.length = 0;

  for (let i = 0; i < props.numPlayers; i++) {
    addCar();
  }
};

watch(() => props.numPlayers, () => initPlayers());

const animate = () => {
  requestAnimationFrame(animate);
  ctx.value.clearRect(0, 0, canvas.value.width, canvas.value.height);

  players.value.forEach((player) => {
    if (player.position < player.targetPosition) player.position += 0.05;
  });

  updateField();
};

onMounted(() => {
  canvas.value = document.querySelector("canvas");
  ctx.value = canvas.value.getContext("2d");

  // Установить размер canvas
  canvas.value.width = 400;
  canvas.value.height = 400;

  initPlayers();
  animate();
});
</script>
