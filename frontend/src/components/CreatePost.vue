<template>
    <!-- New Post -->
    <div
      class="border border-gray-200 dark:border-dim-200 pb-4 border-l border-r"
    >
      <div class="flex flex-shrink-0 p-4 pb-0">
        <div class="w-12 flex items-top">
          <img class="inline-block h-10 w-10 rounded-full" 
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQq5_JvyIL-RDm7skjduw5wJz1hQwk9UimpMA&s"
          alt="" />
        </div>
        <div class="w-full p-2">
          <form action="post">
            <textarea
              v-model="body"
              class="dark:text-white text-gray-900 placeholder-gray-400 w-full h-10 bg-transparent border-0 focus:outline-none resize-none"
              placeholder="Kya chla bhai?"
            ></textarea>
          </form>
        </div>
      </div>
      <div class="w-full flex items-top p-2 text-white pl-14">
        <button
          type="submit"
          class="bg-blue-400 hover:bg-blue-500 text-white rounded-full py-1 px-4 ml-auto mr-1"
          :class="{ 'opacity-50': !isBodyValid }"
          :disabled="!isBodyValid"
          @click.prevent="sumbitPost"
        >
          <span class="font-semibold text-sm">Post</span>
        </button>
      </div>
    </div>
    <!-- /New Post -->
  </template>
  
  <script>
  export default {
      data() {
      return {
        body: "",
      };
    },
    computed: {
      isBodyValid() {
        // Check if body is not empty and doesn't contain only spaces
        let temp = this.body
        return temp.trim() !== "";
      }
    },
      methods: {
          sumbitPost(){
              this.$emit('postSubmitted', this.body)
              this.body = ''
          }
      }
  };
  </script>
  