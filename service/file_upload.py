from flask_restful import Resource, request
import os
 # Gets the current working directory

from models.store_reports import move_files

class FileUpload(Resource):
    def post(self):
        try:

            # Check if all files are present in the request
            required_files = ['x_linear', 'y_linear', 'z_linear']

            # for file_key in required_files:
            #     if file_key not in request.files:
            #         return {'res_status': False, 'msg': f'File {file_key} not provided'}

            # Save each file

            file_paths = {}
            for file_key in required_files:
                if file_key in request.files:
                    file = request.files[file_key]
                    file_path = f"{folder_path}/{file.filename}"

                    file.save(file_path)
                    file_paths[file_key] = file_path


            return {'res_status': True, 'msg': 'File Uploaded successfully', 'file_paths': file_paths}
        except Exception as e:

            return {'res_status': False, 'msg': 'File Uploaded failed','Error': str(e)}
