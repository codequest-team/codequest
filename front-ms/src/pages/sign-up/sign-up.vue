<template>
  <q-layout>
    <q-page-container>
      <q-page class="row justify-center items-center">
        <q-card flat>
          <q-card-section>
            <q-input
              v-show="false"
              ref="nicknameRef"
              v-model.trim="form.nickname"
              outlined
              lazy-rules="ondemand"
              :rules="[required]"
              type="username"
              label="Ваш ник"
              @keydown.enter.prevent="onLogIn"
              :autofocus="true"
            >
              <template #prepend>
                <q-icon name="person" />
              </template>
              <template #append>
                <q-icon name="close" @click="form.nickname = ''" class="cursor-pointer" />
              </template>
            </q-input>

            <q-input
              ref="usernameRef"
              v-model.trim="form.username"
              outlined
              lazy-rules="ondemand"
              :rules="[required]"
              type="username"
              label="Юзернейм"
              @keydown.enter.prevent="onLogIn"
              :autofocus="true"
            >
              <template #prepend>
                <q-icon name="person" />
              </template>
              <template #append>
                <q-icon name="close" @click="form.username = ''" class="cursor-pointer" />
              </template>
            </q-input>

            <q-input
              ref="passwordRef"
              class="q-mt-sm"
              v-model.trim="form.password"
              outlined
              :type="passwordFieldType"
              lazy-rules="ondemand"
              :rules="[required]"
              label="Пароль"
              @keydown.enter.prevent="onLogIn"
            >
              <template #prepend>
                <q-icon name="lock" />
              </template>
              <template #append>
                <q-icon :name="visibilityIcon" @click="visibility = !visibility" class="cursor-pointer" />
                <q-icon name="close" @click="form.password = ''" class="cursor-pointer" />
              </template>
            </q-input>

            <q-input
              ref="password2Ref"
              class="q-mt-sm"
              v-model.trim="form.password2"
              outlined
              :type="passwordFieldType"
              lazy-rules="ondemand"
              :rules="[required]"
              label="Подтвердите пароль"
              @keydown.enter.prevent="onLogIn"
            >
              <template #prepend>
                <q-icon name="lock" />
              </template>
              <template #append>
                <q-icon :name="visibilityIcon" @click="visibility = !visibility" class="cursor-pointer" />
                <q-icon name="close" @click="form.password = ''" class="cursor-pointer" />
              </template>
            </q-input>

            <div class="q-mt-md" align="center">
              <q-btn size="lg" color="primary" class="full-width text-white" label="Создать аккаунт" @click="onLogIn" />
            </div>

            <button
              class="pt-2 underline text-slate-700"
              @click.stop="$router.push({ path: '/log-in', query: $route.query })"
            >
              Уже есть аккаунт?
            </button>
          </q-card-section>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref, computed } from "vue";
import { required } from "@/utils/validators";
import { User } from "@/api/auth";
import { useRouter } from "vue-router";
import { Notify } from "quasar";

const router = useRouter();

const nicknameRef = ref(null);
const usernameRef = ref(null);
const passwordRef = ref(null);
const password2Ref = ref(null);

const form = ref({
  nickname: "sdfsdf",
  username: null,
  password: null,
  password2: null,
});

const visibility = ref(false);

const passwordFieldType = computed(() => (visibility.value ? "text" : "password"));

const visibilityIcon = computed(() => (visibility.value ? "visibility_off" : "visibility"));

const onLogIn = async () => {
  nicknameRef.value.validate();
  usernameRef.value.validate();
  passwordRef.value.validate();

  if (nicknameRef.value.hasError || usernameRef.value.hasError || passwordRef.value.hasError) return;

  if (form.value.password !== form.value.password2) {
    Notify.create({
      type: "warning",
      message: "Пароли не совпадают",
    });
  }
  const formData = new FormData();

  formData.append("nickname", form.value.nickname);
  formData.append("username", form.value.username);
  formData.append("password", form.value.password);

  await User.signup(formData)
    .then((r) => {
      localStorage.setItem("access_token", r.data.accessToken);
      localStorage.setItem("refresh_token", r.data.refreshToken);
      router.push("/");
    })
    .catch((e) => {});
};

document.title = "Вход | ITP";
</script>
