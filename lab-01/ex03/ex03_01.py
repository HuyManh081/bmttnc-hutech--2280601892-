def TinhTongSoChan(list):
    tong = 0    
    for i in list:
        if i % 2 == 0:
            tong += i
    return tong
input_list = input("Nhap so phan tu trong danh sach: ")
numbers = list(map(int, input_list.split(',')))
tongchan = TinhTongSoChan(numbers)
print("Tong cac so chan trong danh sach: ", tongchan)