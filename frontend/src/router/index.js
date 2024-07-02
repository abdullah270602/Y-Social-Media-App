import { createRouter, createWebHistory } from 'vue-router'
import SignupView from '../views/SignUpView.vue'
import EmailSentView from '@/views/EmailSentView.vue'
import VerificationSuccessfulView from '@/views/VerificationSuccessfulView.vue'
import SignInView from '@/views/SignInView.vue' 
import FeedView from '@/views/FeedView.vue'
import SearchView from '@/views/SearchView.vue'
import ProfileView from '@/views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/emailSent',
      name: 'emailSent',
      component: EmailSentView
    },
    {
      path: '/VerificationSuccessful',
      name: 'VerificationSuccessful',
      component: VerificationSuccessfulView
    },
    {
      path: '/SignIn',
      name: 'SignIn',
      component: SignInView
    },
    {
      path: '/',
      name: 'feed',
      component: FeedView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/:username',
      name: 'profile',
      component: ProfileView
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ]
})

export default router
