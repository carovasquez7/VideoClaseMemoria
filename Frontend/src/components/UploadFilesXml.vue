<template>

  <v-container
    fluid
      ma-10 pa-10 
      class="grey lighten-5 md-9"  
  >
    <div>
        <div v-if="currentFile">
            <div>
                <v-progress-linear
                  v-model="progress"
                  color="light-blue"
                  height="25"
                  reactive
                  >
                {{ progress }} %
                </v-progress-linear>
            </div>
        </div>

        <v-row no-gutters justify="center" align="center">
            <v-col cols="8">
                <v-file-input
                show-size
                label="Subir Archivo Xml"
                @change="selectFile"
                ></v-file-input>
            </v-col>

            <v-col cols="4" class="pl-2">
                <v-btn color="success" dark small @click="upload">
                Subir Archivo
                <v-icon right dark>mdi-cloud-upload</v-icon>
                </v-btn>
            </v-col>    
        </v-row>

        <v-alert v-if="message" border="left" color="blue-grey" dark>
        {{ message }}
        </v-alert>

        <v-card v-if="fileInfos.length > 0" class="ms-auto">
          <v-list>
              <v-subheader>Lista de Archivos</v-subheader>

                <v-list-item-group color="primary">
                  <v-list-item v-for="(file, index) in fileInfos" :key="index">                       
                      <v-btn x-small rounded class=ma-3 color="success" dark>
                        <v-icon left>mdi-pencil</v-icon>
                        Crear Video</v-btn>

                      
                      <a :href="file.url">{{ file.objeto.titulo }}</a>
                      

                  </v-list-item>                                   
                </v-list-item-group>

          </v-list>
        </v-card>
    </div>
  </v-container>
</template>

<script>
import UploadService from "../services/UploadFilesService";

export default {
  name: "upload-files",
  data() {
    return {
      currentFile: undefined,
      fileInfos: [],
      progress: 0,
      message: "",

      
      //loading: false
    };
  },
  methods: {
    selectFile(file) {
      this.progress = 0;
      this.currentFile = file;
    },

    upload() {
      if (!this.currentFile) {
        this.message = "Por favor seleccione un Archivo XML";
        return;
      }

      this.message = "";

      UploadService.upload(this.currentFile, (event) => {        
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then((response) => {
          this.message = response.data.message;
          return UploadService.getFiles();
        })
        .then((files) => {
          this.fileInfos = files.data;
        })
        .catch(() => {
          this.progress = 0;
          this.message = "No logró subir el Archivo XML";
          this.currentFile = undefined;
        });
    },
  },
  mounted() {
    UploadService.getFiles().then((response) => {
      this.fileInfos = response.data
    });
  },
};
</script>