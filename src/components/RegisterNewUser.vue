<template>
  <div class="form-container">
    <div id="multi-step-form-container" class="mt-5">
      <!-- Form Steps / Progress Bar -->
      <!-- Step Wise Form Content -->
      <form id="userRegistrationForm" name="userRegistrationForm" enctype="multipart/form-data" method="POST"
        @submit.prevent="submitForm">
        <!-- Step 1 Content -->
        <section id="step-1" class="add-user-form form-step form-spep-one" :class="{ 'd-none': currentStep !== 1 }">
          <h2 class="font-normal h5 text-left mb-2"><i class="fa-solid fa-user me-2 h5"></i>Register New User</h2>
          <div class="row">
            <div class="form-group col-md-6">
              <label class="form-label">Full Name<span class="text-danger">*</span></label>
              <input type="text" id="full-name" class="form-control" placeholder="Enter full name"
                v-model="formData.ncharFullName" />
            </div>
            <div class="form-group col-md-6">
              <label for="username" class="form-label">Username<span class="text-danger">*</span></label>
              <input type="text" id="username" class="form-control" placeholder="Enter Username"
                v-model="formData.ncharUsername" />
            </div>
          </div>
          <div class="row">
            <div class="form-group col-md-6">
              <label for="password" class="form-label">Password<span class="text-danger">*</span></label>
              <input type="password" id="password" class="form-control" placeholder="Enter Password"
                v-model="formData.ncharPassword" />
            </div>
            <div class="form-group col-md-6">
              <label for="mobile-number" class="form-label">Mobile Number<span class="text-danger">*</span></label>
              <input type="tel" id="mobile-number" class="form-control" placeholder="Enter Mobile Number"
                v-model="formData.ncharMobileNumber" />
            </div>
          </div>
          <div class="row">
            <div class="form-group col-md-6">
              <label for="email" class="form-label">Email<span class="text-danger">*</span></label>
              <input type="email" id="email" class="form-control" placeholder="Enter Email"
                v-model="formData.ncharEmail" />
            </div>
            <div class="form-group col-md-6">
              <label for="aadhaar" class="form-label">Aadhaar Number<span class="text-danger">*</span></label>
              <input type="text" id="aadhaar" class="form-control" placeholder="Enter Aadhaar Number"
                v-model="formData.ncharAdharNumber" />
            </div>
          </div>
          <div class="row">
            <div class="form-group col-md-6">
              <label class="form-label">Zillha Parishad<span class="text-danger">*</span></label>
              <input type="text" id="zillha-parishad" class="form-control" placeholder="Aurangabad" v-model="formData.ncharZillhaParishad" />
            </div>
            <div class="form-group col-md-6">
              <label for="username" class="form-label">Panchayat Samiti<span class="text-danger">*</span></label>
              <input type="text" id="panchayat-samiti" class="form-control" placeholder="Enter Panchayat Samiti Name"
                v-model="formData.ncharPanchayatSamiti" />
            </div>
          </div>
          <div class="row">
            <div class="form-group col-md-6">
              <label class="form-label">Gram Panchayat<span class="text-danger">*</span></label>
              <input type="text" id="gram-panchayat" class="form-control" placeholder="Enter Gram Panchayat Name"
                v-model="formData.ncharGramPanchayat" />
            </div>

          </div>

          <!-- Right side: Authority Checkboxes -->
          <div class="form-group">
            <h2 class="h5 mb-3"><i class="fa-solid fa-street-view me-2"></i>Authority Names</h2>
            <div class="form-check" v-if="gpo">
              <input type="checkbox" id="grampanchayat-operator-authorities" class="form-check-input"
                v-model="formData.bGrampanchayatOperatorAuthoraties" />
              <label for="grampanchayat-operator-authorities" class="form-check-label">Grampanchayat Operator
                Authorities</label>
            </div>
            <div class="form-check" v-if="gp">
              <input type="checkbox" id="grampanchayat-authorities" class="form-check-input"
                v-model="formData.bGrampanchayatAuthorisationAuthorities" />
              <label for="grampanchayat-authorities" class="form-check-label">Grampanchayat Authorities</label>
            </div>
            <div class="form-check" v-if="pso">
              <input type="checkbox" id="panchayatsamiti-operator-authorities" class="form-check-input"
                v-model="formData.bPanchayatSamitiOperatorAuthoraties" />
              <label for="panchayatsamiti-operator-authorities" class="form-check-label">Panchayat Samiti Operator
                Authorities</label>
            </div>
            <div class="form-check" v-if="ps">
              <input type="checkbox" id="panchayatsamiti-authorities" class="form-check-input"
                v-model="formData.bPanchayatSamitiAuthorisationAuthorities" />
              <label for="panchayatsamiti-authorities" class="form-check-label">Panchayat Samiti Authorities</label>
            </div>
            <div class="form-check" v-if="zp">
              <input type="checkbox" id="zillhaparishad-authorities" class="form-check-input"
                v-model="formData.bZillhaParishadAuthorities" />
              <label for="zillhaparishad-authorities" class="form-check-label">Zillha Parishad Authorities</label>
            </div>
          </div>

          <div class="button-container">
            <button class="button go-back-btn me-2" @click="goBack"><i class="fa-solid fa-arrow-left me-1"></i>Go
              Back</button>
            <button class="button submit-btn" type="submit">Submit<i class="fa-solid fa-arrow-right ms-2"></i></button>
          </div>
        </section>
      </form>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2'

export default {
  data() {
    return {
      currentStep: 1,

      formData:
      {
        "bGrampanchayatAuthorisationAuthorities": null,
        "bGrampanchayatOperatorAuthoraties": null,
        "bPanchayatSamitiAuthorisationAuthorities": null,
        "bPanchayatSamitiOperatorAuthoraties": null,
        "bZillhaParishadAuthorities": null,
        "dtDateOfCreation": null,
        "dtDateOfModification": null,
        "ncharAdharNumber": "",
        "ncharDepartment": "",
        "ncharDesignation": "",
        "ncharZillhaParishad": "",
        "ncharPanchayatSamiti": "",
        "ncharGramPanchayat": "",
        "ncharEmail": "",
        "ncharFullName": "",
        "ncharMobileNumber": "",
        "ncharPassword": "",
        "ncharUsername": "",
        "ynDeleted": false
      },
      gpo : false,
      gp  : false,
      pso : false,
      ps  : false,
      zp  : false,
      user: (localStorage.getItem('login')) ? JSON.parse(localStorage.getItem('login')) : alert('User not logged in.'),
      saveURL: 'http://127.0.0.1:5555/saveAdmin'
    };
  },
  methods:
  {
    navigateToStep(stepNumber) {
      this.currentStep = stepNumber;
    },
    goBack() {
      this.$emit('go-back');
    },

    submitForm() {
      axios.post(this.saveURL, JSON.stringify(this.formData), { headers: { 'Content-Type': 'application/json' } })
        .then(responce => {
          if (responce.status == 200) {
            Swal.fire({
              title: 'Success!',
              text: 'User registered successfully',
              icon: 'success',
              confirmButtonText: 'OK'
            }).then(() => {
              // Redirect to the previous page
              this.goBack();
            });
          }
          else {
            Swal.fire({
              title: 'Error! ' + responce.status,
              text: 'Opps! somthing went wrong',
              icon: 'warning',
              confirmButtonText: 'OK'
            });
          }
        })
        .catch(() => Swal.fire({
          title: 'Error!',
          text: 'Opps! somthing went wrong',
          icon: 'warning',
          confirmButtonText: 'OK'
        }));
    },
    fetchEditUser(userId = 0) {
      axios.post('http://127.0.0.1:5555/GetAdminById', JSON.stringify({ id: userId }), { headers: { 'Content-Type': 'application/json' } })
        .then(responce => {
          if (responce.status == 200) {
            this.saveURL = 'http://127.0.0.1:5555/editAdmin';
            this.formData =
            {
              "bGramPanchayatAuthority": responce.data.bGramPanchayatAuthority,
              "bPanchayatSamitiAuthority": responce.data.bPanchayatSamitiAuthority,
              "bZillaParishadAuthority": responce.data.bZillaParishadAuthority,
              "dtDateOfCreation": responce.data.dtDateOfCreation,
              "dtDateOfModification": responce.data.dtDateOfModification,
              "ncharAdharNumber": responce.data.ncharAdharNumber,
              "ncharDepartment": responce.data.ncharDepartment,
              "ncharDesignation": responce.data.ncharDesignation,
              "ncharZillhaParishad": responce.data.ncharZillhaParishad,
              "ncharPanchayatSamiti": responce.data.ncharPanchayatSamiti,
              "ncharGramPanchayat": responce.data.ncharGramPanchayat,
              "ncharEmail": responce.data.ncharEmail,
              "ncharFullName": responce.data.ncharFullName,
              "ncharMobileNumber": responce.data.ncharMobileNumber,
              "ncharPassword": responce.data.ncharPassword,
              "ncharUsername": responce.data.ncharUsername,
              "ynDeleted": responce.data.ynDeleted,
              "id": responce.data.id,
              "bGrampanchayatAuthorisationAuthorities": responce.data.bGrampanchayatAuthorisationAuthorities,
              "bGrampanchayatOperatorAuthoraties": responce.data.bGrampanchayatOperatorAuthoraties,
              "bPanchayatSamitiAuthorisationAuthorities": responce.data.bPanchayatSamitiAuthorisationAuthorities,
              "bPanchayatSamitiOperatorAuthoraties": responce.data.bPanchayatSamitiOperatorAuthoraties,
              "bZillhaParishadAuthorities": responce.data.bZillhaParishadAuthorities,
            }
          }
          else {
            Swal.fire({
              title: 'Error! ' + responce.status,
              text: 'Opps! somthing went wrong',
              icon: 'warning',
              confirmButtonText: 'OK'
            });
          }
        })
        .catch(() => Swal.fire({
          title: 'Error!',
          text: 'Opps! somthing went wrong',
          icon: 'warning',
          confirmButtonText: 'OK'
        }));
    }
  },
  mounted()
  {
    if (localStorage.getItem('edituser')) this.fetchEditUser(localStorage.getItem('edituser'));
    
    if(this.user['bGramPanchayatAuthority'] !== undefined && this.user.bGramPanchayatAuthority === true)
      this.gpo = true;
    else if(this.user['bPanchayatSamitiAuthority'] !== undefined && this.user.bPanchayatSamitiAuthority === true || this.user['panchaytsamitioprator'] !== undefined && this.user.panchaytsamitioprator === true)
      this.gp = true;
    else if(this.user['bZillaParishadAuthority'] !== undefined && this.user.bZillaParishadAuthority === true)
    {
      this.ps = true;
      this.pso = true;
      this.zp = true;
    }
    
  }
};
</script>



<style scoped>
.form-check {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.authority-checkboxes {
  flex: 1;
  padding-left: 2rem;
  /* Add spacing from the left side */
}

.authority-checkboxes h2 {
  margin-top: 0;
}

.authority-checkboxes .form-group {
  margin-bottom: 1rem;
}

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
  flex-direction: column;
  gap: 1rem;
  /* Vertical gap between form elements */
}

.form-group {
  margin-bottom: 0.5rem;
}

.form-group {
  /* display: flex;
  align-items: center; */
  margin-bottom: 1rem;
  /* Add some vertical spacing */
}


.full-name-label {
  display: flex;
  width: 50%;
  /* Adjust the width as needed */
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
  width: 80%;
  /* Adjust width as needed */
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

ul.form-stepper>li:not(:last-of-type) {
  margin-bottom: 0.625rem;
  -webkit-transition: margin-bottom 0.4s;
  -o-transition: margin-bottom 0.4s;
  transition: margin-bottom 0.4s;
}

.form-stepper-horizontal>li:not(:last-of-type) {
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
  width: 100%;
  /* Make the button span the full width */
}

.form-container,
.dashboard {
  padding: 0 !important;
}

.form-label {
  font-size: 14px !important;
}</style>
