import PyPDF2
import os
from PyPDF2 import PdfReader

from models.get_content import get_readings_data,get_readings

def find_axis(file_name):
    axis = file_name.split(".pdf")[0]
    return axis

def repatability(mes,x):

    mes = float(mes)
    res =[]
    for i in x:
        a = float(i)
        dif = mes-a
        res.append(dif)
    rep = max(res) - min(res)
    rep = rep*1000

    return rep

def remarks(mes,x,tol):

    mes = float(mes)
    res =[]
    for i in x:
        a = float(i)
        dif = mes-a
        dif = dif*100
        if dif>tol:
            res.append("Y")
        else:
            res.append("N")

    c = res.count("Y")
    if c == 3:
        rep = "WITH IN LIMITS"
    else:
        rep = "NOT WITH IN LIMITS"
    return rep


def cordinate_readings(matter):

    key = 'Position'
    clse = "DecimalPoints:"
    idx = matter.index(key)
    end = matter.index(clse)

    one = idx+4

    new = matter[one:end]
    q = []
    w = []
    for i in range(0,len(new)-1):
        a = float(new[i])
        b = float(new[i + 1])
        if a-b<=2 and b>90 and a>90 and a>0 and b>0:
            q.append(new[i])
            w.append(new[i + 1])
    return q,w



def tolderance(x,request_data):
    e1 = request_data.get('err_1',None)
    e2 = request_data.get('err_2',None)

    if e1 == None or e2 == None:

        sp_ac = request_data.get('sp_ac')


        if type(x)== str:
            l = x
        else:
            l=str(x)

        sp_ac = sp_ac.replace("L", l)

        result = eval(sp_ac)


        return result

    else:
        x = float(x)
        # return 1.8+(x/400)
        return e1+(x/e2)


def pdf_file_to_list(folder_path,request_data):
    response = {}
    count = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):

            file_path = os.path.join(folder_path, filename)

            # Open the PDF file
            with open(file_path, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                reader = PdfReader(file_path)
                # print(len(reader.pages))
                # Loop through each page in the PDF
                pagecont = []
                for page_num in range(len(reader.pages)):
                    # page = pdf_reader.getPage(page_num)
                    # text = page.extractText()
                    # extracting text from page
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    # print("text type----------------------------------------------------------------------\n",type(text))
                    page_text = text.split()
                    pagecont.extend(page_text)

                axis = find_axis(filename)

                m, o = cordinate_readings(pagecont)

                # reads = get_readings(m, o)
                # print("reads",reads)
                base_data,read_data =get_readings_data(pagecont)


                reads = get_readings(base_data, read_data)


                alerts = []
                for i in reads:
                    tol = tolderance(i,request_data)
                    res = {}
                    res["Measured_Size"] = i
                    res["Tolerance"] = tol
                    x = reads[i]

                    # print("x",x)

                    if len(x)>2:
                        res["set_1"] = x[0]
                        res["set_2"] = x[1]
                        res["set_3"] = x[2]
                        res["rep"] = repatability(i, x)
                        res["rem"] = remarks(i, x, tol)
                        axis = axis[0]
                        alerts.append(res)


                count += 1
                key = f"key_{count}"
                response[key] = alerts
    return response

