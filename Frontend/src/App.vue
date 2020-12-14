<template>
  <v-app>  
    <div class="container">
      <v-app-bar
      absolute
      color="#fcb69f"
      dark     
      src="https://www.tokkoro.com/picsup/2624547-blur-background-4k-desktop-wallpaper-hd.jpg"      
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>

      <v-toolbar-title>VideoClase</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar> 
     <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item button to="/">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Inicio</v-list-item-title>
          </v-list-item>

          <v-list-item button to="/upload-xml">
            <v-list-item-icon>
              <v-icon>mdi-upload</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Subir Archivo</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    </div>        
    
    <v-main>
      <v-container>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Home from './views/Home'
import VistaPrueba from './views/VistaPrueba'
import VistaUploadFilesXml from './views/VistaUploadFilesXml'


export default {
  name: 'App',

  components: {
    Home, VistaPrueba, VistaUploadFilesXml
  },

     data: () => ({
      drawer: false,
      group: null,
    }),

   
};
</script>
