<template>
  <div class="letter">
    <p style="text-align: center;">प्रपत्र - अ</p>
    <p>
      महात्मा गांधी राष्ट्रीय ग्रामीण रोजगार हमी योजना- महाराष्ट्र अंतर्गत सिंचन सुविधा म्हणून वैयक्तिक
      लाभाची सिंचन विहीर मंजूर करणेसाठी नमुना अर्ज प्रति,
    </p>
    <p>
      मी<b>&nbsp;{{ formData.ncharFirstName }} {{ formData.ncharMiddleName }}&nbsp;{{formData.ncharLastName}}&nbsp;</b>राहणार<b>&nbsp;{{formData.ncharResidingAt}}&nbsp;</b>तालुका<b>&nbsp;{{formData.ncharTaluka}}&nbsp;</b>जिल्हा<b>&nbsp;{{formData.ncharDistrict}}&nbsp;</b>
      महात्मा गांधी राष्ट्रीय ग्रामीण रोजगार हमी योजनेअंतर्गत सिंचन सुविधेसाठी वैयक्तिक लाभाच्या सिंचन
      विहीरीसाठी अर्ज सादर करीत आहे.
    </p>
    <p>
      मी<b>&nbsp;{{formData.ncharCategory}}&nbsp;</b>संवर्गाचा अर्जदार असून माझा दारिद्रय रेषेखालील क्र.<b>&nbsp;{{formData.intBPLNumber}}&nbsp;</b>आहे.
      माझ्याकडे गट क्र.<b>&nbsp;{{formData.intGroupNumber}}&nbsp;</b>मध्ये एकूण<b>&nbsp;{{formData.floatTotalLand}}&nbsp;</b>इतकी जमीन आहे. माझ्याकडे सिंचन सुविधा उपलब्ध नाही.
    </p>
    <p>
      मी मनरेगा अंतर्गत नोंदणीकृत मजूर असून मी कुटुंबासह प्रस्तावित विहीर कामावर देय दराने अकुशल काम करण्यास
      तयार आहे. सदर योजनेअंतर्गत मी वरीलप्रमाणे अर्ज सादर करीत असून
    </p>
    <p>
      वैयक्तिक लाभाची सिंचन विहीर मंजूर झाल्यानंतर कोणत्याही प्रकारच्या चुकीची / दिशाभूल करणाऱ्या माहितीसाठी
      मी सर्वस्वी जबाबदार राहील व शासनाचा झालेला सर्व खर्च मी स्वत: अदा करेन.
    </p>
    <p style="text-align: right;">
      आपला / आपली विश्वासू,
    </p>
    <p style="text-align: right;">
      (शेतकऱ्याचे  नाव व सही / अंगठा)
    </p>
    <p>
      अर्जदार :-
    </p>
    <p>
      १. अर्जदाराचा संवर्ग<b>&nbsp;{{formData.ncharCategory}}&nbsp;</b>वर्गवारी:<b>&nbsp;{{formData.ncharCategorized}}&nbsp;</b> दारिद्रय रेषेखालील क्रमांक:<b>&nbsp;{{formData.intBPLNumber}}&nbsp;</b>
    </p>
    <p>
      २. धारण केलेले एकूण क्षेत्र :<b>&nbsp;{{formData.floatTotalLand}}&nbsp;</b>आर                      गट क्रमांक :<b>&nbsp;{{formData.intGroupNumber}}&nbsp;</b>
    </p>
    <p>
      ३. अर्जदाराकडे उपलब्ध असलेली सिंचन सुविधा  :<b>&nbsp;{{formData.ncharIrrigationFacility}}&nbsp;</b>
    </p>
    <p>
      ४. प्राप्त अर्जाचा क्रमांक :<b>&nbsp;{{formData.ncharFormNumber}}&nbsp;</b>
    </p>
    <p style="text-align: right;">
      सोबत :- संलग्न कागदपत्रे
    </p>
    <p>
      १) ७/१२ चा ऑनलाईन उतारा
    </p>
    <p>
      २) ८ अ चा ऑनलाईन उतारा
    </p>
    <p>
      ३) जॉबकार्ड ची प्रत
    </p>
    <p>
      ४) सामुदायिक विहीर असल्यास सर्व मिळून 0.४0 हेक्टर पेक्षा अधिक सलग जमिन
    </p>
    <p>
      असल्याचा पंचनामा
    </p>
    <p>
      ५) सामुदायिक विहीर असल्यास समोपचाराने पाणी वापराबाबत सर्व लाभार्थ्यांमध्ये करारपत्र
    </p>
    <p style="text-align: right;">
      अर्जाची पोचपावती मिळाली
    </p>
    <p style="text-align: right;">
      सही / निशाणीचा अंगठा 
    </p>
    <p style="text-align: right;">
      -----------------------------------------------------------------------------------------------------------
    </p>
    <p style="text-align: right;">
      अर्जाची पोचपावती 
    </p>
    <p>
      १) 
    </p>
    <p>
      २) 
    </p>
    <p>
      ३) 
    </p>
    <p>
      ४) 
    </p>
    <p>
      याप्रमाणे आपला अर्ज मनरेगा विहीर वर्ष<b>&nbsp;{{formData.intYear}}&nbsp;</b>साठी प्राप्त झाला आहे.
    </p>
    <p style="text-align: right;">
      ग्रामसेवक                                  सरपंच
    </p>

    <button @click="generatePDF" v-if="formData">Generate PDF</button>
  </div>
</template>


<script>
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';

export default {
  props: {
    //formData: Object, // Receive formData as a prop
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
      },
      formID       : (localStorage.getItem('showForm')) ? JSON.parse(localStorage.getItem('showForm')) : alert('Invalid Application ID.'),
    };
  },
  methods: {
    async generatePDF() {

      // Check if formData is available before generating the PDF
      if (!this.formData) {
        console.error('formData is not available.');
        return;
      }

      const content = this.$el;

      try {
        const canvas = await html2canvas(content, {
          scale: 2, // Increase the scale factor for higher quality
        });

        const imgData = canvas.toDataURL('image/png');

        const pdf = new jsPDF();
        pdf.addImage(imgData, 'PNG', 0, 0, pdf.internal.pageSize.getWidth(), pdf.internal.pageSize.getHeight());
        pdf.save('report.pdf');
      } catch (error) {
        console.error('Error generating PDF:', error);
      }
    },
  },
  mounted()
  {

  },
};
</script>


<style>
.letter {
  font-family: Arial, sans-serif;
  margin: 0 auto;
  max-width: 600px;
  padding: 20px;
  line-height: 1.6;
}

.letter p {
  margin: 0;
}
</style>

