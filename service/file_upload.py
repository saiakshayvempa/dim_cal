from flask_restful import Resource, request
import os
 # Gets the current working directory

from models.store_reports import move_files

class 5FileUpload(Resource):
    def post(self):
        try:

            # Check if all files are present in the request
            required_files = ['x_linear', 'y_linear', 'z_linear']

            # for file_key in required_files:
            #     if file_key not in request.files:
            #         return {'res_status': False, 'msg': f'File {file_key} not provided'}

            # Save each file
            root_folder = os.getcwd()


            folder_path = f"{root_folder}\s3"
            output_file = f'{root_folder}/reports'
            os.makedirs(folder_path, exist_ok=True)
            os.makedirs(output_file, exist_ok=True)
            # folder_path = "C:/Users/Akshay/PycharmProjects/validator/s3/"

            # Example usage
            # source_folder = f'{root_folder}/reports'
            # destination_folder = root_folder
            # destination_folder = destination_folder.replace("\main", "")
            #
            # destination_folder = f"{destination_folder}/report_library"
            #
            # move_files(source_folder, destination_folder)

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
