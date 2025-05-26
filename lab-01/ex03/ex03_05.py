def demsolanxuathien(n):
    count = {}
    for i in n:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
input_list = input("Nhap danh sach phan tu (cach nhau boi dau phay): ")
worldlist = input_list.split(',')
solanxuathien = demsolanxuathien(worldlist)
print("Danh sach phan tu: ", worldlist)