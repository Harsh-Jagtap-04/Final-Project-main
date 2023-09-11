import { createApp } from 'vue'; // Correct import for Vue
import App from './App.vue';
import router from './router'; // Correct import for VueRouter

const app = createApp(App);
app.use(router);
app.mount('#app');

