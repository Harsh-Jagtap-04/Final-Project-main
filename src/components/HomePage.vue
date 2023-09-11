<template>
    <div class="government-page">
      <header class="header-container">
        <!-- Header content goes here -->
      </header>
      <NavBar />
      <div class="content">
        <div class="flex-container">
          <UserSideBar />
          <LoginForm />
          <SideTabs />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import UserSideBar from '@/components/UserSideBar.vue';
  import LoginForm from '@/components/LoginForm.vue';
  import SideTabs from '@/components/SideTabs.vue';
  import NavBar from '@/components/NavBar.vue'
  
  export default {
    name: "HomePage",
    components: {
      UserSideBar,
      LoginForm,
      SideTabs,
      NavBar
    },
    // Component logic goes here
  };
  </script>
  
  <style scoped>
  .government-page {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
  }
  
  header {
    background-color: #ccc;
    padding: 10px 20px;
    display: flex;
    align-items: center;
  }
  
  .header-container {
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    position: relative;
    overflow: hidden;
  }
  
  .logo {
    width: 100px;
    margin-right: 20px;
  }
  
  .content {
    margin-top: 20px; /* Add some top margin to separate content from header */
  }
  
  .flex-container {
    display: flex;
    justify-content: space-between; /* Create horizontal layout */
  }
  
  /* Add any other homepage-specific styles here */
  </style>
  