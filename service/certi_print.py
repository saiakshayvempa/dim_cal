from flask_restful import Resource, request
import os

from models.get_pdf_content import pdf_file_to_list
from models.printing_docs import printing
from models.store_reports import move_files

class ReportGenerate(Resource):
    def post(self):
        try:

            # Check if all files are present in the request
            request_data = request.get_json()
            # make dyanamic
            # print("request_data",request_data)
            root_folder = os.getcwd()

            # pdf_file_to_list(folder_path)
            response = pdf_file_to_list(folder_path,request_data)

            set_x = response['key_1']
            set_y = response['key_2']
            set_z = response['key_2']

            request_data['set_x'] = set_x
            request_data['set_y'] = set_y
            request_data['set_z'] = set_z
            # input_file = 'C:/Users/Akshay/PycharmProjects/validator/templates/temp.docx'

            input_file = root_folder
            input_file = input_file.replace("\main", "")

            input_file = f"{input_file}/templates/temp.docx"

            # output_file = 'C:/Users/Akshay/PycharmProjects/validator/reports/report' + '.docx'
            output_file = f'{root_folder}/reports/report' + '.docx'
            doc_file = f'{root_folder}/reports/report' + '.docx'
            pdf_file = f'{root_folder}/reports/report' + '.pdf'
            printing(input_file, doc_file,pdf_file, request_data)

            # Example usage
            source_folder = f'{root_folder}/reports'
            destination_folder = root_folder
            destination_folder = destination_folder.replace("\main", "")

            destination_folder = f"{destination_folder}/report_library"


            # print('doc_fiel', doc_file,'pdf_file',pdf_file)
            # move_files(source_folder, destination_folder)

            return {'res_status': True, 'msg': 'Certificate Generated Sussfully', 'doc_file': doc_file,'pdf_file':pdf_file,"link":'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'}
        except Exception as e:

            return {'res_status': False, 'msg': 'File Uploaded failed', 'Error': str(e)}
