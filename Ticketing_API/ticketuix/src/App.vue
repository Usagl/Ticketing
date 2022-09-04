<template>
  <router-view />
</template>

<script>
import formulario from './components/formulario.vue'
import viewAgent from './components/viewAgent'

export default {
  name: 'App',
  components: { formulario, viewAgent }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
