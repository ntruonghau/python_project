from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import *
from app_school.xu_ly.giao_vien.XL_Giao_vien import *
from app_school.xu_ly.nien_khoa.XL_Nien_khoa import *
from datetime import datetime

def load_danh_sach_hoat_dong(Nien_Khoa,hocsinh):
    hdong = db_session.query(Hoat_Dong).filter(Hoat_Dong.NienKhoa == Nien_Khoa).all()
    lp = db_session.query(Lop).filter(Lop.IDLop == hocsinh.IDLop).one()

    danh_sach_hoat_dong =[]

    for i in hdong:
        danh_sach_doi_tuong = []
        if i.Khoi_10 == 1:
            danh_sach_doi_tuong.append(1)
        if i.Khoi_11 == 1:
            danh_sach_doi_tuong.append(2)
        if i.Khoi_12 == 1:
            danh_sach_doi_tuong.append(3)  

        if lp.IDKhoi in danh_sach_doi_tuong:
            hoatdong = {}
            t = db_session.query(Tham_Gia_Hoat_Dong).filter(Tham_Gia_Hoat_Dong.IDHocSinh == hocsinh.IDHocSinh, Tham_Gia_Hoat_Dong.IDHoatDong == i.IDHoatDong).first()
            if t != None:
                hoatdong['TinhTrang'] =  "Đã Tham Gia"
            else:
                hoatdong['TinhTrang'] =  "Tham Gia"

            hoatdong['IDHoatDong'] = str(i.IDHoatDong)
            hoatdong['TieuDe'] = i.TieuDe
            hoatdong['NoiDung'] = i.NoiDung
            hoatdong['NguoiTao'] = ten_giao_vien(i.GiaoVienTao)
            hoatdong['ThoiHan'] =  datetime.strptime(i.ThoiHanDangKy, '%d-%m-%Y')
            hoatdong['NienKhoa'] = ten_nien_khoa(i.NienKhoa)
            hoatdong['SoNguoiThamGia'] =  i.SoNguoiDaThamGia


            danh_sach_hoat_dong.append(hoatdong)
    return(danh_sach_hoat_dong)