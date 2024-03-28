from flask_restful import Resource, request
# from .service.get_pdf_content import pdf_file_to_list

from service.get_pdf_content import pdf_file_to_list

class ReportGenerator(Resource):
    def post(self):
        try:
            print("test data")

            # Check if all files are present in the request
            required_files = ['x_linear', 'y_linear', 'z_linear']
            for file_key in required_files:
                if file_key not in request.files:
                    return {'res_status': False, 'msg': f'File {file_key} not provided'}

            # Save each file
            folder_path = "C:/Users/Akshay/PycharmProjects/validator/s3/"
            file_paths = {}
            for file_key in required_files:
                file = request.files[file_key]
                print(f"{file_key}: {file}")
                file_path = f"{folder_path}/{file.filename}"
                file.save(file_path)
                file_paths[file_key] = file_path

            print("Files saved to folder:", file_paths)

            # Process the PDF files
            response = pdf_file_to_list(folder_path)
            print("Response:", response)

            return {'res_status': True, 'msg': 'Data retrieved successfully', 'file_paths': file_paths}
        except Exception as e:
            print('Error:', str(e))
            return {'res_status': False, 'msg': str(e)}
