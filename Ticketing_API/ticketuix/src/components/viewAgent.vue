<template>
  <div class="hello">
    <template>
    <div>
      <br>
        <h1 class="text-center">Registro de solicitudes</h1>
        <br>
        <div id="first" class="row justify-content-center">
          <div class="col-auto">

            <table table class="table table-striped">
                <tr>
                    <th scope="col">Correo</th>
                    <th scope="col">Nombre</th>
                    <th scope="col">Apellido</th>
                    <th scope="col">Asunto</th>
                    <th scope="col">Mensaje</th>
                </tr>
                <tbody>
                    <tr v-for="(data, index) in data" :key="index">
                        <td class="td1">{{ data.mail }}</td>
                        <td class="td2">{{ data.name }}</td>
                        <td class="td2">{{ data.lastname }}</td>
                        <td class="td2">{{ data.subject }}</td>
                        <td class="td2">{{ data.message }}</td>
                        <!--<td>
                            <b-button pill class="ibutton" variant="outline-danger" @click="onDeleteData(data)">Delete
                            </b-button>
                        </td>
                        <td>
                            <b-button pill class="ibutton" variant="outline-success" v-b-modal.edit-update-modal
                                @click="editData(data)">Update</b-button>
                        </td>!-->
                    </tr>
                </tbody>
            </table>
            <!--<b-modal ref="editDataModal" id="edit-update-modal" title="Update" hide-footer>
                <div class="updateContainer">
                    <b-form @submit.prevent="updatesubmit">
                        <b-form-group id="input-12" label="Company Name" label-for="input-2">
                            <b-form-inputid="input-2"type="String"v-model="editentry.company"placeholder="Company Name">
                                </b-form-input>
                        </b-form-group>
                        <b-form-group id="input-12" label="Designation" label-for="input-2">
                            <b-form-inputid="input-2"type="String"v-model="editentry.designation"placeholder="Designation">
                                </b-form-input>
                        </b-form-group>
                        <b-form-group id="input-12" label="Review" label-for="input-2">
                            <b-form-textareaid="input-2"type="text"v-model="editentry.review"placeholder="Type
                                Review"rows=8>
                                </b-form-textarea>
                        </b-form-group>
                        <b-button pill v-on:Click.stop="updatesubmit" @click="$bvModal.hide('edit-update-modal')"
                            id="button-2" type="submit" variant="dark">Update</b-button>
                    </b-form>
                </div>
            </b-modal>!-->
            </div>
        </div>
    </div>
</template>
      <!--<table class="table">
        <thead>
          <tr>
            <th>Mail</th>
            <th>Last Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user_alias in User" :key="user_alias.id">
            <td> {{ user_alias.mail }}</td>
            <td>{{ user_alias.name }}</td>
            <td>{{ user_alias.lastname }}</td>
          </tr>
        </tbody>
      </table>!-->

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      data: []
    }
  },
  methods: {
    getData () {
      const path = 'http://localhost:5000/list'
      axios.get(path).then((res) => {
        this.data = res.data
        console.log(this.data)
      })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.getData()
  }
}

/* export default {
  name: 'viewAgent',
  data () {
    return {
      userData: {}
    }
  },
  mounted () {
    const path = 'http://localhost:5000/list'
    axios.get(path).then((response) => {
      console.log(response.data)
      this.userData = response.data
    })
      .catch((error) => {
        console.log(error)
      })
  }
} */
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
