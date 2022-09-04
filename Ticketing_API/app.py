from flask import Flask, Response, request, render_template, jsonify
import pymongo
import json
from flask_cors import CORS
from bson import json_util

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}} )

#Este metodo permite ingresar dentro de la base de datos, comprobando la autenticacion de usuario
#ingresando a al host y al puerto de acceso designado, seteando una base de datos con la variable "db"
#la cual en caso de no estar creada se creara.
try:
    mongo = pymongo.MongoClient(username="admin", password="supersecurePass1", host="localhost",
                                port=27017,
                                serverSelectionTimeoutMS = 1000)

    db = mongo.formlog
    mongo.server_info()

except:
    print("ERROR - Cannot connect to db")

#def parse_json(data):
#    return json.loads(json_util.dumps(data))

#Este metodo retorna todos los registros que se encuentran en la base de datos, mostrandolo en el front-end en formato
#de tablas.
@app.route("/list", methods=["POST","GET"])
def view_data():
    if request.method == 'GET':
        allData = db.forms.find()
        dataJson = []
        for data in allData:
            id = data['_id']
            mail = data['mail']
            name = data['name']
            lastname = data['lastname']
            subject = data['subject']
            message = data['message']
            dataDict = {
                'id': str(id),
                'mail': mail,
                'name': name,
                'lastname': lastname,
                'subject': subject,
                'message': message
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)

#@app.route("/list", methods=["GET"])
#def get_some_forms():
#    try:
#
#        data = list(db.forms.find())
#
#        for form in data:
#           form["_id"] = str(form["_id"])
#        return Response(
#           response=json.dumps(data),
#           status=500,
#           mimetype="application/json"
#
#        )
#    except Exception as ex:
#        print(ex)
#        return Response(
#            response=json.dumps({"message": "cannot read forms"}),
#            status=500,
#            mimetype="application/json"
#        )

#Este metodo permite la creación de una solicitud mediante POST la cual permite enviar la información a la base de datos
#de registros y auditorias.
@app.route("/form", methods=["POST"])
def create_form():
    try:
        form = request.get_json()
        dbresponse = db.forms.insert_one(form)
        print(dbresponse)
        return Response(
            response=json.dumps({"message": "form created", "id": f"{dbresponse}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)

#@app.route('/api/v1.0/mensaje')
#def mensaje():
#    return jsonify('Nuevo mensaje desde un servidor Flask')


if __name__ == '__main__':
    app.run(debug=True)
