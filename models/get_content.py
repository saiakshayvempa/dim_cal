
def get_readings_data(pagecont):
    key = 'Position'
    clse = "DecimalPoints:"
    idx = pagecont.index(key)
    end = pagecont.index(clse)

    one = idx+4

    new = pagecont[one:end]


    base_data = []
    read_data = []
    for i in range(1,len(new)-2):

        a = float(new[i-1])
        b = float(new[i])
        c = float(new[i+1])
        if int(b)+1 == int(a):

            base_data.append(a)
            read_data.append(b)

    if len(base_data) ==0 or len(read_data)==0:
        base_data, read_data = get_readings_data_type2(new)
    return base_data,read_data
# base_data,read_data  = get_readings_data(pagecont)


# for i in range(0,len(base_data)):
#     print("o,r",base_data[i],read_data[i])


# exit()

def get_readings(base_data,read_data):

    reads = {}
    for i in range(0,len(base_data)):
        key = base_data[i]
        value = read_data[i]
        # print("ikey,value",key,value)
        # print("i",i)
        if key in reads.keys():

            old_value = reads[key]

            old_value.append(value)

            reads[key] = old_value

        else:

            reads[key] = [value]


    return reads
# reads = get_readings(base_data,read_data)
#
# print("reads",reads)

def get_readings_data_type2(new):

    inx = int(float(new[0]))
    inx = abs(inx)


    base_data_readings = [inx]

    for n in range(0,len(new)-2):
        i = new[n]
        ref = base_data_readings[-1]
        # print("ref",ref)
        val = int(float(i))
        val = abs(val)
        # print("val", val)
        if ref-val == 100:
            # print("if ---->",val)
            base_data_readings.append(val)
        if ref-val == -100:
            # print("if ---->",val)
            base_data_readings.append(val)
        elif ref == val:
            # print("elif ---->", val)
            base_data_readings.append(val)
        else:
            # print("else",val)
            pass




    base_data_readings = base_data_readings[1:]



    base_data = []

    for i in base_data_readings:
        val = inx-i
        # print("i,val",i,val)
        base_data.append(val)


    read_data = []


    for n in range(2,len(new)):
        try:
            i  = new[n]
            # print("i",i)
            val = float(i)
            l = len(read_data)
            se = int(val)
            if se== base_data[l] or se+1 == base_data[l]:
                read_data.append(float(i))
        except:
            pass


    return base_data,read_data



