<template>
  <div class="admin-login-modal">
    <div class="admin-login-content">
      <h2>Admin Login</h2>
      <input type="text" v-model="email" placeholder="Email Address" />
      <button @click="requestOTP">Get OTP</button>
      <input type="text" v-model="otp" placeholder="Enter OTP" />
      <button @click="verifyOTP">Login</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2'

export default {
  data() {
    return {
      showAdminLogin: false,
      email: '',
      otp: '',
    };
  },
  methods: {
    openAdminLogin() {
      this.showAdminLogin = true;
    },

    async requestOTP() {
      if (this.email.trim() !== '') {
        try {
          // Send a request to check if the email is registered
          const checkEmailResponse = await axios.post('http://127.0.0.1:5555/checkAdminEmail', {
            email: this.email,
          });

          if (checkEmailResponse.status === 200 && checkEmailResponse.data.isRegistered !== false)
          {
              localStorage.setItem('login',JSON.stringify(checkEmailResponse.data.admin_data));

            const otpResponse = await axios.post('http://127.0.0.1:5555/generateOtp', {
              email: this.email,
            });
            if (otpResponse.status === 200) {
              console.log('OTP Sent Successfully');
              Swal.fire({
            title: 'Success!',
            text: 'OTP Sent Successfully',
            icon: 'success',
            confirmButtonText: 'OK'
          })             

            } else {
              console.error('OTP request failed:', otpResponse.data.error);
              Swal.fire({
            title: 'Error!',
            text: 'User Not found',
            icon: 'error',
            confirmButtonText: 'OK'
          })
            }
          } else {
            console.error('Email is not registered');
            Swal.fire({
            title: 'Error!',
            text: 'Email is not registered',
            icon: 'error',
            confirmButtonText: 'OK'
          })
          }
        } catch (error) {
          console.error('Error:', error);
          
          Swal.fire({
            title: 'Error!',
            text: 'An error occurred while checking email or requesting OTP. Please try again later.',
            icon: 'error',
            confirmButtonText: 'OK'
          })
        }
      } else {
        alert('Please enter an email address.');
      }
    },
    async verifyOTP() {
      if (this.email.trim() !== '' && this.otp.trim() !== '') {
        try {
          // Send a request to your server to verify OTP
          const response = await axios.post('http://127.0.0.1:5555/verifyOtp', {
            email: this.email,
            otp: this.otp,
          });

          if (response.status === 200) {
            console.log('OTP Verified Successfully');
            alert('OTP Verified Successfully');
            // You can now consider the user as log
            this.$router.push('/admin');

          } else {
            //console.error('OTP verification failed:', response.data.error);
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
  },
};
</script>

<style scoped>
.admin-login-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999; /* Ensure it's above other content */
}

.admin-login-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  text-align: center;
  max-width: 400px;
  width: 80%;
}

.admin-login-content h2 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
}

.admin-login-content input[type="text"],
.admin-login-content input[type="password"] {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.admin-login-content button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  margin-top: 10px;
}

.admin-login-content button:hover {
  background-color: #0056b3;
}

.admin-login-content button:last-child {
  background-color: #ccc;
  color: #333;
  margin-left: 10px;
}

.admin-login-content button:last-child:hover {
  background-color: #999;
}

</style>
