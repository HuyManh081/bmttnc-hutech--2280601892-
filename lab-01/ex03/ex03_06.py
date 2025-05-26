def xoaphantu(dectionary, key):
     if key in dectionary:
         del dectionary[key]
         return True
     else: 
         return False
my_dict = {'a': 1, 'b': 2, 'c': 3}
keytodelete = 'b'
result = xoaphantu(my_dict, keytodelete)
if result:
    print("Phần tử đã được xóa thành công: ", my_dict)
else:
    print("Phần tử không tồn tại trong từ điển.")