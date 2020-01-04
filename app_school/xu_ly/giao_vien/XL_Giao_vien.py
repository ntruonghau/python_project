from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import GiaoVien
from datetime import datetime
def doc_danh_sach_gv_select(): # select field tupple choice
    ds_giao_vien = []
    try:
        ds_gv = db_session.query(GiaoVien).all()
        for giao_vien in ds_gv:
            gv = (giao_vien.IDGiaoVien,  giao_vien.HoVaTen + ' - ' + giao_vien.TenDangNhap)
            ds_giao_vien.append(gv)
    except:
        pass
    return ds_giao_vien

def Profile_Giao_Vien(TaiKhoan):
    gv1 = db_session.query(GiaoVien).filter(GiaoVien.TenDangNhap == TaiKhoan).first()
    if (gv1.NgaySinh == None):
        gv1.NgaySinh = '1900-01-01'
    gv = {"HoVaTen": gv1.HoVaTen, "GioiTinh": gv1.GioiTinh, "NgaySinh": datetime.strptime(gv1.NgaySinh,'%Y-%m-%d' ).date(), "Email": gv1.Email, "DiaChi" : gv1.DiaChi,
         "SoDienThoai": gv1.SoDienThoai, "TrinhDo":gv1.TrinhDo,"ChuyenMon": gv1.ChuyenMon}
    return gv