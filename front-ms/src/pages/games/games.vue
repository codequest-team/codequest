<template>
  <div class="container px-5 py-5 mx-auto">
    <div class="flex flex-wrap -m-4 text-center">
      <div class="p-4 md:w-1/4 sm:w-1/2 w-full cursor-pointer" @click.stop="$router.push('/regex-race')">
        <div class="border-2 border-gray-200 px-4 py-6 rounded-lg hover:bg-indigo-100">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            class="text-indigo-500 w-20 h-20 mb-3 inline-block"
            viewBox="0 0 25 24"
          >
            <path
              d="M2.52 3.515A2.5 2.5 0 0 1 4.82 2h6.362c1 0 1.904.596 2.298 1.515l.792 1.848c.075.175.21.319.38.404.5.25.855.715.965 1.262l.335 1.679c.033.161.049.325.049.49v.413c0 .814-.39 1.543-1 1.997V13.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-1.338c-1.292.048-2.745.088-4 .088s-2.708-.04-4-.088V13.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-1.892c-.61-.454-1-1.183-1-1.997v-.413a2.5 2.5 0 0 1 .049-.49l.335-1.68c.11-.546.465-1.012.964-1.261a.807.807 0 0 0 .381-.404l.792-1.848ZM3 10a1 1 0 1 0 0-2 1 1 0 0 0 0 2Zm10 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2ZM6 8a1 1 0 0 0 0 2h4a1 1 0 1 0 0-2H6ZM2.906 5.189a.51.51 0 0 0 .497.731c.91-.073 3.35-.17 4.597-.17 1.247 0 3.688.097 4.597.17a.51.51 0 0 0 .497-.731l-.956-1.913A.5.5 0 0 0 11.691 3H4.309a.5.5 0 0 0-.447.276L2.906 5.19Z"
            />
          </svg>
          <h2 class="title-font font-medium text-3xl text-gray-900">Regex Race</h2>
          <p class="leading-relaxed">Изучайте и решайте на скорость регулярные выражения со своими друзьями!</p>
        </div>
      </div>
      <div class="p-4 md:w-1/4 sm:w-1/2 w-full cursor-pointer">
        <div class="border-2 border-gray-200 px-4 py-6 rounded-lg hover:bg-indigo-100">
          <svg fill="currentColor" class="text-indigo-500 w-16 h-16 mb-3 inline-block" viewBox="0 0 24 24">
            <path
              d="M0 1.5A1.5 1.5 0 0 1 1.5 0h13A1.5 1.5 0 0 1 16 1.5v13a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 14.5v-13zM1.5 1a.5.5 0 0 0-.5.5V5h4V1H1.5zM5 6H1v4h4V6zm1 4h4V6H6v4zm-1 1H1v3.5a.5.5 0 0 0 .5.5H5v-4zm1 0v4h4v-4H6zm5 0v4h3.5a.5.5 0 0 0 .5-.5V11h-4zm0-1h4V6h-4v4zm0-5h4V1.5a.5.5 0 0 0-.5-.5H11v4zm-1 0V1H6v4h4z"
            />
          </svg>
          <h2 class="title-font font-medium text-3xl text-gray-900">
            3 в ряд
            <q-badge align="top" color="red" label="В разработке" />
          </h2>

          <p class="leading-relaxed">
            Играйте в самый популярный формат мобильных игр с пользой для себя! Пишите регулярные выражения, которые
            принесут вам как можно больше совпадений!
          </p>
        </div>
      </div>
      <div class="p-4 md:w-1/4 sm:w-1/2 w-full cursor-pointer">
        <div class="border-2 border-gray-200 px-4 py-6 rounded-lg hover:bg-indigo-100">

          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="text-indigo-500 w-12 h-12 mb-3 inline-block"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125"
            />
          </svg>

          <h2 class="title-font font-medium text-3xl text-gray-900">
            SQL Race
            <q-badge align="top" color="red" label="В разработке" />
          </h2>
          <p class="leading-relaxed">
            Встречайте всем полюбившийся формат гонок с новым функционалом! Пишите оптимизированные SQL запросы быстрее
            соперников и побеждайте!
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup></script>
