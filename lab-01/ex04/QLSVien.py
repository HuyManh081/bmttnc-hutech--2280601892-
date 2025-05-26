from SinhVien import SinhVien
class QLSVien:
    list_sinhvien = []
    def generateID(self):
        maxID =1 
        if (self.soluongSV()>0):
            maxID = self.list_sinhvien[0]._id
            for sv in self.list_sinhvien:
                if (maxID < sv._id):
                    maxID = sv._id
            maxID = maxID + 1
        return maxID 
    def soluongSV(self):
        return self.list_sinhvien.__len__()
    def nhapSV(self):
        svID= self.generateID()
        ten = input("Nhap ten sinh vien: ")
        tuoi = int(input("Nhap tuoi sinh vien: "))
        gioitinh = input("Nhap gioi tinh sinh vien: ")
        chuyennganh = input("Nhap chuyen nganh sinh vien: ")
        diem = float(input("Nhap diem sinh vien: "))
        sv = SinhVien(svID,ten,tuoi,gioitinh,chuyennganh,diem)
        self.xepHocluc(sv)
        self.list_sinhvien.append(sv)
    def updateSV(self, ID):
        sv: SinhVien = self.findByID(ID)
        if(sv != None):
            ten = input("Nhap ten sinh vien: ")
            tuoi = int(input("Nhap tuoi sinh vien: "))
            gioitinh = input("Nhap gioi tinh sinh vien: ")
            chuyennganh = input("Nhap chuyen nganh sinh vien: ")
            diem = float(input("Nhap diem sinh vien: "))
            sv._ten = ten
            sv._tuoi = tuoi
            sv._gioitinh = gioitinh
            sv._chuyennganh = chuyennganh
            sv._diem = diem
            self.xepHocluc(sv)
        else: 
            print ("Sinh Vien co ID = {} khong ton tai".format(ID))
    def sortByID(self):
        self.list_sinhvien.sort(key=lambda x: x._id, reverse=False)
    def sortByName(self):
        self.list_sinhvien.sort(key=lambda x: x._ten, reverse=False)
    def sortByScore(self):
        self.list_sinhvien.sort(key=lambda x: x._diem, reverse=False)
    def findByID(self, ID):
        searchResult = None
        if(self.soluongSV() > 0):
         for sv in self.list_sinhvien:
            if (sv._id == ID):
                searchResult = sv
        return searchResult  
    def findByName(self, keyword):
        listSV = []
        if(self.soluongSV() > 0):
            for sv in self.list_sinhvien:
                if (keyword.upper() in sv._ten.upper()):
                    listSV.append(sv)
        return listSV
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.list_sinhvien.remove(sv)
            isDeleted = True
        return isDeleted
    def xepHocluc(self, sv: SinhVien):
        if (sv._diem >= 8.0):
            sv._hocluc = "Gioi"
        elif (sv._diem >= 6.5):
            sv._hocluc = "Kha"
        elif (sv._diem >= 5.0):
            sv._hocluc = "Trung Binh"
        else:
            sv._hocluc = "Yeu"
    def showSinhVien(self, listSV):
        print ("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8} {:<8}".format("ID", "Ten", "Tuoi", "Gioi Tinh", "Chuyen Nganh", "Diem", "Hoc Luc"))
        if (listSV.__len__() > 0):
              for sv in listSV:
                print ("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8} {:<8}".
                         format(sv._id, sv._ten, sv._tuoi, sv._gioitinh, sv._chuyennganh, sv._diem, sv._hocluc))
        print("\n")
    def getListSV(self):
        return self.list_sinhvien
                       