<template>
    <main class="bg-white dark:bg-dim-900">
      <div class="container mx-auto h-screen">
        <div class="flex flex-row justify-center">
          <!-- Left -->
          <div class="w-68 xs:w-88 xl:w-275 h-screen">
            <div
              class="flex flex-col h-screen xl:pr-3 fixed overflow-y-auto w-68 xs:w-88 xl:w-275"
            >
              <NavBar></NavBar>
            </div>
          </div>
          <!-- /Left -->
  
          <!-- Middle -->
          <div class="w-full sm:w-600 h-screen">
            <!-- Search -->
            <div class="relative mt-6 mx-2">
              <!-- <div
                class="absolute left-3 top-0 bottom-0 my-auto h-full text-gray-600 dark:text-gray-400 cursor-pointer"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="icon icon-tabler icon-tabler-mail"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path
                    d="M21.53 20.47l-3.66-3.66C19.195 15.24 20 13.214 20 11c0-4.97-4.03-9-9-9s-9 4.03-9 9 4.03 9 9 9c2.215 0 4.24-.804 5.808-2.13l3.66 3.66c.147.146.34.22.53.22s.385-.073.53-.22c.295-.293.295-.767.002-1.06zM3.5 11c0-4.135 3.365-7.5 7.5-7.5s7.5 3.365 7.5 7.5-3.365 7.5-7.5 7.5-7.5-3.365-7.5-7.5z"
                  ></path>
                </svg>
              </div> -->
  
              <form @submit.prevent="submitForm">
                <input
                  v-model="query"
                  class="w-full bg-gray-900 dark:bg-dim-400 border-gray-200 dark:border-dim-400 text-gray-900 focus:bg-gray-100 dark:focus:bg-dim-900 focus:outline-none focus:border focus:border-blue-200 font-normal h-9 pl-12 text-sm rounded-full border shadow"
                  placeholder="  What are you looking for?"
                />
              </form>
            </div>
            <!-- /Search -->
  
            <!-- AccountResults-->
            <div v-if="UserResults.length"
            class="mt-11">
              <div
                v-for="user in UserResults"
                :key="user.id"
                class="text-blue-400 text-sm font-normal p-3 border-b border-gray-200 dark:border-dim-200 hover:bg-gray-100 dark:hover:bg-dim-300 cursor-pointer transition duration-350 ease-in-out"
              >
                <div class="flex flex-row justify-between p-6 mt-4 ">
                  <div class="flex flex-row">
                    <img
                      class="w-10 h-10 rounded-full"
                      src="https://media.istockphoto.com/id/1419922260/photo/3d-render-of-a-cat-playing-video-games-with-a-vr-headset.webp?b=1&s=170667a&w=0&k=20&c=cOMTzhJgUbE_GRZUturqnUoZff1wEvSaiRNYD3Nc1HQ="
                      alt="Babar Azam"
                    />
                    <div class="flex flex-col ml-2">
                      <h1 class="text-gray-900 dark:text-white font-bold text-sm">
                        <a
                          :to="{ name: 'profile', params: { id: user.id } }"
                          >{{ user.full_name }}
                        </a>
                      </h1>
                      <p class="text-gray-400 text-sm">
                          @{{user.username}}
                      </p>
                    </div>
                  </div>
                  <div class="">
                    <div
                      class="flex items-center h-full text-gray-800 dark:text-white"
                    >
                      <!-- <a
                        href="#"
                        class="text-xs font-bold text-blue-400 px-4 py-1 rounded-full border-2 border-blue-400"
                        >Follow</a
                      > -->
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- /AccountResults-->

            <br>
            <br>
  
            <!--Post Results-->
            <div v-if="PostResults.length"
            class="mt-6">
              <div
                v-for="post in PostResults"
                :key="post.id"
                class="border border-gray-200 dark:bg-dim-900 dark:border-dim-200 hover:bg-gray-100 dark:hover:bg-dim-300 cursor-pointer transition duration-350 ease-in-out pb-4 border-l border-r"
              >
                <Post :post="post"></Post>
              </div>
            </div>
            <!--/Post Results-->
          </div>
          <!--/Middle-->
  
          <!-- Right -->
          <div class="hidden md:block w-290 lg:w-350 h-screen">
            <div
              class="flex flex-col fixed overflow-y-auto w-290 lg:w-350 h-screen"
            >
            </div>
          </div>
          <!-- /Right -->
        </div>
      </div>
      <RouterView />
    </main>
  </template>
  
  <script>
  import axios from "axios";
  import Post from "../components/Post.vue";
  import NavBar from "../components/NavBar.vue";
  
  export default {
    name: "SearchView2",
    components: {
      Post,
      NavBar,
    },
    data() {
      return {
        query: "",
        UserResults: [],
        PostResults: [],
      };
    },
  
    methods: {
      submitForm() {
        console.log("submitform", this.query);
  
        if (this.query.length === 0) {
          return;
        }
  
        axios
          .post("api/search/", {
            query: this.query,
          })
          .then((response) => {
            console.log("response", response.data);
            this.UserResults = response.data.user_results;
            this.PostResults = response.data.post_results;
          })
          .catch((error) => {
            console.log("error", error);
          });
      },
    },
  };
  </script>
  
  <style></style>
  