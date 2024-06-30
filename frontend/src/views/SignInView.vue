<template>
  <div
    class="bg-gray-50 dark:bg-gray-900 min-h-screen flex items-center justify-center"
  >
    <div
      class="w-full bg-white rounded-lg shadow dark:border sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
    >
      <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <div class="flex items-center justify-center mb-6">
          <img
            class="w-8 h-8"
            src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg"
            alt="logo"
          />
        </div>
        <h1
          class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white text-center"
        >
          Sign in to your account
        </h1>
        <form class="space-y-4 md:space-y-6" @submit.prevent="submitForm">
          <div>
            <label
              for="email"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Your email</label
            >
            <input
              type="email"
              v-model="form.email"
              class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-gray-600 focus:border-gray-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="dodge@company.com"
              @input="validateEmail"
              required
            />
            <span v-if="errors.email" class="text-red-500 text-xs">{{
              errors.email
            }}</span>
          </div>
          <div>
            <label
              for="password"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Password</label
            >
            <input
              type="password"
              placeholder="••••••••"
              class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-gray-600 focus:border-gray-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              v-model="form.password"
              @input="validatePassword"
              required
            />
            <span v-if="errors.password" class="text-red-500 text-xs">{{
              errors.password
            }}</span>
          </div>
          <button
            type="submit"
            class="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
            :disabled="formInvalid"
          >
            Sign in
          </button>
          <p class="text-sm font-light text-gray-500 dark:text-gray-400">
            Don't have an account?
            <RouterLink
              :to="{ name: 'signup' }"
              class="font-medium text-blue-600 hover:underline dark:text-primary-500"
            >
              Sign up
            </RouterLink>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/user";
import axios from "axios";

export default {
  setup(){
    const userStore = useUserStore()


    return {
      userStore
    }
  },
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      errors: {
        email: null,
        password: null,
      },
      emailValid: false,
    };
  },

  computed: {
    formInvalid() {
      return !!this.errors.email || !!this.errors.password;
    },
  },

  methods: {
    validateEmail() {
      if (!this.form.email) {
        this.errors.email = "Your email is missing";
      } else if (!this.validateEmailFormat(this.form.email)) {
        this.errors.email = "Invalid email format";
      } else {
        this.errors.email = "";
        this.emailValid = true;
      }
    },

    validatePassword() {
      if (!this.form.password) {
        this.errors.password = "Password is required";
      } else {
        this.errors.password = "";
      }
    },

    validateEmailFormat(email) {
      const re =
        /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@(([^<>()[\]\\.,;:\s@"]+\.)+[^<>()[\]\\.,;:\s@"]{2,})$/i;
      return re.test(String(email).toLowerCase());
    },

    async submitForm() {
      if (this.formInvalid) {
        return;
      }

    
      await axios
        .post("/api/login/", this.form)
        .then((response) => {
          this.userStore.setToken(response.data);

          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log("error while signing in", error);
        });

      await axios
        .get("api/get-user-info/")
        .then((response) => {
          this.userStore.setUserInfo(response.data);

          this.$router.push("/");
        })
        .catch((error) => {
          console.log("error getting user info", error);
        });
    },
  },
};
</script>
