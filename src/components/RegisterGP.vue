<template>
    <div class="form-container"> 
    
      <div id="multi-step-form-container" class="mt-5">
        <!-- Form Steps / Progress Bar -->
    
        <!-- Step Wise Form Content -->
        <form
          id="userAccountSetupForm"
          name="userAccountSetupForm"
          enctype="multipart/form-data"
          method="POST"
          @submit.prevent="submitForm"
        >
          <!-- Step 1 Content -->
          <section id="step-1" class="form-step" :class="{ 'd-none': currentStep !== 1 }">
            <h1 class="text-center">Register Gram Panchayat</h1>
            <!-- Step 1 input fields -->
            
            <div class="mt-3">
      <div class="form-group col">
        <label class="full-name-label" for="select-ps">Select Panchayat Samiti</label>
        <select id="select-ps" class="form-control">
    <option value="category-1">Category 1</option>
    <option value="category-2">Category 2</option>
    <option value="category-3">Category 3</option>
  </select>
      </div>

      <div class="form-group col">
        <label class="full-name-label" for="gp-name">Gram Panchayat Name</label>
        <input type="text" id="gp-name" class="form-control" />
      </div>

      <div class="form-group col">
        <label class="full-name-label" for="pin-code">Pin Code</label>
        <input type="text" id="pin-code" class="form-control" />
      </div>
      <div class="form-group col">
      <label class="full-name-label" for="address">Address</label>
      <!-- <input type="text" id="residing-at" class="form-control" /> -->
      <textarea id="address" class="form-control"></textarea>
    </div>
  <!-- </div> -->
    <!-- <div class="mt-3"> -->
      <div class="form-group col">
        <label class="full-name-label" for="contact-no">Contact Number</label>
        <input type="number" id="contact-no" class="form-control" />
      </div>
      <div class="button-container">
  <button class="button submit-btn" type="submit">Submit</button>
</div>
    </div>
    <!-- </div> -->
  
        </section>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        currentStep: 1
      };
    },
    methods: {
      navigateToStep(stepNumber) {
        this.currentStep = stepNumber;
      },
      submitForm() {
        // Handle form submission
      }
    }
  };
  </script>
  
  <style scoped>
  /* Your CSS styles here */
  .d-flex {
    display: flex;
    align-items: center;
    background: linear-gradient(135deg, #71b7e6, #9b59b6);
  }
  
  /* Align buttons to opposite sides */
  .justify-content-between {
    justify-content: space-between;
  }
  .form-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
  }
  
  .form-group {
    flex: 1;
    margin-right: 1rem;
  }
  
  .form-group {
    /* display: flex;
    align-items: center; */
    margin-bottom: 1rem; /* Add some vertical spacing */
  }
  
  
  .full-name-label {
    display: flex;
    width: 50%; /* Adjust the width as needed */
    vertical-align: middle;
  }
  
  .file-input {
    display: inline-block;
    margin-top: 0.5rem;
  }
  
  
  /* Optional: Adjust form field widths if needed */
  .form-control {
    width: 100%;
    font-size: 20px;
  }
  
  
  h1 {
      text-align: center;
  }
  h2 {
      margin: 0;
  }
  #multi-step-form-container {
      margin-top: 5rem;
  }
  .form-container {
    background-color: #f9f8fd;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  }
  .text-center {
      text-align: center;
  }
  .mx-auto {
      margin-left: auto;
      margin-right: auto;
  }
  .pl-0 {
      padding-left: 0;
  }
  .button {
      padding: 0.7rem 1.5rem;
      border: 1px solid #4361ee;
      background-color: #4361ee;
      color: #fff;
      border-radius: 5px;
      cursor: pointer;
  }
  .submit-btn {
      border: 1px solid #0e9594;
      background-color: #0e9594;
  }
  .mt-3 {
      margin-top: 2rem;
  }
  .d-none {
      display: none;
  }
  .form-step {
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-radius: 20px;
      padding: 3rem;
  }
  .font-normal {
      font-weight: normal;
  }
  ul.form-stepper {
      counter-reset: inherit;
      margin-bottom: 3rem;
  }
  ul.form-stepper .form-stepper-circle {
      position: relative;
  }
  ul.form-stepper .form-stepper-circle span {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translateY(-50%) translateX(-50%);
  }
  .form-stepper-horizontal {
      position: relative;
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-pack: justify;
      -ms-flex-pack: justify;
      justify-content: space-between;
  }
  ul.form-stepper > li:not(:last-of-type) {
      margin-bottom: 0.625rem;
      -webkit-transition: margin-bottom 0.4s;
      -o-transition: margin-bottom 0.4s;
      transition: margin-bottom 0.4s;
  }
  .form-stepper-horizontal > li:not(:last-of-type) {
      margin-bottom: 0 !important;
  }
  .form-stepper-horizontal li {
      position: relative;
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      -webkit-box-align: start;
      -ms-flex-align: start;
      align-items: start;
      -webkit-transition: 0.5s;
      transition: 0.5s;
  }
  .form-stepper-horizontal li:not(:last-child):after {
      position: relative;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      height: 1px;
      content: "";
      top: 32%;
  }
  .form-stepper-horizontal li:after {
      background-color: #dee2e6;
  }
  .form-stepper-horizontal li.form-stepper-completed:after {
      background-color: #4da3ff;
  }
  .form-stepper-horizontal li:last-child {
      flex: unset;
  }
  ul.form-stepper li a .form-stepper-circle {
      display: inline-block;
      width: 40px;
      height: 40px;
      margin-right: 0;
      line-height: 1.7rem;
      text-align: center;
      background: rgba(0, 0, 0, 0.38);
      border-radius: 50%;
  }
  .form-stepper .form-stepper-active .form-stepper-circle {
      background-color: #4361ee !important;
      color: #fff;
  }
  .form-stepper .form-stepper-active .label {
      color: #4361ee !important;
  }
  .form-stepper .form-stepper-active .form-stepper-circle:hover {
      background-color: #4361ee !important;
      color: #fff !important;
  }
  .form-stepper .form-stepper-unfinished .form-stepper-circle {
      background-color: #f8f7ff;
  }
  .form-stepper .form-stepper-completed .form-stepper-circle {
      background-color: #0e9594 !important;
      color: #fff;
  }
  .form-stepper .form-stepper-completed .label {
      color: #0e9594 !important;
  }
  .form-stepper .form-stepper-completed .form-stepper-circle:hover {
      background-color: #0e9594 !important;
      color: #fff !important;
  }
  .form-stepper .form-stepper-active span.text-muted {
      color: #fff !important;
  }
  .form-stepper .form-stepper-completed span.text-muted {
      color: #fff !important;
  }
  .form-stepper .label {
      font-size: 1rem;
      margin-top: 0.5rem;
  }
  .form-stepper a {
      cursor: default;
  }
  .form-stepper-active .form-stepper-circle {
    background-color: #3b2273 !important;
  }
  .button-container {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}

.button-container button {
  width: 100%; /* Make the button span the full width */
}
  </style>
  