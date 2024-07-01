<template>
  <div>
    <div>
      <div class="flex flex-shrink-0 p-4 pb-0">
        <a href="#" class="flex-shrink-0 group block">
          <div class="flex items-top">
            <div>
              <img
                class="inline-block h-9 w-9 rounded-full"
                src="https://media.istockphoto.com/id/1419922260/photo/3d-render-of-a-cat-playing-video-games-with-a-vr-headset.webp?b=1&s=170667a&w=0&k=20&c=cOMTzhJgUbE_GRZUturqnUoZff1wEvSaiRNYD3Nc1HQ="
                alt=""
              />
            </div>
            <div class="ml-3">
              <p
                class="flex items-center text-base leading-6 font-medium text-gray-800 dark:text-white"
              >
                <p
         S         :to="{
                    name: 'profile',
                    params: { id: post.created_by.username },
                  }"
                  >{{ post.created_by.full_name }}
                </p>
                <span
                  class="ml-1 text-sm leading-5 font-medium text-gray-400 group-hover:text-gray-300 transition ease-in-out duration-150"
                >
                  {{ post.time_since_creation }} 
                </span>
              </p>
            </div>
          </div>
        </a>
      </div>
      <div class="pl-16">
        <p
          class="text-base width-auto font-medium text-gray-800 dark:text-white flex-shrink"
        >
          {{ post.body }}
        </p>

        <div class="flex my-3 mr-2 rounded-2xl border border-gray-600">
          <img class="rounded-2xl" src="" alt="" />
        </div>
      </div>
    </div>
  </div>
  <!-- /Tweet -->
</template>

<script>
export default {
  props: ["post"],
};
</script>
