import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useUserStore = defineStore({
  id: "user",

  state: () => ({
    user: {
      isAuthenticated: false,
      username: null,
      fullName: null,
      email: null,
      // profilePicture: null,
      dateOfBirth: null,
      access: null,
      refresh: null,
    },
  }),

  actions: {
    initStore() {
      // Checking if there are any stored tokens in the local storage.
      const access = localStorage.getItem("user.access");

      if (access) {
        this.user.access = access;
        this.user.refresh = localStorage.getItem("user.refresh");
        this.user.username = localStorage.getItem("user.username");
        this.user.fullName = localStorage.getItem("user.fullName");
        this.user.email = localStorage.getItem("user.email");
        // this.user.profilePicture = localStorage.getItem('user.profilePicture');
        this.user.dateOfBirth = localStorage.getItem("user.dateOfBirth");
        this.user.isAuthenticated = true;

        // Refresh the token to ensure it's valid.
        this.refreshToken();

        console.log("Initialized user", this.user);
      }
    },

    setToken(data) {
      console.log("Setting token", data);

      this.user.access = data.access;
      this.user.refresh = data.refresh;
      this.user.isAuthenticated = true;

      localStorage.setItem("user.access", data.access);
      localStorage.setItem("user.refresh", data.refresh);

      // Set axios default authorization header
      // axios.defaults.headers.common['Authorization'] = 'Bearer ' + data.access;
    },

    removeToken() {
      console.log("Removing token");

      this.user.access = null;
      this.user.refresh = null;
      this.user.username = null;
      this.user.fullName = null;
      this.user.email = null;
      // this.user.profilePicture = null;
      this.user.dateOfBirth = null;
      this.user.isAuthenticated = false;

      localStorage.removeItem("user.access");
      localStorage.removeItem("user.refresh");
      localStorage.removeItem("user.username");
      localStorage.removeItem("user.fullName");
      localStorage.removeItem("user.email");
      // localStorage.removeItem('user.profilePicture');
      localStorage.removeItem("user.dateOfBirth");

      // Remove axios default authorization header
      delete axios.defaults.headers.common["Authorization"];
    },

    setUserInfo(user) {
      console.log("Setting user info", user);

      this.user.username = user.username;
      this.user.fullName = user.full_name;
      this.user.email = user.email;
      // this.user.profilePicture = user.profile_picture;
      this.user.dateOfBirth = user.date_of_birth;

      localStorage.setItem("user.username", this.user.username);
      localStorage.setItem("user.fullName", this.user.fullName);
      localStorage.setItem("user.email", this.user.email);
      // localStorage.setItem('user.profilePicture', this.user.profilePicture);
      localStorage.setItem("user.dateOfBirth", this.user.dateOfBirth);
    },

    refreshToken() {
      axios
        .post("/api/refresh/", {
          refresh: this.user.refresh,
        })
        .then((response) => {
          this.user.access = response.data.access;
          localStorage.setItem("user.access", response.data.access);

          // Set axios default authorization header
          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.error("Error refreshing token", error);

          this.removeToken();
        });
    },


  },
});
