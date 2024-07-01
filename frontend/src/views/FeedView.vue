<template>
    <main class="bg-white dark:bg-dim-900">
      <div class="container mx-auto h-screen">
        <div class="flex flex-row justify-center">
          <!-- Left -->
          <div class="w-68 xs:w-88 xl:w-275 h-screen">
            <div
              class="flex flex-col h-screen xl:pr-3 dark:bg-dim-900 fixed overflow-y-auto w-68 xs:w-88 xl:w-275"
            >
              
            </div>
          </div>
          <!-- /Left -->
  
          <!-- Middle -->
          <div class="w-full sm:w-600 h-screen">
            <CreatePost @postSubmitted="submitPostForm"></CreatePost>
  
            <div
              v-for="post in posts"
              :key="post.id"
              class="border border-gray-200 dark:bg-dim-900 dark:border-dim-200 hover:bg-gray-100 dark:hover:bg-dim-300 cursor-pointer transition duration-350 ease-in-out pb-4 border-r border-l"
            >
              <Post :post="post"></Post>
            </div>
          </div>
          <!--/Middle-->
  
          
          <!-- Right -->
          <div class="hidden md:block w-290 lg:w-350 h-screen ">
            <div
              class="flex flex-col fixed overflow-y-auto w-290 lg:w-350 h-screen dark:bg-dim-900 "
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
  import CreatePost from "../components/CreatePost.vue";
  
  
  export default {
    name: "FeedView",
    components: {
      Post,
      CreatePost,
    },
  
    data() {
      return {
        posts: [],
      };
    },
  
    mounted() {
      this.getFeed();
    },
  
    methods: {
      getFeed() {
        axios
          .get("api/posts/",)
          .then((response) => {
            console.log("data", response.data);
  
            this.posts = response.data;
          })
          .catch((error) => {
            console.log("Posts Error", error);
          });
      },
  
      submitPostForm(postBody) {
        console.log("submitPostForm", postBody);
  
        axios
          .post("api/posts/create/", { body: postBody })
          .then((response) => {
            console.log("Created Post", response.data);
            this.posts.unshift(response.data);
          })
          .catch((error) => {
            console.log("Error:", error);
          });
      },
    },
  };
  </script>
  
  
  