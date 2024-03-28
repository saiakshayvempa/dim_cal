import PyPDF2
import os
from PyPDF2 import PdfReader

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

def get_readings(m,o):
    dis = {}
    for i in range(0, len(m) - 1):
        k = m[i]
        if m[i] < m[i + 1]:
            if m[i] in dis.keys():
                v = dis[k]
                a = o[i]
                v.append(a)
                dis[k] = v
            else:
                dis[k] = [o[i]]

    return dis

def tolderance(x):
    x = float(x)
    return 1.8+(x/400)


def pdf_file_to_list(folder_path):
    response = {}
    count = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            print("file_name--->",filename)
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
                print("pagecont",pagecont)
                axis = find_axis(filename)
                print("axis------------->", axis)
                m, o = cordinate_readings(pagecont)
                # print("m,o",m,o)
                reads = get_readings(m, o)
                result = {}
                print("reads", reads)

                alerts = []
                for i in reads:
                    tol = tolderance(i)
                    res = {}
                    res["Measured_Size"] = i
                    res["Tolerance"] = tol
                    x = reads[i]

                    print("X----->", x)

                    res["set_1"] = x[0]
                    res["set_2"] = x[1]
                    res["set_3"] = x[2]
                    res["rep"] = repatability(i, x)
                    res["rem"] = remarks(i, x, tol)
                    axis = axis[0]
                    alerts.append(res)
                # print("result",result)
                # print("alerts---->>>",alerts)
                count += 1
                key = f"key_{count}"
                response[key] = alerts

    return response

#
# folder_path = 'C:/Users/Akshay/PycharmProjects/project_N/input'
# pdf_file_to_list(folder_path)