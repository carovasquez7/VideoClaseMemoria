<template>

  <div>
      
      <v-container 
      fluid
      ma-10 pa-10 
      class="grey lighten-5 md-9"
      >
    <v-layout></v-layout>
        <h1>
         Prueba Subir Archivo
        </h1>        
        <v-file-input multiple label="Subi Archivo"></v-file-input>

      </v-container>
  </div>

</template>

<script>
  export default {
    data: () => ({
      alignments: [
        'start',
        'center',
        'end',
      ],
    }),
  }
</script>

<style>

</style>