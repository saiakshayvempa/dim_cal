from flask_restful import Resource, request


from models.get_pdf_content import pdf_file_to_list
from models.printing_docs import printing

class ReportGenerate(Resource):
    def post(self):
        try:

            # Check if all files are present in the request
            request_data = request.get_json()
            print("request_data",request_data)
            folder_path = "C:/Users/Akshay/PycharmProjects/validator/s3/"
            # pdf_file_to_list(folder_path)
            response = pdf_file_to_list(folder_path)
            print("respone", response)
            set_x = response['key_1']
            set_y = response['key_2']
            set_z = response['key_2']

            request_data['set_x'] = set_x
            request_data['set_y'] = set_y
            request_data['set_z'] = set_z
            input_file = 'C:/Users/Akshay/PycharmProjects/project_N/temp/temp.docx'
            output_file = 'C:/Users/Akshay/PycharmProjects/validator/reports/report' + '.docx'

            result = printing(input_file, output_file, request_data)
            print("result", result)

            return {'res_status': True, 'msg': 'File Uploaded successfully', 'data': output_file,"link":'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'}
        except Exception as e:
            print('Error:', str(e))
            return {'res_status': False, 'msg': 'File Uploaded failed', 'Error': str(e)}
