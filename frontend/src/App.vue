<template>
  <html class="dark">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    </head>

    <body>
      <RouterView />
    </body>
  </html>
</template>

<script>
import axios from "axios";
import { useUserStore } from "./stores/user";

export default {
  setup() {
    const userStore = useUserStore();

    return {
      userStore,
    };
  },

  beforeCreate() {
    this.userStore.initStore();

    const token = this.userStore.user.access;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>
