import http from "../http-common";

class UploadFilesService {
  upload(xmlfile, onUploadProgress) {
    let formData = new FormData();

    formData.append("xmlfile", xmlfile);

    return http.post( "/upload-xml", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      },
      onUploadProgress
    });
  }

  getFiles() {
    return http.get("/files-xml");
  }
}

export default new UploadFilesService();