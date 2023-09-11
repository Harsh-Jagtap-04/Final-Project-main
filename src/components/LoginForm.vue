<template>
  <div class="login-page">
    <div class="form">
      <form class="register-form">
        <input v-model="registerData.ncharRegisterUserName" type="text" placeholder="Name" />
        <input v-model="registerData.ncharEmail" type="text" placeholder="Email Address" />
        <input v-model="registerData.ncharMobileNumber" type="text" placeholder="Contact Number" />
        <input v-model="registerData.ncharAadharNumber" type="text" placeholder="Aadhar Number" />
        <button @click.prevent="register">Create</button>

        <p class="message">Already registered? <a href="#" @click.prevent="toggleForm">Sign In</a></p>
      </form>
      <form class="login-form">
        <input v-model="loginData.email" type="text" placeholder="Email Address" />
        <button @click.prevent="requestOTP">Get OTP</button> 
        
        <input v-model="loginData.otp" type="text" placeholder="Enter OTP" />
        <button @click.prevent="login">Login</button>
        <p class="message">Not registered? <a href="#" @click.prevent="toggleForm">Create an account</a></p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import $ from 'jquery';



export default {
  data() {
    return {
      registerData: {
        ncharRegisterUserName: '',
        ncharEmail: '',
        ncharMobileNumber: '',
        ncharAadharNumber: '',
      },
      loginData: {
        email: '',
        otp: '',
      },
      isRegistered: false,
    };
  },
  methods: {
    toggleForm() {
      /* eslint-disable-next-line no-undef */
      $('form').animate({ height: 'toggle', opacity: 'toggle' }, 'slow');
    },
    async requestOTP() {
  if (this.loginData.email.trim() !== '') { // Check if email is not empty
    try {
      // Send a request to check if the email is registered
      const checkEmailResponse = await axios.post('http://127.0.0.1:5555/checkEmail', {
        email: this.loginData.email,
      })//.then(data => console.log(data));

      if (checkEmailResponse.status === 200 && checkEmailResponse.data.isRegistered) {
        // The email is registered, proceed to generate OTP
        const otpResponse = await axios.post('http://127.0.0.1:5555/generateOtp', {
          email: this.loginData.email,
        });

        if (otpResponse.status === 200) {
          console.log('OTP Sent Successfully');
          alert('OTP Sent Successfully');
        } else {
          console.error('OTP request failed:', otpResponse.data.error);
          alert('OTP request failed. Please try again.');
        }
      } else {
        console.error('Email is not registered');
        alert('Email is not registered. Please register an account.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while checking email or requesting OTP. Please try again later.');
    }
  } else {
    alert('Please enter an email address.');
  }
},
    async login() {
      if (this.loginData.email.trim() !== '' && this.loginData.otp.trim() !== '') { // Check if email and OTP are not empty
        try {
          // Send a request to your server to verify OTP
          const response = await axios.post('http://127.0.0.1:5555/verifyOtp', {
            email: this.loginData.email,
            otp: this.loginData.otp,
          });

          if (response.status === 200) {
            console.log('OTP Verified Successfully');
            alert('OTP Verified Successfully');
            // You can now consider the user as logged in

          } else {
            console.error('OTP verification failed:', response.data.error);
            alert('OTP verification failed. Please try again.');
          }
        } catch (error) {
          console.error('Error:', error);
          alert('An error occurred during OTP verification. Please try again later.');
        }
      } else {
        alert('Please enter both email and OTP.');
      }
    },
    async register() {
  if (this.validateRegistrationData()) {
    try {
      const response = await axios.post('http://127.0.0.1:5555/saveRegisterUser', this.registerData);
      
      if (response.status === 200) {
        console.log('Registration Successful');
        alert('Registration Successful');
        this.resetRegistrationForm();
        this.isRegistered = true;
      } else {
        console.error('Registration failed:', response.data.error);
        alert('Registration failed. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred during registration. Please try again later.');
    }
  } else {
    alert('Please fill in all fields.');
  }
},

validateRegistrationData() {
      return (
        this.registerData.ncharRegisterUserName !== '' &&
        this.registerData.ncharEmail !== '' &&
        this.registerData.ncharMobileNumber !== '' &&
        this.registerData.ncharAadharNumber !== ''
      );
    },
resetRegistrationForm() {
      this.registerData.ncharRegisterUserName = '';
      this.registerData.ncharEmail = '';
      this.registerData.ncharMobileNumber = '';
      this.registerData.ncharAadharNumber = '';
    },
  },
};
</script>


  
  <style scoped>
  .login-page {
    width: 500px;
    padding: 8% 0 0;
    margin: auto;
    text-align: center;
  }
  
  .form {
    position: relative;
    z-index: 1;
    background: #FFFFFF;
    max-width: 360px;
    margin: 0 auto 100px;
    padding: 45px;
    text-align: center;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
  }
  /** 
  .login-form {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  width: 80%; 
  margin: 0 auto; /* Center the LoginForm horizontally /*
} */
  .form input {
    font-family: 'Roboto', sans-serif;
    outline: 0;
    background: #f2f2f2;
    width: 100%;
    border: 0;
    margin: 0 0 15px;
    padding: 15px;
    box-sizing: border-box;
    font-size: 14px;
  }
  
  .form button {
    font-family: 'Roboto', sans-serif;
    text-transform: uppercase;
    outline: 0;
    background: #4CAF50;
    width: 100%;
    border: 0;
    padding: 15px;
    color: #FFFFFF;
    font-size: 14px;
    transition: all 0.3s ease;
    cursor: pointer;
    margin-bottom: 15px;
  }
  
  .form button:hover,
  .form button:active,
  .form button:focus {
    background: #43A047;
  }
  
  .form .message {
    margin: 15px 0 0;
    color: #b3b3b3;
    font-size: 12px;
  }
  
  .form .message a {
    color: #4CAF50;
    text-decoration: none;
  }
  
  .form .register-form {
    display: none;
  }
  
  .container {
    position: relative;
    z-index: 1;
    max-width: 300px;
    margin: 0 auto;
  }
  
  .container:before,
  .container:after {
    content: '';
    display: block;
    clear: both;
  }
  
  .container .info {
    margin: 50px auto;
    text-align: center;
  }
  
  .container .info h1 {
    margin: 0 0 15px;
    padding: 0;
    font-size: 36px;
    font-weight: 300;
    color: #1a1a1a;
  }
  
  .container .info span {
    color: #4d4d4d;
    font-size: 12px;
  }
  
  .container .info span a {
    color: #000000;
    text-decoration: none;
  }
  
  .container .info span .fa {
    color: #EF3B3A;
  }
  
  body {
    background: #76b852;
    background: -webkit-linear-gradient(right, #76b852, #8DC26F);
    background: -moz-linear-gradient(right, #76b852, #8DC26F);
    background: -o-linear-gradient(right, #76b852, #8DC26F);
    background: linear-gradient(to left, #76b852, #8DC26F);
    font-family: 'Roboto', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  </style>
  