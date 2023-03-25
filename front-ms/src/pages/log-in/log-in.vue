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

            <div class="q-mt-md" align="center">
              <q-btn size="lg" color="primary" class="full-width text-white" label="Войти" @click="onLogIn" />
            </div>
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
      router.push("/");
    })
    .catch((e) => {});
};

document.title = "Вход | ITP";
</script>
