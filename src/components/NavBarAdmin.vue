<template>
  <nav class="navbar">
    <div class="logo_item">
      <img src="../../img/logo.jpg" alt="">
      <img src="../../img/logo2.jpg" alt="">
      <div class="logotxt">
          <p>THE MAHATMA GANDHI NATIONAL</p>
          <p>RURAL EMPLOYMENT GUARANTEE ACT 2005</p>
          <p>Ministry Of Rural Development, Government Of India</p>
      </div>
    </div>
<!--
    <div class="search_bar">
      <input type="text" placeholder="Search" />
    </div>
  -->
    <div class="navbar_content">
      <i class="bi bi-grid"></i>
      <i class="bx bx-sun" id="darkLight"></i>
      <i class="bx bx-bell"></i>
<!--     
      <img src="images/profile.jpg" alt="Profile" class="profile" />
-->
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBarAdmin'
};
</script>

<style>

@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

.content {
  /* Set a higher z-index value */
  z-index: 99;
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
  /* Remove or set a lower z-index value */
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
  width: 35px;
  height: 35px;
  border-radius: 50%;
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

</style>