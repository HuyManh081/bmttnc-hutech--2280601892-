def TaoTuple(lst):
    return tuple(lst)
input_list = input("Nhap danh sach cac phan tu (cach nhau boi dau phay): ")
numbers = list(map(int, input_list.split(',')))
my_tuple = TaoTuple(numbers)
print("List: ", numbers)
print("Tuple da tao: ", my_tuple)
