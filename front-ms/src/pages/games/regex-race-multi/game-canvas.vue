<template>
  <div class="flex flex-col">
    <canvas id="canvas" class="bg-gray-600 rounded-md" :width="`${width}px`" :height="`${height}px`" />
  </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from "vue";
import { drawRoad, drawCars, drawUsernames } from "./helpers";

const props = defineProps({
  width: { type: Number, required: true },
  height: { type: Number, required: true },
  numTasks: { type: Number, required: true },
  currentUser: { type: Object, required: true },
});

const emit = defineEmits(["addNewPlayer"]);

const canvas = ref(null);
const ctx = ref(null);

const players = ref([]);

const laneWidth = computed(() => props.width / numPlayers.value);

const stepSize = computed(() => canvas.value?.height / (props.numTasks + 1));

const randInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

const numPlayers = computed(() => players.value.length);

// const shuffleCars = () => {
//   for (let i = 0; i < props.numPlayers; i++) {
//     players.value[i].position = randInt(1, props.numTasks + 1);
//   }
// };

// const moveRandomCarForward = () => {
//   players.value[randInt(0, props.numPlayers - 1)].targetPosition += 1;
// };

const addCar = (users) => {
  players.value.length = 0;

  for (const key in users) {
    const player = {
      id: players.value.length + 1,
      position: 1,
      targetPosition: 1,
      username: users[key],
      carImage: new Image(),
    };

    console.log(player)

    console.log((players.value.length + 1) % 6)

    player.carImage.src = `/src/assets/cars/car-${(players.value.length + 1) % 6}.svg`;

    players.value.push(player);

    console.log(`${key}: ${users[key]}`);
  }
};

const moveCarUp = (username) => {
  let player = players.value.find((p) => p.username === username);
  player.targetPosition += 1;
};

const updateField = async () => {
  ctx.value.clearRect(0, 0, canvas.value.width, canvas.value.height);
  drawRoad(ctx.value, canvas.value.width, canvas.value.height, numPlayers.value, laneWidth.value, stepSize.value);
  await drawCars(ctx.value, canvas.value.width, canvas.value.height, laneWidth.value, stepSize.value, players.value);
  drawUsernames(ctx.value, canvas.value.width, canvas.value.height, laneWidth.value, players.value);
};

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
  canvas.value.width = 300;
  canvas.value.height = 400;

  animate();
});

defineExpose({ moveCarUp, addCar });
</script>
