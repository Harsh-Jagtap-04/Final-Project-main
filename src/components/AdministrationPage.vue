<template>
  <div class="dashboard">
    <div v-if="selectedOption === null" class="dashboard-options">
      <div @click="selectOption('user')" class="btn btn-info mb-4 text-white"><i class="fa-solid fa-plus me-2"></i>Add New User</div>
      <div id="userTable mt-3">
        <table class="table table-striped">
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>User Name</th>
              <th>Password</th>
              <th>Email</th>
              <th>Phone</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in users" :key="user.id">
              <td>{{ ++index }}</td>
              <td>{{ user.ncharFullName }}</td>
              <td>{{ user.ncharUsername }}</td>
              <td>{{ user.ncharPassword }}</td>
              <td>{{ user.ncharEmail }}</td>
              <td>{{ user.ncharMobileNumber }}</td>
              <td>
                <button class="btn btn-sm rounded btn-info me-2" @click="selectUserForEdit(user.id)"><i class="fa-solid fa-pen-to-square text-white"></i></button>
                <button class="btn btn-sm rounded btn-danger" @click="deleteUser(user.id)"><i class="fa-solid fa-trash-can"></i></button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-else>
      <component :is="selectedOptionComponent" @go-back="goBackFromChild" />
    </div>
  </div>
</template>

<script>
import RegisterNewUser from "@/components/RegisterNewUser.vue";
import RegisterGP from "@/components/RegisterGP.vue";
import RegisterPS from "@/components/RegisterPS.vue";
import axios from 'axios';// ... (import other components)

export default {
  name: 'DashboardPage',
  components: {
    RegisterNewUser,
    RegisterGP,
    RegisterPS,
    // ... (other components)
  },
  data() {
    return {
      selectedOption: null,
      users: [], // Initialize an empty array to store users
    };
  },
  computed: {
    selectedOptionComponent() {
      return this.selectedOption === 'user'
        ? 'RegisterNewUser'
        : this.selectedOption === 'gram'
        ? 'RegisterGP'
        : this.selectedOption === 'panchayat'
        ? 'RegisterPS'
        : null;
    }
  },
  methods: {
    selectOption(option)
    {
      localStorage.removeItem('edituser');
      this.selectedOption = option;
    },
    reloadUserData() {
      this.fetchUsers();
    },
    deleteUser(userId)
    {
      const jsonData = {id: userId};

      axios.post('http://127.0.0.1:5555/deleteAdmin', jsonData,{headers: {'Content-Type': 'application/json'}})
      .then(response => {
        // Handle successful deletion
        const deletedUserId = response.data.id;
        console.log(`User with ID ${deletedUserId} has been deleted.`);

        // Remove the deleted user from the frontend
        this.users = this.users.filter(user => user.id !== userId);
        this.reloadUserData();

      })
      .catch(error => {
        // Handle error
        console.error('Error deleting user:', error);
      });
    },
    fetchUsers()
    {
      axios.get('http://127.0.0.1:5555/GetAdmin')
        .then(users => this.users = users.data)
        .catch(error => console.error('Error:', error));
    },
    selectUserForEdit(userId)
    {
      this.selectedOption = 'user'; // Set the selectedOption to 'user'
      this.selectedUserId = userId; // Store the selected user ID
      localStorage.setItem('edituser',this.selectedUserId);
    },

    goBackFromChild()
    {
      this.selectedOption = null;
      this.reloadUserData();
    }
  },
  mounted() {
    this.fetchUsers(); // Fetch users when the component is mounted
  }
};
</script>

<style scoped>
.dashboard {
  padding: 40px;
  background-color: #ffffff;
  box-shadow: 0 0 2px var(--grey-color-light);
}

.dashboard-block {
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.dashboard-block:hover {
  transform: translateY(-5px);
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
}

.block-content {
  text-align: center;
}

.block-content h2 {
  margin: 0;
  font-size: 18px;
  color: #333;
}
</style>