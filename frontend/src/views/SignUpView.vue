<template>
  <div
    class="bg-gray-50 dark:bg-gray-900 min-h-screen flex items-center justify-center"
  >
    <div
      class="w-full bg-white rounded-lg shadow dark:border sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
    >
      <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <div class="flex items-center justify-center ">
          <img
            class="w-8 h-8"
               src="../assets/Y-logo.png"
            alt="logo"
            style="width: 100px; height: 100px"
          />
        </div>
        <h1
          class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white text-center"
        >
          Create an account
        </h1>
        <form class="space-y-4 md:space-y-6" @submit.prevent="submitForm">
          <div>
            <label
              for="full name"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Your Full Name</label
            >
            <input
              type="text"
              class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-gray-600 focus:border-gray-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Dodge Why"
              v-model="form.full_name"
              @input="validateName"
              required
            />
            <span
              v-if="errors.full_name"
              class="text-red-500 text-xs focus:ring-red-500"
              >{{ errors.full_name }}</span
            >
          </div>
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
            <span v-else-if="emailValid" class="text-green-500 text-xs"
              >Email is valid</span
            >
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
            <div v-if="form.password">
              <span
                :class="{
                  'text-red-500 text-xs': !passwordCriteria.length,
                  'text-green-500 text-xs': passwordCriteria.length,
                }"
              >
                Minimum 8 characters </span
              ><br />
              <span
                :class="{
                  'text-red-500 text-xs': !passwordCriteria.uppercase,
                  'text-green-500 text-xs': passwordCriteria.uppercase,
                }"
              >
                Contains an uppercase letter </span
              ><br />
              <span
                :class="{
                  'text-red-500 text-xs': !passwordCriteria.number,
                  'text-green-500 text-xs': passwordCriteria.number,
                }"
              >
                Contains a number </span
              ><br />
            </div>
          </div>

          <div>
            <label
              for="date_of_birth"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Date of Birth</label
            >
            <input
              type="Date"
              class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              v-model="form.date_of_birth"
              required
            />
            <span v-if="errors.date_of_birth" class="text-red-500 text-xs">{{
              errors.date_of_birth
            }}</span>
          </div>

          <button
            type="submit"
            class="w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
            :disabled="formInvalid"
          >
            Sign up
          </button>
          <p class="text-sm font-light text-gray-500 dark:text-gray-400">
            Already have an account?

            <RouterLink
              :to="{ name: 'SignIn' }"
              class="font-medium text-blue-600 hover:underline dark:text-primary-500"
            >
              Sign in
            </RouterLink>
          </p>
        </form>
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
        // username: "",
        full_name: "",
        email: "",
        password: "",
        date_of_birth: "",
      },
      errors: {
        // username: "",
        full_name: "",
        email: "",
        password: "",
        date_of_birth: "",
      },
      passwordCriteria: {
        length: false,
        uppercase: false,
        lowercase: false,
        number: false,
      },
      emailValid: false,
    };
  },

  computed: {
    formInvalid() {
      return (
        this.errors.full_name ||
        this.errors.email ||
        this.errors.password ||
        this.errors.date_of_birth ||
        Object.values(this.passwordCriteria).includes(false)
      );
    },
  },

  methods: {
    async validateEmail() {
      if (!this.form.email) {
        this.errors.email = "Your email is missing";
      } else if (!this.validateEmailFormat(this.form.email)) {
        this.errors.email = "Invalid email format";
      } else {
        axios
          .post("api/check-email-exists/", { email: this.form.email })
          .then((response) => {
            console.log("response.data.exists: ", response.data.exists);
            if (response.data.exists) {
              this.errors.email = "Email already exists";
            } else {
              this.errors.email = "";
              this.emailValid = true;
            }
          })
          .catch((error) => {
            console.error(error);
            this.errors.email = "Error checking email";
          });
      }
    },

    validatePassword() {
      const password = this.form.password;
      this.passwordCriteria.length = password.length >= 8;
      this.passwordCriteria.uppercase = /[A-Z]/.test(password);
      this.passwordCriteria.lowercase = /[a-z]/.test(password);
      this.passwordCriteria.number = /\d/.test(password);
      if (Object.values(this.passwordCriteria).includes(false)) {
        this.errors.password = "Password does not meet criteria";
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
      console.log(this.form.date_of_birth);

      axios
        .post("/api/signup/", this.form)
        .then((response) => {
          if (response.status === 201) {
            // this.form.username = "";
            this.form.full_name = "";
            this.form.email = "";
            this.form.password = "";
            // this.form.password2 = "";
            this.form.date_of_birth = "";

            this.$router.push({ name: "emailSent" });
          } else {
            alert("Signup failed: " + response.data.errors); // add toast here
          }
        })
        .catch((error) => {
          console.error("Oh no ERROR", error);
        });
    },
  },
};
</script>
