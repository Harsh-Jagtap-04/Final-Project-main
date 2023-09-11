<template>
  <div class="sidebar1">
    <h2 class="sidebar1-title">Instructions</h2>
    <p class="sidebar1-text">Follow these steps to apply for the scheme:</p>
    <ul class="instruction-list">
      <li class="instruction-item">
        <span class="step-number">1</span> Enter your Email.
      </li>
      <li class="instruction-item">
        <span class="step-number">2</span> Enter your OTP.
      </li>
      <li class="instruction-item">
        <span class="step-number">3</span> Click on login.
      </li>
      <li class="instruction-item">
        <span class="step-number">4</span> Apply for the scheme.
      </li>
    </ul>
  </div>
</template>

<style scoped>
.sidebar1 {
  background-color:  #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  width: 300px;
  float: left;
  text-align: left;
  margin-right: 20px;
}

.sidebar1-title {
  font-size: 24px;
  margin-bottom: 10px;
  color: #333;
}

.sidebar1-text {
  font-size: 16px;
  margin-bottom: 15px;
  color: #555;
}

.instruction-list {
  list-style-type: none;
  padding: 0;
}

.instruction-item {
  font-size: 16px;
  margin-bottom: 10px;
  display: flex;
  align-items: flex-start;
  color: #444;
}

.step-number {
  width: 25px; /* Fixed width for all step numbers */
  height: 25px; /* Fixed height for all step numbers */
  background-color: #4CAF50;
  color: #fff;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  margin-right: 15px; /* Adjust the margin to add space between number and text */
  font-size: 18px;
}

/* Add hover effect for step numbers */
.step-number:hover {
  background-color: #45a049;
}

/* Add a subtle border to the sidebar1 for separation */
.sidebar1::before {
  content: '';
  display: block;
  width: 4px;
  background-color: #4CAF50;
  height: 100%;
  position: absolute;
  top: 0;
  left: -4px;
}
</style>
