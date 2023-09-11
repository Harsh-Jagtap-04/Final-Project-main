<template>
  <nav class="navbar">
    <div class="logo_item">
      <img src="../../img/logo2.jpg" alt="">
      <img src="../../img/logo.jpg" alt="">
      <div class="logotxt">
          <p>THE MAHATMA GANDHI NATIONAL</p>
          <p>RURAL EMPLOYMENT GUARANTEE ACT 2005</p>
          <p>Ministry Of Rural Development, Government Of India</p>
      </div>
    </div>

    <router-link to="/adminlogin" class="registration-link" id="login-admin-link">
  <div class="admin-login-button">
    <span class="admin-login-label">Admin Login</span>
  </div>
</router-link>

    <div class="navbar_content">
      <i class="bi bi-grid"></i>
      <i class="bx bx-sun" id="darkLight"></i>
      <i class="bx bx-bell"></i>
    </div>
  </nav>
</template>

<script>

export default {
  name: 'NavBar',

};
</script>

<style scooped>
#login-admin-link {
  text-decoration: none; /* Remove the underline */
  /* Add any other styling you want for this link */
}

@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
.content {
  z-index: 3;
}
:root {
  --white-color: #fff;
  --blue-color: #4070f4;
  --grey-color: #707070;
  --grey-color-light: #aaa;
}
body {
  background-color: #e7f2fd;
  transition: all 0.5s ease;
}
body.dark {
  background-color: #333;
}
body.dark {
  --white-color: #333;
  --blue-color: #fff;
  --grey-color: #f2f2f2;
  --grey-color-light: #aaa;
}
.navbar {
  position: sticky;
  top: 0;
  left: 0;
  width: 100%;
  background-color: var(--white-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px 30px;
  z-index: 1;
  box-shadow: 0 0 2px var(--grey-color-light);
}
.logo_item {
  display: flex;
  align-items: center;
  column-gap: 10px;
  font-size: 22px;
  font-weight: 500;
  color: var(--blue-color);
}
.navbar img {
  width: 80px;
  height: 100px;
  /*border-radius: 50%;*/
}
.search_bar {
  height: 47px;
  max-width: 430px;
  width: 100%;
}
.search_bar input {
  height: 100%;
  width: 100%;
  border-radius: 25px;
  font-size: 18px;
  outline: none;
  background-color: var(--white-color);
  color: var(--grey-color);
  border: 1px solid var(--grey-color-light);
  padding: 0 20px;
}
.navbar_content {
  display: flex;
  align-items: center;
  column-gap: 25px;
}
.navbar_content i {
  cursor: pointer;
  font-size: 20px;
  color: var(--grey-color);
}
.admin-login-button {
  cursor: pointer;
  font-size: 16px;
  color: var(--white-color);
  background-color: var(--blue-color);
  border-radius: 50%;
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s ease;
  margin-left: 400px;
}

.admin-login-label {
  text-align: center; 
  line-height: 1.2; 
}

.admin-login-button:hover {
  background-color: #3455a1; 
}
</style>