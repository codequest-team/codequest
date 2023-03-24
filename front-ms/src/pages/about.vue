<template>
  <div class="flex flex-col justify-center items-center h-screen" @click="counter += 1">
    <h6 class="uppercase">CODE QUEST</h6>

    <h6>Версия: {{ CONF.VERSION }}</h6>

    <div class="flex items-center flex-col" v-if="counter > 2">
      <h6 class="font-bold">Разработчики:</h6>

      <p>Ким Максим</p>
      <p>Дюсенов Асет</p>
      <p>Песков Сергей</p>
    </div>
  </div>
</template>

<script setup>
import CONF from "@/config/";
import { ref } from "vue";

const counter = ref(0);

document.title = "О проекте";
</script>
