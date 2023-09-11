<template>
    <div>
      <NavBarAdmin/>
      <div class="sitebar_body">
      <SideBar :active-tab="activeTab" @tab-change="updateActiveTab" />
      <MainContent :active-tab="activeTab" @update:activeTab="updateActiveTab" />
      </div>
    </div>
</template>
  
  <script>
  import SideBar from "@/components/SideBar.vue";
  import MainContent from "@/components/MainContent.vue";
  import NavBarAdmin from "@/components/NavBarAdmin.vue";
  
  export default {
    components: {
      SideBar,
      MainContent,
      NavBarAdmin
    },
    data() {
      return {
        activeTab: "dashboard" // Set the default active tab to "dashboard"
      };
    },
    methods: {
      updateActiveTab(tabName) {
        this.activeTab = tabName;
      }
    }
  };
  </script>