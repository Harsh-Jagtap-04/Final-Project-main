<template>
  <div class="main-content w-100">

    <MultiStepForm v-if="activeTab === 'apply_scheme'"/>

    <DashboardPage v-else-if="activeTab === 'dashboard'"  @select-option="selectOption" />

    <SchemeTable v-else-if="activeTab === 'schemes'" @tab-change="updateActiveTab"/>
    <ApplicationPage
      v-else-if="activeTab === 'applications'"
      @update:activeTab="updateActiveTab"
    />
    <EditFormPage v-else-if="activeTab === 'edit_form'" />

    <AdministrationPage v-else-if="activeTab === 'administration'"  @select-option="selectOption" />

    
  </div>
</template>

<script>
import MultiStepForm from "@/components/MultiStepForm.vue";
import DashboardPage from "@/components/DashboardPage.vue";
import SchemeTable from "@/components/SchemeTable.vue";
import ApplicationPage from "@/components/ApplicationPage.vue";
import EditFormPage from "@/components/EditFormPage.vue";
import AdministrationPage from "@/components/AdministrationPage.vue";


export default {
  components: {
    MultiStepForm,
    DashboardPage,
    SchemeTable,
    ApplicationPage,
    EditFormPage,
    AdministrationPage
  },
  props: {
    activeTab: String
  },
  data() {
    return {
      selectedOption: null
    };
  },
  methods: {
    updateActiveTab(tabName) {
      this.$emit('update:activeTab', tabName); // Forward the event to App.vue
    },
    selectOption(option) {
      this.selectedOption = option;
    },
  },
};
</script>

<style scoped>
/* Main content styles */
.main-content {
  padding: 40px;
  background-color: #ffffff;
  box-shadow: 0 0 2px var(--grey-color-light);
  margin-top: 30px;
  margin-left: 260px;
}
</style>
