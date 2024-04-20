from docxtpl import DocxTemplate
import docx


def printing(input_file, doc_file,pdf_file, res):
    doc = DocxTemplate(input_file)
    doc.render(res)
    doc.save(doc_file)
    doc = docx.Document(doc_file)
    doc.save(pdf_file)
    return True






# Create a Document object from the Word file
# doc = docx.Document("sample.docx")
#
# # Save the document as a PDF file
# doc.save("sample.pdf")