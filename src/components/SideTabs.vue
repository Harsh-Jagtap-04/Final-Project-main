<template>
  <div class="tabs">
    <div class="tab-buttons">
      <button class="tab-button">Applicant Login</button>
      <button class="tab-button"> Find Eligible Scheme</button>
      <button class="tab-button"> User Manual</button>
      <button class="tab-button"> Notices </button>
      <button class="tab-button"> Grievance / Suggestions</button>
    </div>
  </div>
</template>

<script>
export default {
  // Component logic goes here
};
</script>

<style scoped>
.tabs {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  width: 25%; /* Adjust the width as needed */
  float: right; /* Float the Tabs to the right */
}

.tab-buttons {
  display: flex;
  flex-direction: column;
}

.tab-button {
  background-color: #43a047; /* Change the background color to #43A047 */
  color: #fff;
  border: none;
  padding: 24px 36px;
  border-radius: 3px;
  margin-bottom: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.tab-button:hover {
  background-color: #46e05f;
}

/* Add any other component-specific styles here */
</style>
