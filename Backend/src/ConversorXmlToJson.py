import os
import xmltodict
import pprint
import json

NameFile = 'JsonC1.json'

def ConversorXmlToJson(file):
    with open(file) as fd:
        print(type(file))
        doc = xmltodict.parse(fd.read())

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.dumps(doc))

    with open(NameFile,'w') as file:
        final_doc = json.dump(doc, file, indent=4)
    
    return final_doc

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
nombre_archivo= os.path.join(THIS_FOLDER,"XMLPRUEBA.xml")
print(type(nombre_archivo))
ConversorXmlToJson(nombre_archivo)