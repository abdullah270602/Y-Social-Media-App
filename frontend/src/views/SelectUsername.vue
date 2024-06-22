<template>
  <div>
    <div
      class="bg-gray-50 dark:bg-gray-900 min-h-screen flex items-center justify-center"
    >
      <div
        class="w-full bg-white rounded-lg shadow dark:border sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white text-center"
          >
            Choose Your Username
          </h1>
          <p class="text-sm text-gray-600 dark:text-white">
            What should we call you? You can always change it later in your
            profile settings.
          </p>

          <form class="max-w-sm mx-auto" @submit.prevent="submitForm">
            <div class="mb-5">
              <label
                for="username"
                class="block mb-2 sm:text-sm font-medium dark:text-white text-gray-700"
                :class="{
                  'text-green-700 dark:text-green-500':
                    usernameStatus === 'success',
                  'text-red-700 dark:text-red-500': usernameStatus === 'error',
                }"
              >
                Username
              </label>
              <input
                type="text"
                id="username"
                class="sm:text-sm rounded-lg block w-full p-2.5 dark:bg-gray-700 dark:border dark:text-white text-gray-700"
                :class="{
                  'border-green-500': usernameStatus === 'success',
                  'bg-red-50 border-red-500 text-red-900 placeholder-red-700 focus:ring-red-500 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500':
                    usernameStatus === 'error',
                }"
                placeholder="Enter your username"
                v-model="form.username"
                @input="validateUsername"
                required
              />
              <p
                class="mt-2 text-sm"
                :class="{
                  'text-green-600 dark:text-green-500':
                    usernameStatus === 'success',
                  'text-red-600 dark:text-red-500': usernameStatus === 'error',
                }"
              >
                <span class="font-medium">{{ usernameMessage.title }}</span>
                {{ usernameMessage.body }}
              </p>
            </div>

            <button
              type="submit"
              class="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
              :disabled="usernameStatus !== 'success'"
            >
              Next
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        username: "",
      },
      usernameStatus: "", // '' | 'success' | 'error'
      usernameMessage: {
        title: "",
        body: "",
      },
    };
  },

  methods: {
    validateUsername() {
      const invalidChars = /[@(),`&%$#!*./";'~{}]/;
      if (this.form.username === "") {
        this.usernameStatus = "";
        this.usernameMessage = {
          title: "",
          body: "",
        };
      } else if (invalidChars.test(this.form.username)) {
        this.usernameStatus = "error";
        this.usernameMessage = {
          title: "Oops!",
          body: "Username contains invalid characters!",
        };
      } else {
        this.checkUsernameAvailability();
      }
    },
    checkUsernameAvailability() {
      axios
        .post("/api/check-username-exists/", { username: this.form.username })
        .then((response) => {
          console.log("usernameStatus exists:", response.data.exists);
          if (response.data.exists) {
            this.usernameStatus = "error";
            this.usernameMessage = {
              title: "Oops!",
              body: "Username already taken!",
            };
          } else {
            this.usernameStatus = "success";
            this.usernameMessage = {
              title: "Alright!",
              body: "Username available!",
            };
          }
        })
        .catch((error) => {
          console.error(error);
          this.usernameStatus = "error";
          this.usernameMessage = {
            title: "Error!",
            body: "An error occurred while checking username availability.",
          };
        });
    },
    submitForm() {
      // Retrieve access token from localStorage
      const accessToken = localStorage.getItem("access_token");

      if (this.usernameStatus === "success" && accessToken) {
        axios
          .post(
            "/api/submit-username/",
            { username: this.form.username },
            {
              headers: {
                Authorization: `Bearer ${accessToken}`, // Include access token in header
                "Content-Type": "application/json", // Set content type as JSON
              },
            }
          )
          .then((response) => {
            if (response.status === 201) {
              // Handle success (optional)
              this.$router.push({ name: "Home" });
            }
          })
          .catch((error) => {
            console.error(error);
            this.usernameStatus = "error";
            this.usernameMessage = {
              title: "Error!",
              body: "An error occurred while submitting the username.",
            };
          });
      } else {
        // Handle case where usernameStatus is not "success" or accessToken is missing
        console.error("Invalid username status or access token missing.");
      }
    },
  },
};
</script>

<style>
/* Add any additional styles here */
</style>
