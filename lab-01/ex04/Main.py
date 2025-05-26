from QLSVien import QLSVien
qlsv = QLSVien()
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*****************************Menu*************************")
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo DTB")
    print("6. Sap xep sinh vien theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")

    key= int(input("Nhap lua chon: "))
    if(key == 1):
        print("1. Them sinh vien")
        qlsv.nhapSV()
        print("Da them sinh vien")
    elif(key == 2):
        if (qlsv.soluongSV() > 0):
            print("\n2. Cap nhat sinh vien")
            print("\nNhap ID sinh vien can cap nhat: ")
            ID = int(input())
            qlsv.updateSV(ID)
        else:
            print("\nKhong co sinh vien nao trong danh sach")
    elif(key == 3):
        if (qlsv.soluongSV() > 0):
            print("\n3. Xoa sinh vien")
            ID = int(input("\nNhap ID sinh vien can xoa: "))
            if (qlsv.deleteByID(ID)):
                print("\nDa xoa sinh vien co ID = ", ID)
            else:
                print("\nKhong tim thay sinh vien co ID = ", ID)
        else:
            print("\nKhong co sinh vien nao trong danh sach")
    elif(key == 4):
        if (qlsv.soluongSV() > 0):
            print("\n4. Tim kiem sinh vien theo ten")
            print("\nNhap ten sinh vien can tim: ")
            name= input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nKhong co sinh vien nao trong danh sach")
    elif(key == 5):
        if (qlsv.soluongSV() > 0):
            print("\n5. Sap xep sinh vien theo DTB")
            qlsv.sortByScore()
            qlsv.showSinhVien(qlsv.getListSV())
        else:
            print("\nKhong co sinh vien nao trong danh sach")
    elif(key == 6):
        if (qlsv.soluongSV() > 0):
            print("\n6. Sap xep sinh vien theo chuyen nganh")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSV())
        else:
            print("\nKhong co sinh vien nao trong danh sach")
    elif(key == 7):
        if (qlsv.soluongSV() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSV())
        else:
            print("\nKhong co sinh vien nao trong danh sach")
    elif(key == 0):
        print("\nBan da thoat chuong trinh")
        break
    else:
        print("\nLua chon khong hop le")