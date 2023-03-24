<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script setup>
import { computed, markRaw } from "vue";

import { useRoute } from "vue-router";

import defaultLayout from "./layouts/default-layout.vue";
import emptyLayout from "./layouts/empty-layout.vue";

const route = useRoute();

const layout = computed(() => markRaw(route.meta.layout === 'default' ? defaultLayout : emptyLayout));
</script>
