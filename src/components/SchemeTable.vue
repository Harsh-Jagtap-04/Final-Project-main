<template>
  <div class="scheme-table">
    
    <div v-if="!showMultiStepForm">
      <h1 class="text-center">Available Schemes</h1>
      <table class="table mt-5">
        <thead>
          <tr>
            <th>No.</th>
            <th>Scheme Name</th>
            <th>GR (pdf)</th>
            <th>Apply for Scheme</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(scheme, index) in schemes" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ scheme.name }}</td>
            <td>
              <button class="button btn-pdf" @click="openPDF(index)">Open PDF</button>
              <div v-if="pdfVisible === index" class="pdf-popup">
                <button class="btn-close" @click="closePDF"></button>
                <object :data="scheme.pdfPath" type="application/pdf" class="pdf-frame"></object>
              </div>
            </td>
            <td> 
              <button class="button btn-pdf" @click.prevent="openMultiStepForm(index)">Apply</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="showMultiStepForm">
      <!-- Render the MultiStepForm component conditionally -->
      <!-- Pass the selected scheme as a prop to the MultiStepForm component -->
      <MultiStepForm :selected-scheme="selectedScheme" @go-back="closeMultiStepForm" />
    </div>
  </div>
</template>

<script>
 import MultiStepForm from "@/components/MultiStepForm.vue"; // Adjust the path accordingly

export default {
  props: {
    activeTab: String // Add the activeTab prop here
  },
  name: "SchemeTable",
  components: {
     MultiStepForm,
  },
  data() {
    return {
      schemes: [
        {
          name: "Irrigation-well",
          pdfPath: "/assets/pdf/Irrigation-well-GR.pdf", // Update the path here
        },
        // Add more schemes here
      ],
      selectedOption: null,
      pdfVisible: -1,
      showMultiStepForm: false,
      selectedScheme: null, // Store the selected scheme
    };
  },

  methods: {
    openPDF(index) {
      this.pdfVisible = index;
    },
    closePDF() {
      this.pdfVisible = -1;
    },

    openMultiStepForm(index) {
      // Set the selected scheme and show the MultiStepForm
      this.selectedScheme = this.schemes[index];
      this.showMultiStepForm = true;
    },
    closeMultiStepForm() {
      // Clear the selected scheme and hide the MultiStepForm
      this.selectedScheme = null;
      this.showMultiStepForm = false;
    },
    printPDF() {
      const pdfFrame = document.querySelector('.pdf-frame');
      if (pdfFrame) {
        pdfFrame.contentWindow.print();
      }
    },
  },
};
</script>

<style scoped>
/* Your simplified CSS styles here */
.table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 2rem;
}
.table th,
.table td {
  border: 1px solid #dee2e6;
  padding: 0.5rem 1rem;
  text-align: center;
}
.button {
  padding: 0.5rem 1rem;
  border: 1px solid #4361ee;
  background-color: #4361ee;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
}
.btn-pdf {
  background-color: #0e9594;
  border-color: #0e9594;
}
.text-center {
  text-align: center;
}
.mt-5 {
  margin-top: 3rem;
}
.pdf-popup {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.btn-close {
  background-color: #ff4b5c;
  border-color: #ff4b5c;
  color: #fff;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  margin-bottom: 1rem;
  cursor: pointer;
}
.pdf-frame {
  width: 80%;
  height: 80%;
  border: none;
}
.btn-print {
  background-color: #6ab04c;
  border-color: #6ab04c;
  color: #fff;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
</style>
