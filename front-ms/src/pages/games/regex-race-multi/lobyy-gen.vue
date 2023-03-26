<template>
  <div class="py-1 w-full">
    <q-btn class="my-2" label="Создать лобби" @click.stop="createLobby()" v-if="!isLobbyCreated" />
    <q-btn class="my-2" color="primary" label="Начать игру" @click.stop="createLobby()" v-else />
    <p>{{ lobby }}</p>

    <template v-if="isLobbyCreated && !isGameStarted">
      <p class="text-green-800">Лобби создано! Отправьте ссылку друзьям и дождитесь их подключения.</p>
      <p class="text-red-800">
        http://localhost:8080{{ route.fullPath }}
        <q-btn
          @click="copyToClipboard()"
          flat
          class="q-ml-sm"
          color="grey-9"
          round
          size="xs"
          icon="content_copy"
        />
      </p>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { RegexRace } from "@/api/race";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const emit = defineEmits(["onLobbyCreated"]);
const isLobbyCreated = ref(false);
const isGameStarted = ref(false);

const lobby = ref(null);

const copyToClipboard = () => {
  var textarea = document.createElement("textarea");
  textarea.value = `http://localhost:8080${route.fullPath}`;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
};

const createLobby = async () => {
  await RegexRace.Lobby.create()
    .then((r) => {
      lobby.value = r.data;
      emit("onLobbyCreated");
      isLobbyCreated.value = true;
      router.replace({ query: { ...route.query, lobby: lobby.value.lobbyId } });
    })
    .catch((e) => {});
};

onMounted(async () => {
  if (route.query.lobby) {
    await RegexRace.Lobby.get(route.query.lobby).then((r) => {
      lobby.value = r.data;
      isLobbyCreated.value = true;
      emit("onLobbyCreated");
    });
  }
});
</script>
