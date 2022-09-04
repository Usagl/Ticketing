<template>
  <div>
    <br>
    </br>
    <h1 class="text-center">Ingreso de solicitud</h1>
    <form action="/form" method="POST" v-on:submit.prevent="postForm(); procesar();">
      <p>
        Correo: <input type="text" name="mail" placeholder="E-mail" v-model="formulario.mail"/>
      </p>
      <p>
        Nombre: <input type="text" name="name" placeholder="Nombre" v-model="formulario.name"/>
      </p>
      <p>
        Apellido: <input type="text" name="lastname" placeholder="Apellido" v-model="formulario.lastname"/>
      </p>
      <p>
        Asunto: <input type="text" name="subject" placeholder="Asunto" v-model="formulario.subject"/>
      </p>
      <p>
        Mensaje: <textarea name="message" id="message" cols="30" placeholder="Mensaje" v-model="formulario.message"></textarea>
      </p>
      <hr />
      <input type="submit" value="Enviar" title="Enviar"/>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Formulario',
  data () {
    return {
      formulario: {
        mail: '',
        name: '',
        lastname: '',
        subject: '',
        message: ''
      }
    }
  },
  methods: {
    postForm () {
      let newformulario = {
        mail: this.formulario.mail,
        name: this.formulario.name,
        lastname: this.formulario.lastname,
        subject: this.formulario.subject,
        message: this.formulario.message
      }
      console.log(newformulario)
      const path = 'http://127.0.0.1:5000/form'
      axios.post(path, newformulario).then((response) => {
        console.log(response)
      })
    },
    procesar () {
      alert(this.formulario.name + ' ' + 'su solicitud ha sido enviada correctamante')
    }
  }
}
/* import axios from 'axios'
export default {
  name: 'Main',
  data () {
    return {
      mensaje: 'Nuevo mensaje desde Vue JS'
    }
  },
  methods: {
    getMensaje () {
      const path = 'http://localhost:5000/api/v1.0/mensaje'
      axios.get(path).then((respuesta) => {
        this.mensaje = respuesta.data
      })
        .catch((error) => {
          console.error(error)
        })
    }
 },
  created () {
    this.getMensaje()
  }
}  */

</script>

<style>
  form {
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
  }
  label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
  }
  input, select {
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #555;
  }
  input[type="checkbox"] {
    display: inline-block;
    width: 16px;
    margin: 0 10px 0 0;
    position: relative;
    top: 2px;
  }
  .pill {
    display: inline-block;
    margin: 20px 10px 0 0;
    padding: 6px 12px;
    background: #eee;
    border-radius: 20px;
    font-size: 12px;
    letter-spacing: 1px;
    font-weight: bold;
    color: #777;
    cursor: pointer;
  }
  button {
    background: #0b6dff;
    border: 0;
    padding: 10px 20px;
    margin-top: 20px;
    color: white;
    border-radius: 20px;
  }
  .submit {
    text-align: center;
  }
  .error {
    color: #ff0062;
    margin-top: 10px;
    font-size: 0.8em;
    font-weight: bold;
  }
</style>
