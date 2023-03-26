<template>
  <div class="py-1 w-full">
    <q-btn class="my-2" label="Создать лобби" @click.stop="createLobby()" v-if="!isLobbyCreated" />
    <q-btn class="my-2" color="primary" label="Начать игру" @click.stop="startGame()" v-else-if="isGameStarted != true"/>

    <template v-if="isLobbyCreated && !isGameStarted">
      <p class="text-green-800">Лобби создано! Отправьте ссылку друзьям и дождитесь их подключения.</p>
      <p class="text-red-800">
        {{ url }}
        <q-btn @click="copyToClipboard()" flat class="q-ml-sm" color="grey-9" round size="xs" icon="content_copy" />
      </p>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { RegexRace } from "@/api/race";
import { useRoute, useRouter } from "vue-router";
import { LobbySocket } from "@/socket";
import CONF from "@/config";

const route = useRoute();
const router = useRouter();

const emit = defineEmits(["onLobbyCreated", "onNewUserConnected", "onGameStarted"]);
const isLobbyCreated = ref(false);
const isGameStarted = ref(false);

const lobby = ref(null);

const isUserLobbyCreator = ref(false);

const url = computed(() => {
  return `${CONF.HOST}${route.fullPath}`
})

const copyToClipboard = () => {
  var textarea = document.createElement("textarea");
  textarea.value = url.value;
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

      LobbySocket.connect(lobby.value.lobbyId, (data) => {
        console.log(data);
        if (data["users"] != null) {
          emit("onNewUserConnected", data['users']);
          if (Object.keys(data["users"]).length === 3) {
            isGameStarted.value = true;
            emit("onGameStarted");
          }
        };
      });

      isUserLobbyCreator.value = true;
    })
    .catch((e) => {});
};

const startGame = async () => {
  // isGameStarted.value = true;
  // LobbySocket.send({
  //   "message": "Start!!!"
  // })
};

onMounted(async () => {
  if (route.query.lobby) {
    await RegexRace.Lobby.get(route.query.lobby).then((r) => {
      lobby.value = r.data;
      isLobbyCreated.value = true;
      emit("onLobbyCreated");

      LobbySocket.connect(route.query.lobby, (data) => {
        console.log(data);
        if (data["users"] != null) {
          emit("onNewUserConnected", data['users']);
          console.log(Object.keys(data["users"]).length)
          if (Object.keys(data["users"]).length === 3) {
            isGameStarted.value = true;
            emit("onGameStarted");
          }
        }
      });
    });
  }
});
</script>
