<template>
  <div>
    <!-- Logo -->
    <RouterLink :to="{ name: 'feed' }">
      <img
        class="flex my-2 justify-center xl:justify-start"
        src="../assets/Y-logo.png"
        alt="Y-logo"
        style="width: 60px; height: 60px"
      />
    </RouterLink>

    <!-- /Logo -->

    <!-- Nav -->
    <nav class="mt-5">
      <RouterLink
        :to="{ name: 'feed' }"
        class="flex items-center justify-center xl:justify-start text-blue-400 mb-8 transition duration-350 ease-in-out"
      >
        <svg fill="currentColor" viewBox="0 0 24 24" class="h-6 w-6">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M22.58 7.35L12.475 1.897c-.297-.16-.654-.16-.95 0L1.425 7.35c-.486.264-.667.87-.405 1.356.18.335.525.525.88.525.16 0 .324-.038.475-.12l.734-.396 1.59 11.25c.216 1.214 1.31 2.062 2.66 2.062h9.282c1.35 0 2.444-.848 2.662-2.088l1.588-11.225.737.398c.485.263 1.092.082 1.354-.404.263-.486.08-1.093-.404-1.355zM12 15.435c-1.795 0-3.25-1.455-3.25-3.25s1.455-3.25 3.25-3.25 3.25 1.455 3.25 3.25-1.455 3.25-3.25 3.25z"
          ></path>
        </svg>
        <span class="hidden xl:block ml-4 font-bold text-md">Home</span>
      </RouterLink>

      <!-- Search tab-->
      <RouterLink
       :to="{ name: 'search' }"
        class="flex items-center justify-center xl:justify-start text-gray-800 dark:text-white hover:text-blue-400 dark:hover:text-blue-400 mb-8 transition duration-350 ease-in-out"
      >
        <svg fill="currentColor" viewBox="0 0 24 24" class="h-6 w-6">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="0.5"
            d="M10.25 4.25c-3.314 0-6 2.686-6 6s2.686 6 6 6c1.657 0 3.155-.67 4.243-1.757 1.087-1.088 1.757-2.586 1.757-4.243 0-3.314-2.686-6-6-6zm-9 6c0-4.971 4.029-9 9-9s9 4.029 9 9c0 1.943-.617 3.744-1.664 5.215l4.475 4.474-2.122 2.122-4.474-4.475c-1.471 1.047-3.272 1.664-5.215 1.664-4.971 0-9-4.029-9-9z"
          ></path>
        </svg>
        <span class="hidden xl:block ml-4 font-bold text-md">Explore</span>
      </RouterLink>
      <!-- /Search tab-->

      <a
        href="#"
        class="flex items-center justify-center xl:justify-start text-gray-800 dark:text-white hover:text-blue-400 dark:hover:text-blue-400 mb-8 transition duration-350 ease-in-out"
      >
        <svg fill="currentColor" viewBox="0 0 24 24" class="h-6 w-6">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M21.697 16.468c-.02-.016-2.14-1.64-2.103-6.03.02-2.532-.812-4.782-2.347-6.335C15.872 2.71 14.01 1.94 12.005 1.93h-.013c-2.004.01-3.866.78-5.242 2.174-1.534 1.553-2.368 3.802-2.346 6.334.037 4.33-2.02 5.967-2.102 6.03-.26.193-.366.53-.265.838.102.308.39.515.712.515h4.92c.102 2.31 1.997 4.16 4.33 4.16s4.226-1.85 4.327-4.16h4.922c.322 0 .61-.206.71-.514.103-.307-.003-.645-.263-.838zM12 20.478c-1.505 0-2.73-1.177-2.828-2.658h5.656c-.1 1.48-1.323 2.66-2.828 2.66zM4.38 16.32c.74-1.132 1.548-3.028 1.524-5.896-.018-2.16.644-3.982 1.913-5.267C8.91 4.05 10.397 3.437 12 3.43c1.603.008 3.087.62 4.18 1.728 1.27 1.285 1.933 3.106 1.915 5.267-.024 2.868.785 4.765 1.525 5.896H4.38z"
          ></path>
        </svg>
        <span class="hidden xl:block ml-4 font-bold text-md"
          >Notifications</span
        >
      </a>

      <a
        href="#"
        class="flex items-center justify-center xl:justify-start text-gray-800 dark:text-white hover:text-blue-400 dark:hover:text-blue-400 mb-8 transition duration-350 ease-in-out"
      >
        <svg fill="currentColor" viewBox="0 0 24 24" class="h-6 w-6">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M19.25 3.018H4.75C3.233 3.018 2 4.252 2 5.77v12.495c0 1.518 1.233 2.753 2.75 2.753h14.5c1.517 0 2.75-1.235 2.75-2.753V5.77c0-1.518-1.233-2.752-2.75-2.752zm-14.5 1.5h14.5c.69 0 1.25.56 1.25 1.25v.714l-8.05 5.367c-.273.18-.626.182-.9-.002L3.5 6.482v-.714c0-.69.56-1.25 1.25-1.25zm14.5 14.998H4.75c-.69 0-1.25-.56-1.25-1.25V8.24l7.24 4.83c.383.256.822.384 1.26.384.44 0 .877-.128 1.26-.383l7.24-4.83v10.022c0 .69-.56 1.25-1.25 1.25z"
          ></path>
        </svg>
        <span class="hidden xl:block ml-4 font-bold text-md">Messages</span>
      </a>

      <!-- Bookmarks tab-->
      <a
        class="flex items-center justify-center xl:justify-start text-gray-800 dark:text-white hover:text-blue-400 dark:hover:text-blue-400 mb-8 transition duration-350 ease-in-out"
      >
        <svg fill="currentColor" viewBox="0 0 24 24" class="h-6 w-6">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M19.9 23.5c-.157 0-.312-.05-.442-.144L12 17.928l-7.458 5.43c-.228.164-.53.19-.782.06-.25-.127-.41-.385-.41-.667V5.6c0-1.24 1.01-2.25 2.25-2.25h12.798c1.24 0 2.25 1.01 2.25 2.25v17.15c0 .282-.158.54-.41.668-.106.055-.223.082-.34.082zM12 16.25c.155 0 .31.048.44.144l6.71 4.883V5.6c0-.412-.337-.75-.75-.75H5.6c-.413 0-.75.338-.75.75v15.677l6.71-4.883c.13-.096.285-.144.44-.144z"
          ></path>
        </svg>
        <span class="hidden xl:block ml-4 font-bold text-md">Bookmarks</span>
      </a>
      <!-- /Bookmarks tab-->

      <!-- Profile tab-->
      <a
        class="flex items-center justify-center xl:justify-start text-gray-800 dark:text-white hover:text-blue-400 dark:hover:text-blue-400 mb-8 transition duration-350 ease-in-out"
      >
        <svg fill="currentColor" viewBox="0 0 24 24" class="h-6 w-6">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 11.816c1.355 0 2.872-.15 3.84-1.256.814-.93 1.078-2.368.806-4.392-.38-2.825-2.117-4.512-4.646-4.512S7.734 3.343 7.354 6.17c-.272 2.022-.008 3.46.806 4.39.968 1.107 2.485 1.256 3.84 1.256zM8.84 6.368c.162-1.2.787-3.212 3.16-3.212s2.998 2.013 3.16 3.212c.207 1.55.057 2.627-.45 3.205-.455.52-1.266.743-2.71.743s-2.255-.223-2.71-.743c-.507-.578-.657-1.656-.45-3.205zm11.44 12.868c-.877-3.526-4.282-5.99-8.28-5.99s-7.403 2.464-8.28 5.99c-.172.692-.028 1.4.395 1.94.408.52 1.04.82 1.733.82h12.304c.693 0 1.325-.3 1.733-.82.424-.54.567-1.247.394-1.94zm-1.576 1.016c-.126.16-.316.246-.552.246H5.848c-.235 0-.426-.085-.552-.246-.137-.174-.18-.412-.12-.654.71-2.855 3.517-4.85 6.824-4.85s6.114 1.994 6.824 4.85c.06.242.017.48-.12.654z"
          ></path>
        </svg>
        <span class="hidden xl:block ml-4 font-bold text-md">Profile</span>
      </a>
      <!-- /Profile tab-->

      <a
        class="flex items-center justify-center xl:justify-start text-gray-800 dark:text-white hover:text-blue-400 dark:hover:text-blue-400 mb-8 transition duration-350 ease-in-out"
      >
        <svg fill="currentColor" viewBox="0 0 24 24" class="h-6 w-6">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10.54 1.75h2.92l1.57 2.36c.11.17.32.25.53.21l2.53-.59 2.17 2.17-.58 2.54c-.05.2.04.41.21.53l2.36 1.57v2.92l-2.36 1.57c-.17.12-.26.33-.21.53l.58 2.54-2.17 2.17-2.53-.59c-.21-.04-.42.04-.53.21l-1.57 2.36h-2.92l-1.58-2.36c-.11-.17-.32-.25-.52-.21l-2.54.59-2.17-2.17.58-2.54c.05-.2-.03-.41-.21-.53l-2.35-1.57v-2.92L4.1 8.97c.18-.12.26-.33.21-.53L3.73 5.9 5.9 3.73l2.54.59c.2.04.41-.04.52-.21l1.58-2.36zm1.07 2l-.98 1.47C10.05 6.08 9 6.5 7.99 6.27l-1.46-.34-.6.6.33 1.46c.24 1.01-.18 2.07-1.05 2.64l-1.46.98v.78l1.46.98c.87.57 1.29 1.63 1.05 2.64l-.33 1.46.6.6 1.46-.34c1.01-.23 2.06.19 2.64 1.05l.98 1.47h.78l.97-1.47c.58-.86 1.63-1.28 2.65-1.05l1.45.34.61-.6-.34-1.46c-.23-1.01.18-2.07 1.05-2.64l1.47-.98v-.78l-1.47-.98c-.87-.57-1.28-1.63-1.05-2.64l.34-1.46-.61-.6-1.45.34c-1.02.23-2.07-.19-2.65-1.05l-.97-1.47h-.78zM12 10.5c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5c.82 0 1.5-.67 1.5-1.5s-.68-1.5-1.5-1.5zM8.5 12c0-1.93 1.56-3.5 3.5-3.5 1.93 0 3.5 1.57 3.5 3.5s-1.57 3.5-3.5 3.5c-1.94 0-3.5-1.57-3.5-3.5z"
          ></path>
        </svg>
        <span class="hidden xl:block ml-4 font-bold text-md">Settings</span>
      </a>

      <!-- User Menu -->
      <div v-if="userStore.user.isAuthenticated">
        <div
          id="dropdownAvatarNameButton"
          data-dropdown-toggle="dropdownAvatarName"
          class="flex items-center text-sm pe-1 font-medium text-gray-900 rounded-full hover:text-blue-600 dark:hover:text-white-500 md:me-0 focus:ring-4 focus:ring-gray-100 dark:focus:ring-dim-700 dark:text-white cursor-pointer"
          @click="toggleDropDown"
        >
          <span class="sr-only">Open user menu</span>
          <img
            class="w-8 h-8 me-2 rounded-full"
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQq5_JvyIL-RDm7skjduw5wJz1hQwk9UimpMA&s"
            alt="user photo"
          />
          {{ userStore.user.name }}
          <svg
            class="w-2.5 h-2.5 ms-3"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 10 6"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="m1 1 4 4 4-4"
            />
          </svg>
        </div>
      </div>
      <!-- Dropdown menu -->
      <div v-if="showDropDown">
        <div
          id="dropdownAvatarName"
          class="z-10 bg-white divide-y divide-gray-100 rounded-lg shadow w-60 dark:bg-gray-700 dark:divide-gray-600"
        >
          <div class="px-4 py-3 text-sm text-gray-900 dark:text-white">
            <div class="font-sm text-xs">Signed in as</div>
            <div class="truncate">{{ userStore.user.email }}</div>
          </div>

          <div class="py-2">
            <div
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-dim-100 dark:hover:bg-dim-600 dark:text-gray-200 dark:hover:text-white cursor-pointer"
              @click="handleSignOut"
            >
              Sign out
            </div>
          </div>
        </div>
      </div>
    </nav>
    <!-- /Nav -->
  </div>
</template>

<script>
import { RouterLink } from "vue-router";
import { useUserStore } from "../stores/user";

export default {
  setup() {
    const userStore = useUserStore();

    return {
      userStore,
    };
  },
  data() {
    return {
      showDropDown: false,
    };
  },

  methods: {
    toggleDropDown() {
      this.showDropDown = !this.showDropDown;
    },
    handleSignOut() {
      this.userStore.removeToken();
    },
  },
};
</script>
