import { createRouter, createWebHistory } from 'vue-router'; // Correct import for VueRouter

import HomePage from "@/components/HomePage.vue";
import AdminLogin from '@/components/AdminLogin.vue';
import AdminPage from "@/components/AdminPage.vue";


const routes = [
  { path: "/", component: HomePage },
  { path: "/adminlogin", component: AdminLogin }, // Add this line
  { path: "/admin", component: AdminPage },

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
