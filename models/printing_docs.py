from docxtpl import DocxTemplate

def printing(input_file, output_file, res):
    doc = DocxTemplate(input_file)
    doc.render(res)
    doc.save(output_file)
    return True