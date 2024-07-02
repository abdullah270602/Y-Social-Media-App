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
            <!--Profile-->
            <div
              class="text-gray-900 dark:bg-dim-900 dark:text-white text-md font-bold p-3 border border-gray-200 dark:border-dim-200"
            >
              <img
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQq5_JvyIL-RDm7skjduw5wJz1hQwk9UimpMA&s"
              class="mb-6 mx-auto rounded"
              />
  
              <p
                class="text-gray-900 dark:text-white font-bold text-center text-lg"
              >
                <strong>{{ user.full_name }}</strong>
                
              </p>
              <p
              class="text-gray-900 dark:text-white font-bold text-center text-sm">
                <span>@{{ user.username }}</span>
              </p>
  
              <div class="mt-6 flex space-x-8 justify-center">
                <a
                  :to="{ name: 'followers', params: { username: user.username } }"
                  class="text-xs text-gray-500 no-underline hover:underline cursor-pointer"
                >
                  {{ followerFollowingData.followers_count }} Followers
                </a>
                <a
                  :to="{ name: 'following', params: { username: user.username } }"
                  class="text-xs text-gray-500 no-underline hover:underline cursor-pointer"
                >
                  {{ followerFollowingData.following_count }}
                  Following</a
                >
                <p class="text-xs text-gray-500">{{ postCount }} posts</p>
              </div>
  
              <div v-if="userStore.user.username != user.username">
                <!--Follow button-->
                <div
                  v-if="isFollowing == false"
                  class="mt-6 mx-auto flex justify-center"
                >
                  <button
                    class="bg-blue-400 hover:bg-blue-700 text-white rounded-full py-2 px-6"
                    @click="sendFollowRequest"
                  >
                    Follow
                  </button>
                </div>
                <!--/Follow button-->
  
                <!--UnFollow button-->
                <div v-if="isFollowing" class="mt-6 mx-auto flex justify-center">
                  <button
                    class="bg-sky-500 hover:bg-red-500 text-white rounded-full py-2 px-6"
                    @click="sendUnfollowRequest"
                    @mouseenter="hovering = true"
                    @mouseleave="hovering = false"
                  >
                    <span v-if="!hovering">Following</span>
                    <span v-else>Unfollow</span>
                  </button>
                </div>
              </div>
              <!--/UnFollow button-->
            </div>
            <!--/Profile-->
  
            <!-- Nav -->
            <div
              class="text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:text-gray-400 dark:border-gray-700"
            >
              <ul class="flex flex-wrap -mb-px justify-evenly">
                <li class="me-2">
                  <a
                    href="#"
                    class="inline-block p-4 text-blue-600 border-b-2 border-blue-600 rounded-t-lg dark:text-blue-500 dark:border-blue-500"
                    >Posts</a
                  >
                </li>
                <li class="me-2">
                  <a
                    class="inline-block p-4 border-b-2 border-transparent rounded-t-lg active hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300"
                    >Replies</a
                  >
                </li>
                <li class="me-2">
                  <RouterLink
                    
                    class="inline-block p-4 border-b-2 border-transparent rounded-t-lg active hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300"
                    >Likes</RouterLink
                  >
                </li>
              </ul>
            </div>
            <!-- /Nav -->
  
            <div v-if="userStore.user.username == user.username">
              <CreatePost @postSubmitted="sumbitPostForm"></CreatePost>
            </div>
  
            <!--Posts-->
            <div
              v-for="post in posts"
              :key="post.id"
              class="border border-gray-200 dark:bg-dim-900 dark:border-dim-200 hover:bg-gray-100 dark:hover:bg-dim-300 cursor-pointer transition duration-350 ease-in-out pb-4 border-l border-r"
            >
              <Post :post="post"></Post>
            </div>
            <!--/Posts-->
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
  import { useUserStore } from "../stores/user";
  import Post from "../components/Post.vue";
  import CreatePost from "../components/CreatePost.vue";
  import NavBar from "../components/NavBar.vue";
//   import ProfileLikesView from "./ProfileLikesView.vue";
  
  export default {
    name: "FeedView",
    components: {
      Post,
      CreatePost,
      NavBar,
    //   ProfileLikesView,
    },
  
    setup() {
      const userStore = useUserStore();
  
      return {
        userStore,
      };
    },
  
    data() {
      return {
        user: {},
        posts: [],
        followerFollowingData: {},
        body: "",
        isFollowing: false,
        hovering: false,
      };
    },
    computed: {
      postCount() {
        return this.posts.length;
      },
    },
  
    mounted() {
      this.getFeed();
      this.checkFollowRelationship();
      this.getUserFollowingAndFollowersCount();
    },
  
    // To laod the feed according to the profile
    watch: {
      $route: "getFeed",
    },
  
    methods: {
      getFeed() {
        axios
          .get(`api/posts/get_users_post_list/${this.$route.params.username}`)
          .then((response) => {
            console.log("data", response.data);
  
            this.user = response.data.user;
            this.posts = response.data.posts;
          })
          .catch((error) => {
            console.log("Posts Error", error);
          });
      },
  
      checkFollowRelationship() {
        axios
          .get(`api/check-follow-relationship/${this.$route.params.username}`)
          .then((response) => {
            console.log("check-follow-relationship", response);
  
            this.isFollowing = response.data.is_following;
          })
          .catch((error) => {
            console.log("check-follow-relationship Error", error);
          });
      },
  
      sumbitPostForm(postBody) {
        console.log("submitPostForm", postBody);
  
        axios
          .post("api/posts/create/", { body: postBody })
          .then((response) => {
            console.log("data", response.data);
            this.posts.unshift(response.data);
          })
          .catch((error) => {
            console.log("Error:", error);
          });
      },
  
      sendFollowRequest() {
        console.log("Follow Request");
        axios
          .post(`api/follow/${this.$route.params.username}`)
          .then((response) => {
            console.log("follow", response);
            if (response.data.followed) {
              this.isFollowing = true;
              this.followerFollowingData.followers_count += 1;
            }
          })
          .catch((error) => {
            console.log("Follow Error", error);
          });
      },
      sendUnfollowRequest() {
        console.log("UnFollow Request");
        axios
          .post(`api/unfollow/${this.$route.params.username}`)
          .then((response) => {
            console.log("Unfollow", response);
            if (response.data.unfollowed) {
              this.isFollowing = false;
              this.followerFollowingData.followers_count -= 1;
            }
          })
          .catch((error) => {
            console.log("Unfollow Error", error);
          });
      },
  
      getUserFollowingAndFollowersCount() {
        console.log("get-user-following-and-followers");
        axios
          .get(
            `api/get-user-following-and-followers-count/${this.$route.params.username}`
          )
          .then((response) => {
            console.log("getUserFollowingAndFollowersCount", response.data);
            this.followerFollowingData = response.data.data;
          })
          .catch((error) => {
            console.log("getUserFollowingAndFollowersCount Error", error);
          });
      },
    },
  };
  </script>
  
  <style></style>
  