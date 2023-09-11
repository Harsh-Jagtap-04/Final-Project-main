<template>
  <div class="form-container"> 
    <!-- <button class="btn-go-back" @click="goBack">Go Back</button> -->
    <h1 class="h3"><i class="fa-brands fa-wpforms me-2"></i>Apply For Scheme</h1>

    <div id="multi-step-form-container" class="mt-5">

      <!-- Form Steps / Progress Bar -->
      <ul class="form-indicator form-stepper form-stepper-horizontal text-center mx-auto pl-0">
        <!-- Step 1 -->
        <li :class="{'form-stepper-active': currentStep === 1, 'form-stepper-unfinished': currentStep !== 1}" step="1">
          <a class="mx-2">
            <span class="form-stepper-circle">
              <span>1</span>
            </span>
            <div class="label">Letter - A</div>           
          </a>
        </li>
        <!-- Step 2 -->
        <li :class="{'form-stepper-active': currentStep === 2, 'form-stepper-unfinished': currentStep !== 2}" step="2">
          <a class="mx-2">
            <span class="form-stepper-circle text-muted">
              <span>2</span>
            </span>
            <div class="label text-muted">Documents</div>
          </a>
        </li>
        <!-- Step 3 -->
        <li :class="{'form-stepper-active': currentStep === 3, 'form-stepper-unfinished': currentStep !== 3}" step="3">
          <a class="mx-2">
            <span class="form-stepper-circle text-muted">
              <span>3</span>
            </span>
            <div class="label text-muted">Verification</div>
          </a>
        </li>
      </ul>
      <!-- Step Wise Form Content -->
      <form
      id="userAccountSetupForm"
      name="userAccountSetupForm"
      enctype="multipart/form-data"
      method="POST"
      @submit.prevent="submitForm"
      >
        <!-- Step 1 Content -->
      <section id="step-1" class="form-step form-spep-one" :class="{ 'd-none': currentStep !== 1 }">
          <h2 class="font-normal h5"><i class="h-6 fa-solid fa-user me-2"></i>User Basic Details</h2>
            <!-- Step 1 input fields -->
                <div class="row mt-3">
                    <div class="col-md-4 form-group">
                        <label class="form-label" for="first-name">First Name/प्रथम नाव<span class="text-danger">*</span></label>
                        <input type="text" id="ncharFirstName" class="form-control"  v-model="formData.ncharFirstName" placeholder="Enter First Name"/>
                    </div>
                    <div class="col-md-4 form-group">
                      <label class="form-label" for="middle-name">Middle Name/वडिलांचे नाव<span class="text-danger">*</span></label>
                      <input type="text" id="ncharMiddleName" class="form-control" v-model="formData.ncharMiddleName" placeholder="Enter Middle Name"/>
                    </div>
                    <div class="col-md-4 form-group">
                      <label class="form-label" for="last-name">Last Name/आडनाव<span class="text-danger">*</span></label>
                      <input type="text" id="ncharLastName" class="form-control" v-model="formData.ncharLastName" placeholder="Enter Last Name"/>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12 form-group">
                      <label class="form-label" for="residing-at">Residing At/राहणार<span class="text-danger">*</span></label>
                      <textarea id="ncharResidingAt" class="form-control" v-model="formData.ncharResidingAt" placeholder="Enter full address"></textarea>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 form-group">
                      <label class="form-label" for="taluka">Taluka/तालुका<span class="text-danger">*</span></label>
                      <input type="text" id="ncharTaluka" class="form-control" v-model="formData.ncharTaluka" placeholder="Enter taluka"/>
                    </div>
                    <div class="col-md-6 form-group">
                      <label class="form-label" for="district">District/जिल्हा<span class="text-danger">*</span></label>
                      <input type="text" id="ncharDistrict" class="form-control" v-model="formData.ncharDistrict" placeholder="Enter district" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 form-group">
                      <label class="form-label" for="poverty-line">BPL Number/दारिद्र्य रेषेखालील क्रमांक<span class="text-danger">*</span></label>
                      <input type="number" id="intBPLNumber" class="form-control" v-model="formData.intBPLNumber" placeholder="Enter BPL Number"/>
                    </div>
                    <div class="col-md-6 form-group">
                      <label class="form-label" for="group-number">Group Number/गट क्रमांक<span class="text-danger">*</span></label>
                      <input type="number" id="intGroupNumber" class="form-control" v-model="formData.intGroupNumber" placeholder="Enter Group Number" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 form-group">
                      <label class="form-label" for="total-land">Total Land/धारण केलेले एकुण क्षेत्र(आर)<span class="text-danger">*</span></label>
                      <input type="number" id="floatTotalLand" class="form-control" v-model="formData.floatTotalLand" placeholder="Enter Total Land"/>
                    </div>
                    <div class="col-md-6 form-group">
                      <label class="form-label" for="category">Category of Applicant/अर्जदाराचा संवर्ग<span class="text-danger">*</span></label>
                      <select id="ncharCategory" class="form-control" v-model="formData.ncharCategory" placeholder="">
                        <option selected disabled  value="category-1">Select Category of Applicant</option>
                        <option value="category-1">Category 1</option>
                        <option value="category-2">Category 2</option>
                        <option value="category-3">Category 3</option>
                      </select>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 form-group">
                      <label class="form-label" for="categorized">Categorized<span class="text-danger">*</span></label>
                      <input type="text" id="ncharCategorized" class="form-control" v-model="formData.ncharCategorized" placeholder="Categorized"/>
                    </div>
                    <div class="col-md-6 form-group">
                      <label class="form-label" for="irrigation-facility">Irrigation Facility/उपलब्ध असलेली सिंचन सुविधा<span class="text-danger">*</span></label>
                      <input type="text" id="ncharIrrigationFacility" class="form-control" v-model="formData.ncharIrrigationFacility" placeholder="Enter Irrigation Facility"/>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12 col-md-6 form-group">
                      <label class="form-label" for="form-Number">Form Number/प्राप्त अर्जाचा क्रमांक<span class="text-danger">*</span></label>
                      <input type="text" id="ncharFormNumber" class="form-control" v-model="formData.ncharFormNumber" placeholder="Enter Form Number"/>
                    </div>
                    <div class="col-12 col-md-6 form-group">
                      <label class="form-label" for="year">Year/वर्ष<span class="text-danger">*</span></label>
                      <input type="number" id="intYear" class="form-control" min="1900" max="2099" step="1"  v-model="formData.intYear" placeholder="Enter Year"/>
                    </div>
                </div>
                <div class="mt-3">
                  <button class="button btn-navigate-form-step" type="button" @click="navigateToStep(2)">Save and Next</button>
                </div>
                <ReportForm :formData="formData" />
      </section>
        <!-- Step 2 Content, default hidden on page load. -->
    
        <section id="step-2" class="form-step form-spep-one" :class="{ 'd-none': currentStep !== 2 }">
          <h2 class="font-normal h5"><i class=" fa-solid fa-file me-2"></i>Documents</h2>
          <div class="mt-4">
            <div class="form-group">
              <label class="form-label" for="extract-7-12" >Online Transcript of 7/12 / ७/१२ चा ऑनलाईन उतारा</label>
              <input type="file" id="blobExtract712" accept=".pdf, .jpg, .jpeg, .png" class="form-control" @change="handleFileChange('blobExtract712', $event)" />
              <!-- Add a button to view the uploaded document -->
    <button type="button" v-if="formData.blobExtract712" class="btn btn-link" @click="viewDocument('blobExtract712')">View Document</button>
            </div>
            <div class="form-group">
              <label class="form-label" for="form-8a">Online Transcript of Form 8A</label>
              <input type="file" id="blobForm8A" accept=".pdf, .jpg, .jpeg, .png" class="form-control"  @change="handleFileChange('blobForm8A', $event)" />
            </div>
            <div class="form-group">
              <label class="form-label" for="job-card">Copy of Job Card/ जॉबकार्ड ची प्रत</label>
              <input type="file" id="blobJobCard" accept=".pdf, .jpg, .jpeg, .png" class="form-control" @change="handleFileChange('blobJobCard', $event)"/>
            </div>
            <div class="form-group">
              <label class="form-label" for="additional-land-affidavit">Additional Land Ownership Affidavit/</label>
              <input type="file" id="blobAdditionalLandAffidavit" accept=".pdf, .jpg, .jpeg, .png" class="form-control" @change="handleFileChange('blobAdditionalLandAffidavit', $event)"/>
            </div>
            <div class="form-group">
              <label class="form-label" for="water-usage-agreement">Water Usage Agreement</label>
              <input type="file" id="blobWaterUsageAgreement" accept=".pdf, .jpg, .jpeg, .png" class="form-control" @change="handleFileChange('blobWaterUsageAgreement', $event)" />
            </div>
          </div>
          <div class="mt-3 d-flex justify-content-between old_backgraund">
            <button class="button btn-navigate-form-step" type="button" @click="navigateToStep(1)">Prev</button>
            <button class="button btn-navigate-form-step" type="button" @click="navigateToStep(3)">Save and Next</button>
          </div>
      </section>
      <!-- Step 3 Content -->
      <section id="step-3" class="form-step form-spep-one" :class="{ 'd-none': currentStep !== 3 }">
        <h2 class="font-normal h5"><i class="fa-solid fa-circle-info me-2"></i>Personal Details</h2>
        <div class="mt-3">
          <div class="form-group">
            <label class="form-label" for="aadhar-number">Aadhar Number/आधार कार्ड नंबर</label>
            <input type="text" id="ncharAadharNumber" class="form-control" v-model="formData.ncharAadharNumber" placeholder="Enter Aadhar Number" />
          </div>
          <div class="form-group">
            <label class="form-label" for="mobile-number">Mobile Number/मोबाईल नंबर</label>
            <input type="text" id="ncharMobileNumber" class="form-control" v-model="formData.ncharMobileNumber" placeholder="Enter mobile number" />
          </div>
          <div class="form-group">
            <label class="form-label" for="witness-1">Witness 1/साक्षीदार 1</label>
            <input type="text" id="ncharWitness1" class="form-control" placeholder="Enter your full Name " v-model="formData.ncharWitness1"/>
          </div>
          <div class="form-group">
            <label class="form-label" for="witness-2">Witness 2/साक्षीदार 2</label>
            <input type="text" id="ncharWitness2" class="form-control" placeholder="Enter your full Name"  v-model="formData.ncharWitness2"/>
          </div>
  </div>

  <!-- File Uploads and Buttons -->
  <div class="mt-3">
    <!-- File uploads ... -->

    <div class="d-flex justify-content-between mt-3 old_backgraund">
      <button class="button btn-navigate-form-step" type="button" @click="navigateToStep(2)">Prev</button>
      <button class="button submit-btn" type="submit">Save</button>
    </div>
  </div>
</section>


      </form>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ReportForm from './ReportForm.vue';

export default {
  props: {
    selectedScheme: Object, // Pass the selected scheme as a prop
  },
  components: {
    ReportForm, // Register the child component
  },
  data() {
    return {
      currentStep: 1,
      mstVihirId: '',
      formData: {
        ncharFirstName: '',
        ncharMiddleName: '',
        ncharLastName: '',
        ncharResidingAt: '',
        ncharTaluka: '',
        ncharDistrict: '',
        intBPLNumber: null,
        intGroupNumber: null,
        floatTotalLand: null,
        ncharCategory: '',
        ncharCategorized: '',
        ncharIrrigationFacility: '',
        ncharFormNumber: '',
        intYear: null,
        ncharAadharNumber: '',
        ncharMobileNumber: '',
        ncharWitness1: '',
        ncharWitness2: '',
        // Add fields for documents
        blobExtract712: null,
        blobForm8A: null,
        blobJobCard: null,
        blobAdditionalLandAffidavit: null,
        blobWaterUsageAgreement: null
      }
    };
  },
  methods: {
    viewDocument(fieldName) {
      // Get the base64-encoded document data from the formData
      const documentData = this.formData[fieldName];

      // Create a new window or tab to display the document
      const viewerWindow = window.open('', '_blank');
      viewerWindow.document.open();
      // Depending on the document type (e.g., PDF, image), you may need to set the appropriate content type
      // For example, for PDF:
      viewerWindow.document.write(`<embed width="100%" height="100%" src="data:application/pdf;base64,${documentData}" type="application/pdf" />`);

      viewerWindow.document.close();
    },
    navigateToStep(stepNumber) {
      this.currentStep = stepNumber;
    },
  
    handleFileChange(fieldName, event) {
  const selectedFile = event.target.files[0];

  if (selectedFile) {
    // Read the selected file as a Data URL (base64)
    const reader = new FileReader();

    reader.onload = () => {
      // Extract the Base64 content without the data URI prefix
      const base64Content = reader.result.split(',')[1];

      // Store the Base64 data in formData
      this.formData[fieldName] = base64Content;
    };

    reader.readAsDataURL(selectedFile);
  }
},
goBack() {
      // Emit an event to inform the parent component to go back to "Available Schemes"
      this.$emit('go-back');
    },

    submitFirstPart() {
      const firstPartData = {
        ncharFirstName: this.formData.ncharFirstName,
      ncharMiddleName: this.formData.ncharMiddleName,
      ncharLastName: this.formData.ncharLastName,
      ncharResidingAt: this.formData.ncharResidingAt,
      ncharTaluka: this.formData.ncharTaluka,
      ncharDistrict: this.formData.ncharDistrict,
      intBPLNumber: this.formData.intBPLNumber,
      intGroupNumber: this.formData.intGroupNumber,
      floatTotalLand: this.formData.floatTotalLand,
      ncharCategory: this.formData.ncharCategory,
      ncharCategorized: this.formData.ncharCategorized,
      ncharIrrigationFacility: this.formData.ncharIrrigationFacility,
      ncharFormNumber: this.formData.ncharFormNumber,
      intYear: this.formData.intYear,
        // ... other fields from the first part
      };
      console.log(firstPartData)
      axios.post('http://127.0.0.1:5555/saveVihirInfo', firstPartData, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        console.log('First part saved:', response.data);
        // Continue with the next part of the form submission
        this.mstVihirId = response.data.id;
        console.log(this.mstVihirId)

// Continue with the next part of the form submission
this.submitSecondPart();
      })
      .catch(error => {
        console.error('Error saving first part:', error);
        // Handle error scenario for the first part
      });
    },

    submitSecondPart() {
      const mstVihirId = parseInt(this.mstVihirId);

// Create the object to send to the server
const documentData = {
  mstVihirId: mstVihirId,
  blobExtract712: this.formData.blobExtract712,
  blobForm8A: this.formData.blobForm8A,
  blobJobCard: this.formData.blobJobCard,
  blobAdditionalLandAffidavit: this.formData.blobAdditionalLandAffidavit,
  blobWaterUsageAgreement: this.formData.blobWaterUsageAgreement
};
console.log(documentData)
// Send the base64-encoded documents to your backend API
axios.post('http://127.0.0.1:5555/saveVihirDocuments', documentData, {
  headers: {
    'Content-Type': 'application/json',
  },
})
.then((response) => {
  console.log('Documents saved:', response.data);
  // Continue with other parts of the form submission if needed
  this.submitThirdPart();
})
.catch((error) => {
  console.error('Error saving documents:', error);
  // Handle error scenario for document submission
});
},

    submitThirdPart() {
      const thirdPartData = {
        mstVihirId: this.mstVihirId,
        ncharAadharNumber: this.formData.ncharAadharNumber,
        ncharMobileNumber: this.formData.ncharMobileNumber,
        ncharWitness1: this.formData.ncharWitness1,
        ncharWitness2: this.formData.ncharWitness2,
        // ... other fields from the third part
      };

      axios.post('http://127.0.0.1:5555//saveVihirVerification', thirdPartData, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        console.log('Third part saved:', response.data);
        // Reset form fields and show success message

        this.resetForm();
        alert('Application submitted successfully');
      })
      .catch(error => {
        console.error('Error saving third part:', error);
        // Handle error scenario for the third part
      });
    },

    resetForm() {
      // Clear form fields
      this.formData.ncharFirstName = '';
        this.formData.ncharMiddleName = '';
        this.formData.ncharLastName = '';
        this.formData.ncharResidingAt = '';
        this.formData.ncharTaluka = '';
        this.formData.ncharDistrict = '';
        this.formData.intBPLNumber = null;
        this.formData.intGroupNumber = null;
        this.formData.floatTotalLand = null;
        this.formData.ncharCategory = '';
        this.formData.ncharCategorized = '';
        this.formData.ncharIrrigationFacility = '';
        this.formData.ncharFormNumber = '';
        this.formData.intYear = null;
        this.formData.ncharAadharNumber = '';
        this.formData.ncharMobileNumber = '';
        this.formData.ncharWitness1 = '';
        this.formData.ncharWitness2 = '';
        this.formData.blobExtract712 = null;
        this.formData.blobForm8A = null;
        this.formData.blobJobCard = null;
        this.formData.blobAdditionalLandAffidavit = null;
        this.formData.blobWaterUsageAgreement = null;
      // ... reset other fields
      this.currentStep = 1; // Reset step to 1
    },

    submitForm() {
      // Start the submission process by submitting the first part
      this.submitFirstPart();
    }
  }
};
   
</script>

<style scoped>
/* Your CSS styles here */
.btn-go-back {
  background-color: #007bff; /* Updated color */
  border-color: #007bff; /* Updated color */
  color: #fff; /* Updated color */
  border-radius: 5px;
  padding: 0.7rem 1.5rem;
  cursor: pointer;
  position: relative;
  top: 10px;
  right: 10px;
}

.btn-go-back:hover {
  background-color: #0056b3; /* Hover color */
}

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

.old_backgraund
{
  background: none !important;
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
.form-spep-one label.form-label span
{
    margin: 0 5px;
}
.form-spep-one [placeholder]::placeholder
{
    text-transform: capitalize;
    opacity: .7;
    font-size: 13px;
}
.form-spep-one [placeholder]
{
    border-radius: 7px;
    border: 1px solid rgba(0,0,0,.5);
    padding: 5px 20px !important;
}
.form-spep-one label.form-label
{
    font-size: 14px;
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