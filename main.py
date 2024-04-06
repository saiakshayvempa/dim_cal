
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource,request,Api

# Services Import

from service.file_upload import FileUpload
from service.certi_print import ReportGenerate

app = Flask(__name__)
api = Api(app)
CORS(app)


class HelloWord(Resource):
    def post(self):
        try:
            return {'res_status': True, 'msg': 'Hello World', "data":"data"}
        except Exception as e:

            return {'res_status': False, 'msg': "msg"}


api.add_resource(ReportGenerate,'/ReportGenerate')
api.add_resource(FileUpload,'/FileUpload')

api.add_resource(HelloWord,'/')

if __name__ == '__main__':
    app.run(host='localhost', port=5100, debug=False)

app = Flask(__name__)
api = Api(app)
CORS(app)
