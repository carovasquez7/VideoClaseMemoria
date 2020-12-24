import os
import xmltodict
import pprint
import json
from flask import Flask, request, redirect, Response, abort, jsonify, send_from_directory, render_template, url_for
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from bson import json_util
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/videoclasedb"
mongo = PyMongo(app)
#RUTAS DE LA API
@app.route('/')
def home():
    return ('Hola mundo')

########

@app.route('/files-xml', methods=['GET'])
def get_xmlfile():
    basedatos= mongo.db.files
    files = basedatos.find({},{"_id":0, "objeto.@titulo":1})    
    
    #for x in files:
     #     print(x)

    response = json_util.dumps(files)
    return Response(response, mimetype='/application/json')

##### POST-GET xml API-MOONGO

@app.route("/upload-xml", methods=["GET", "POST"])
def upload_xmlfile():
  if request.method == "POST":
    if request.files:
      xmlfile = request.files['xmlfile']      
      docJson = xmltodict.parse(xmlfile.read()) #Etapa de convertir XML a JSON (xml a dic)
      finalJson = json.loads(json.dumps(docJson))#json final
      #Cargar archivo XML a mongo
      #Cargar finalJson a mongo-base de datos
      mongo.db.files.insert(finalJson)  
      print("xml guardado")
      return redirect(request.url)
  
  return '''

<div class="container">
  <div class="row">
    <div class="col">

      <h1>Upload an image</h1>
      <hr>

      <form action="/upload-xml" method="POST" enctype="multipart/form-data">

        <div class="form-group">
          <label>Select xml</label>
          <div class="custom-file">
            <input type="file" class="custom-file-input" name="xmlfile" id="xmlfile">
            <label class="custom-file-label" for="xmlfile">Select image...</label>
          </div>
        </div>

        <button type="submit" class="btn btn-primary">Upload</button>

      </form>

    </div>
  </div>
</div>

    '''


if __name__ == "__main__":
    app.run (debug=True)
