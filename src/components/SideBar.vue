<template>
  <nav class="sidebar">
    <div class="menu_content">
      <ul class="menu_items">
        <!-- Menu item 1: Dashboard -->
        <li class="item">
          <a href="#dashboard" class="nav_link submenu_item with-border" @click.prevent="openMultiStepForm('dashboard')" :class="{ active: activeTab === 'dashboard' }">
            <span class="navlink_icon">
              <i class="bx bx-home-alt"></i>
            </span>
            <span class="navlink center-text">Dashboard</span>
          </a>
        </li>
                <!-- Menu item 3: Schemes -->
                <li class="item">
                  <a href="#schemes" class="nav_link submenu_item with-border" @click.prevent="openMultiStepForm('schemes')" :class="{ active: activeTab === 'schemes' }" >
            <span class="navlink_icon">
              <i class="bx bx-list-ul"></i>
            </span>
            <span class="navlink center-text">Schemes</span>
          </a>
        </li>
        <!-- Menu item 2: Apply For Scheme -->
        <!--
        <li class="item">
          <a href="#apply_scheme" class="nav_link submenu_item with-border" @click.prevent="openMultiStepForm('apply_scheme')" :class="{ active: activeTab === 'apply_scheme' }">
            <span class="navlink_icon">
              <i class="bx bx-grid-alt"></i>
            </span>
            <span class="navlink center-text">Apply For Scheme</span>
          </a>
        </li>
      -->
        <!-- Menu item 4: Applications -->
        <li class="item">
          <a href="#applications" class="nav_link submenu_item with-border" @click.prevent="openMultiStepForm('applications')" :class="{ active: activeTab === 'applications' }">
            <span class="navlink_icon">
              <i class="bx bx-file"></i>
            </span>
            <span class="navlink center-text">Submitted Forms</span>
          </a>
        </li>
        <li class="item">
          <a href="#administration" class="nav_link submenu_item with-border" @click.prevent="openMultiStepForm('administration')" :class="{ active: activeTab === 'administration' }">
            <span class="navlink_icon">
              <i class="bx bx-file"></i>
            </span>
            <span class="navlink center-text">Administration</span>
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>


<script>
export default {
  props: {
    activeTab: String // Add the activeTab prop here
  },
  methods: {
    openMultiStepForm(tabName) {
      this.$emit('tab-change', tabName);
    }
    // Other methods and properties
  }
};
</script>

<style>
/* Sidebar styles */
.sidebar {
  margin: 0;
  padding: 0;
  width: 260px; /* Increased sidebar width */
  background-color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
  margin: 28px 0 0 0;
}
ul.menu_items
{
    margin-right: 20px;
}
/* Sidebar links */
/* Sidebar links */
.nav_link
{
  display: block;
  color: black;
  padding: 10px 16px;
  text-decoration: none;
  transition: background-color 0.3s, color 0.3s; /* Add smooth transition */
}

/* Active link */
.nav_link.active
{
  border-radius: 8px;
  background-color: #04AA6D;
  color: white;
}

/* Hover effect */
.nav_link:hover {
  background-color: #555;
  color: white;
}
li.item,
li.item:hover
{
    list-style: none;
}
ol, ul
{
    padding-left: 1rem !important;
}
/* Make sidebar responsive */
@media screen and (max-width: 700px) {
  .sidebar {
    width: 100%;
    height: auto;
    position: relative;
  }
  .nav_link {
    float: left;
  }
  div.content {
    margin-left: 0;
  }
}

@media screen and (max-width: 400px) {
  .nav_link {
    text-align: center;
    float: none;
  }
}
</style>