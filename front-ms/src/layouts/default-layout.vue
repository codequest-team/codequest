<template>
  <q-layout view="hHh Lpr lff" class="shadow-2 rounded-borders" v-if="currentUser !== null">
    <q-header elevated class="bg-dark">
      <q-toolbar>
        <q-btn flat @click="leftDrawer = !leftDrawer" round dense icon="menu" />
        <q-toolbar-title>
          <q-btn flat :label="`${currentUser.username}`" />
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawer"
      show-if-above
      :mini="miniState"
      @mouseover="miniState = false"
      @mouseout="miniState = true"
      mini-to-overlay
      :width="250"
      :breakpoint="500"
      bordered
      class="bg-grey-3"
    >
      <q-scroll-area class="fit">
        <q-list padding>
          <q-item v-for="(item, index) in menuItems" :key="index" clickable :to="item.to">
            <q-item-section avatar>
              <q-icon :name="item.icon" />
            </q-item-section>

            <q-item-section style="white-space: nowrap">
              <q-item-label>{{ item.label }}</q-item-label>
            </q-item-section>
          </q-item>

          <q-item clickable @click="$store.dispatch('logout')">
            <q-item-section avatar>
              <q-icon name="logout" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Выйти</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { computed, ref } from "vue";
import CONF from "@/config/";
import { Notify } from "quasar";
import { useStore } from "vuex";

const store = useStore();

const leftDrawer = ref(false);
const miniState = ref(true);

const currentUser = computed(() => store.getters["user"]);

const menuItems = [
  { to: "/games", icon: "sports_esports", label: "Игры" },
  // { to: `/profile/${currentUser.value.id}/`, icon: "person", label: "Профиль" },
  { to: "/about", icon: "info", label: "О проекте" },
  { to: "/faqs", icon: "help_outline", label: "FAQ" },
];
</script>
