<template>
  <div class="VistaPrueba">
    <Prueba  msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Prueba from '@/components/Prueba.vue'

export default {
  name: 'VistaPrueba',
  components: {
    Prueba
  }
}
</script>
