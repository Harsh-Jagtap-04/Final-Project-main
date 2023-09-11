<template>
  <div class="dashboard">
    <div v-if="showDashboard" class="dashboard-options">
      <div class="dashboard-block" @click="selectOption('schemes')">
        <div class="block-content">
          <h2>Schemes</h2>
          <br>
          <p>Total Schemes</p>
          <span class="total-number">{{ totalSchemes }}</span>
        </div>
      </div>
      <div class="dashboard-block" @click="selectOption('applications')">
        <div class="block-content">
          <h2>Submitted Applications</h2>
          <br>
          <p>Total Applications</p>
          <span class="total-number">{{ totalApplications }}</span>
        </div>
      </div>
      <!-- Add more blocks for other options -->
    </div>
    <div v-else>
      <button class="go-back-button" @click="goBack">Go Back</button>
      <component :is="selectedOptionComponent" />
    </div>
  </div>
</template>

<script>
import SchemeTable from "@/components/SchemeTable.vue";
import ApplicationPage from "@/components/ApplicationPage.vue";
// ... (import other components)

export default {
  name: 'DashboardPage',
  components: {
    SchemeTable,
    ApplicationPage,
    // ... (other components)
  },
  data() {
    return {
      selectedOption: null,
      totalSchemes: 1, // Replace with the actual number of schemes
      totalApplications: 14,
      showDashboard: true, 
    };
  },
  computed: {
    selectedOptionComponent() {
      return this.selectedOption === 'schemes'
        ? 'SchemeTable'
        : this.selectedOption === 'applications'
        ? 'ApplicationPage'
        : null;
    }
  },
  methods: {
  selectOption(option) {
    this.selectedOption = option;
    this.showDashboard = false; // Hide the dashboard when an option is selected
  },
  goBack() {
    this.selectedOption = null; // Reset the selected option
    this.showDashboard = true; // Show the dashboard again
  }
},
};
</script>


<style scoped>
.go-back-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.go-back-button:hover {
  background-color: #0056b3;
}

.dashboard {
  padding: 40px;
  background-color: #f7f7f7; /* Use a light background color for the dashboard */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px; /* Add some border-radius for a softer look */
}

.dashboard-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive grid */
  gap: 20px;
  max-width: 1000px; /* Adjust the maximum width as needed */
  margin: 0 auto; /* Center the grid horizontally */
  padding: 20px;
}

.dashboard-block {
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  text-align: center;
  width: 100%; /* Ensure each block takes up the full width */
}

.dashboard-block:hover {
  transform: translateY(-5px);
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
}

.block-content {
  text-align: center;
}

.block-content h2 {
  margin: 0;
  font-size: 24px; /* Increase the font size to your desired value, e.g., 24px */
  color: #333;
}


/* Add some hover effects for the dashboard blocks */
.dashboard-block:hover .block-content h2 {
  color: #007bff; /* Change text color on hover */
}

/* Add a subtle gradient to the dashboard blocks */
.dashboard-block::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 255, 0.6) 100%);
  pointer-events: none;
  z-index: -1;
  border-radius: 8px;
  opacity: 0;
  transition: opacity 0.2s;
}

.dashboard-block:hover::before {
  opacity: 1;
}

/* Style the selected option differently */
.dashboard-options .dashboard-block.selected {
  background-color: #007bff; /* Change background color */
  color: #fff; /* Change text color */
  border-color: #007bff; /* Change border color */
}

.dashboard-options .dashboard-block.selected:hover {
  transform: translateY(0); /* Remove hover effect */
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
}

/* Add a subtle gradient to the selected dashboard block */
.dashboard-options .dashboard-block.selected::before {
  background: linear-gradient(to bottom, rgba(0, 123, 255, 0.8) 0%, rgba(0, 123, 255, 0.6) 100%);
}

/* Adjust the padding inside the selected block */
.dashboard-options .dashboard-block.selected .block-content {
  padding: 30px;
}

/* Center the content vertically inside the blocks */
.block-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
}

/* Style the total numbers */
.total-number {
  font-size: 24px; /* Adjust the font size */
  font-weight: bold; /* Make the text bold */
  color: #007bff; /* Set the text color */
}
</style>