<template>
  <div>

    <h1>For testing</h1>
    <h3>{{ userStore.user.username }}</h3>
    <h3>{{ userStore.user.fullName }}</h3>
    <h3>{{ userStore.user.email }}</h3>

    <button class="bg-gray-600 text-white rounded-lg" @click="handleSignOut">
      Sign out
    </button>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/user";
import { onMounted } from "vue";
import axios from "axios";
export default {
  setup() {
    const userStore = useUserStore();

    // Fetch home data when component is mounted
    onMounted(() => {
      axios
        .get("/api/home/")
        .then((response) => {
          if (response.status === 200) {
            console.log("Verified");
          } else {
            console.log("Not verified");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });

    return {
      userStore,
    };
  },

  methods: {
    handleSignOut() {
      this.userStore.removeToken();
    },
  },
};
</script>

<style>
/* Add any necessary styles */
</style>
