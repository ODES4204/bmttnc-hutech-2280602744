from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1==1):
  print("CHUONG TRINH QUAN LY SINH VIEN")
  print("*****************************Menu*****************************")
  print("** 1. Nhap sinh vien.")
  print("** 2. Cap nhat thong tin sinh vien theo ID.")
  print("** 3. Xoa sinh vien theo ID.")
  print("** 4. Tim kiem sinh vien theo ten.")
  print("** 5. Sap xep sinh vien theo diem trung binh.")
  print("** 6. Sap xep sinh vien theo ten chuyen nganh.")
  print("** 7. Hien thi danh sach sinh vien.")
  print("** 0. Thoat chuong trinh.")
  print("*************************************************************")

  key = int(input("Nhap lua chon cua ban: "))
  if(key==1):
    print("\n1. Nhap thong tin sinh vien.")
    qlsv.NhapSinhVien()
    print("\nThem sinh vien thanh cong")
  elif(key==2):
    if(qlsv.SoLuongSinhVien() > 0):
      print("\n2. Cap nhat thong tin sinh vien.")
      print("\nNhap ID sinh vien can cap nhat: ")
      ID = int(input())
      qlsv.updateSinhVien(ID)
    else:
      print("\nDanh sach sinh vien trong.")
  elif(key==3):
    if(qlsv.SoLuongSinhVien() > 0):
      print("\n3. Xoa sinh vien.")
      print("\nNhap ID sinh vien can xoa: ")
      ID = int(input())
      if(qlsv.deletedByID(ID)):
        print("\nXoa sinh vien co ID = ",ID, "thanh cong.")
      else:
        print("\nSinh vien co ID = ",ID, "khong ton tai.")
    else:
      print("\nDanh sach sinh vien trong.")
  elif(key==4):
    if(qlsv.SoLuongSinhVien() > 0):
      print("\n4. Tim kiem sinh vien theo ten.")
      print("\nNhap ten sinh vien can tim: ")
      name = input()
      searchResult = qlsv.findByName(name)
      qlsv.ShowSinhVien(searchResult)
    else:
      print("\nDanh sach sinh vien trong.")
  elif(key==5):
    if(qlsv.SoLuongSinhVien() > 0):
      print("\n5. Sap xep sinh vien theo diem trung binh.")
      qlsv.sortByDiemTB()
      qlsv.ShowSinhVien(qlsv.getListSinVien())
    else:
      print("\nDanh sach sinh vien trong.")
  elif(key==6):
    if(qlsv.SoLuongSinhVien() > 0):
      print("\n6. Sap xep sinh vien theo ten chuyen nganh.")
      qlsv.sortByName()
      qlsv.ShowSinhVien(qlsv.getListSinVien())
    else:
      print("\nDanh sach sinh vien trong.")
  elif(key==7):
    if(qlsv.SoLuongSinhVien() > 0):
      print("\n7. Hien thi danh sach sinh vien.")
      qlsv.ShowSinhVien(qlsv.getListSinVien())
    else:
      print("\nDanh sach sinh vien trong.")
  elif(key==0):
    print("\nCam on ban da su dung chuong trinh.")
    break
  else:
    print("\nLua chon khong hop le. Vui long chon lai.")