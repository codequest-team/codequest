<template>
  <q-layout>
    <q-page-container>
      <q-page class="row justify-center items-center">
        <q-card flat>
          <q-card-section>
            <q-input
              ref="usernameRef"
              v-model.trim="form.username"
              outlined
              lazy-rules="ondemand"
              :rules="[required]"
              type="username"
              label="Пользователь"
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

            <div class="q-mt-md" align="cente q-gutter-md">
              <q-btn size="lg" color="primary" class="full-width text-white py-2" label="Войти" @click="onLogIn" />
            </div>

            <button
              class="pt-2 underline text-slate-700"
              @click.stop="$router.push({ path: '/sign-up', query: $route.query })"
            >
              регистрация
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
import { api, User } from "@/api/auth";
import { useRouter, useRoute } from "vue-router";

const route = useRoute();
const router = useRouter();

const usernameRef = ref(null);
const passwordRef = ref(null);

const form = ref({
  username: null,
  password: null,
});

const visibility = ref(false);

const passwordFieldType = computed(() => (visibility.value ? "text" : "password"));

const visibilityIcon = computed(() => (visibility.value ? "visibility_off" : "visibility"));

const onLogIn = async () => {
  usernameRef.value.validate();
  passwordRef.value.validate();

  if (usernameRef.value.hasError || passwordRef.value.hasError) return;

  const formData = new FormData();

  formData.append("username", form.value.username);
  formData.append("password", form.value.password);

  await User.login(formData)
    .then((r) => {
      localStorage.setItem("access_token", r.data.accessToken);
      localStorage.setItem("refresh_token", r.data.refreshToken);

      if (route.query.target) {
        router.push(route.query.target)
      } else {
        router.push("/");
      }
    })
    .catch((e) => {});
};

document.title = "Вход | ITP";
</script>
