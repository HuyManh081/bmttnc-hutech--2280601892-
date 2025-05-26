def truycapphantu(tupledata):
    first_element = tupledata[0]
    last_element = tupledata[1]
    return first_element, last_element
input_tuple = eval(input("Nhap tuple: "))
first, last = truycapphantu(input_tuple)
print("Phan tu dau tien: ", first)
print("Phan tu cuoi cung: ", last)