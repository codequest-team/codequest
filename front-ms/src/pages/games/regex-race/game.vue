<template>
  <section class="text-gray-600 body-font relative">
    <div class="container px-5 py-24 mx-auto flex sm:flex-nowrap flex-wrap">
      <div
        class="lg:w-2/3 md:w-1/2 bg-slate-100 rounded-lg overflow-hidden sm:mr-10 p-10 flex items-end justify-center relative"
      >
        <game-canvas
          :width="400"
          :height="400"
          :num-players="numPlayers"
          :num-tasks="numTasks"
          @add-new-player="increaseNumberOfPlayers"
        />
      </div>

      <div class="lg:w-1/3 md:w-1/2 bg-slate-100 flex flex-col md:ml-auto w-full md:py-8 mt-8 md:mt-0 rounded-lg p-4">
        <div class="relative mb-4">
          <label for="name" class="leading-7 text-sm text-gray-600">Ожидаемый результат</label>
          <input
            type="text"
            id="name"
            name="name"
            readonly
            class="w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
          />
        </div>
        <div class="relative mb-4">
          <label for="email" class="leading-7 text-sm text-gray-600">Текст</label>
          <input
            type="email"
            id="email"
            name="email"
            readonly
            class="w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
          />
        </div>

        <div class="relative mb-4">
          <label for="message" class="leading-7 text-sm text-gray-600">Результат</label>
          <input
            type="email"
            id="email"
            name="email"
            readonly
            class="w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
          />
        </div>

        <div class="relative mb-4">
          <label for="message" class="leading-7 text-sm text-gray-600">Регекс</label>
          <input
            type="email"
            id="email"
            name="email"
            class="w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
          />
        </div>
        <button
          class="text-white bg-green-500 border-0 py-2 px-6 focus:outline-none hover:bg-green-600 rounded text-lg"
        >
          Отправить
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import gameCanvas from "./game-canvas.vue";
import { RegexRace } from "@/api/race";

const numPlayers = ref(4);
const numTasks = ref(5);

const increaseNumberOfPlayers = () => (numPlayers.value += 1);

onMounted(async () => {
  await RegexRace.Learn.list()
    .then((r) => console.log(r.data))
    .catch((e) => {});
})
</script>
