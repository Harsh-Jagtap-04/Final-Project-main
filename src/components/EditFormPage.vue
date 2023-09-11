<template>
    <div>
      <h1 class="text-center">Edit Application Form</h1>
      
      <!-- Form -->
      <form id="editForm" @submit.prevent="submitForm">
        <!-- Step 1 Content -->
        <section id="step-1" class="form-step" :class="{ 'd-none': currentStep !== 1 }">
          <!-- Step 1 input fields -->
          <div class="mt-3">
            <!-- ... Your step 1 input fields ... -->
          </div>
          <div class="mt-3">
            <button class="button btn-navigate-form-step" type="button" @click="navigateToStep(2)">Next</button>
          </div>
        </section>
  
        <!-- Step 2 Content -->
        <section id="step-2" class="form-step" :class="{ 'd-none': currentStep !== 2 }">
          <!-- Step 2 input fields -->
          <div class="mt-3">
            <!-- ... Your step 2 input fields ... -->
          </div>
          <div class="mt-3">
            <button class="button btn-navigate-form-step" type="button" @click="navigateToStep(1)">Prev</button>
            <button class="button btn-navigate-form-step" type="button" @click="navigateToStep(3)">Next</button>
          </div>
        </section>
  
        <!-- Step 3 Content -->
        <section id="step-3" class="form-step" :class="{ 'd-none': currentStep !== 3 }">
          <!-- Step 3 input fields -->
          <div class="mt-3">
            <!-- ... Your step 3 input fields ... -->
          </div>
          <div class="mt-3">
            <button class="button btn-navigate-form-step" type="button" @click="navigateToStep(2)">Prev</button>
            <button class="button submit-btn" type="submit">Save</button>
          </div>
        </section>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        currentStep: 1,
        formData: {
          firstName: 'John',
          middleName: 'Doe',
          lastName: 'Smith',
          // ... Other pre-filled data ...
        },
      };
    },
    methods: {
      navigateToStep(stepNumber) {
        this.currentStep = stepNumber;
      },
      submitForm() {
        // Handle form submission
        // Update the data or send it to the server
      },
    },
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
  
  </style>
  