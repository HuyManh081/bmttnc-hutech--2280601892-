def daonguocphantu(n):
    """
    Hàm đảo ngược các phần tử trong danh sách
    :param n: Danh sách cần đảo ngược
    :return: Danh sách đã được đảo ngược
    """
    return n[::-1]
input_list = input("Nhập danh sách các phần tử (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(',')))
daonguoc = daonguocphantu(numbers)
print("Danh sách đã được đảo ngược: ", daonguoc)