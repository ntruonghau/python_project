from flask import Markup, url_for
import json
import os
import sqlite3
from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import QuanLi
from datetime import datetime

Thu_muc_du_lieu ="app_school/du_lieu/"

def Doc_danh_sach_lh_CSDL():
    conn = sqlite3.connect(Thu_muc_du_lieu + "ql_truong_hoc.db")
    list_dslh = []
    cursor = conn.execute("SELECT * FROM LienHe")
    for row in cursor:        
        list_dslh.append(row)          
    conn.commit()
    conn.close()
    return list_dslh

def Doc_danh_sach_lh():
    Danh_sach = []    
    danh_sach_lh = Doc_danh_sach_lh_CSDL()
    for LienHe in danh_sach_lh:    
        info_lh = {}
        info_lh["Người gửi"] = LienHe[0]
        info_lh["Email"] = LienHe[1]
        info_lh["Nội dung"] = LienHe[2]

        Danh_sach.append(info_lh)
    return Danh_sach

def Doc_danh_sach_lh_email():
    Danh_sach = []    
    danh_sach_lh = Doc_danh_sach_lh_CSDL()
    for LienHe in danh_sach_lh:    
        info_lh = {}
        info_lh["Email"] = LienHe[0]
        Danh_sach.append(info_lh)
    return Danh_sach

def Lay_info_theo_Email(Email, Danh_sach_LienHe):
    Danh_sach=list(filter(
        lambda LienHe: str(Email).strip() == str(LienHe["Email"]).strip() ,Danh_sach_LienHe))
    return Danh_sach[0]

def Them_tai_khoan(Danh_sach_info) :
    conn = sqlite3.connect(Thu_muc_du_lieu + "ql_truong_hoc.db")
    sql = "INSERT INTO GiaoVien (IDGiaoVien,TenDangNhap,MatKhau,HoVaTen,Email) \
            VALUES (?,?,?,?,?)"
    if conn.execute(sql,(Danh_sach_info[0],Danh_sach_info[1],Danh_sach_info[2],Danh_sach_info[3],Danh_sach_info[4])) :
        print("Đã thêm tài khoản thành công !")
    conn.commit()
    conn.close()


def Profile_Quan_li(TaiKhoan):
    ql1 = db_session.query(QuanLi).filter(QuanLi.TenDangNhap == TaiKhoan).first()
    ql = {"HoVaTen": ql1.HoVaTen, "GioiTinh": ql1.GioiTinh, "NgaySinh": datetime.strptime(ql1.NgaySinh,'%Y-%m-%d' ).date(), "Email": ql1.Email, "DiaChi" : ql1.DiaChi,
         "SoDienThoai": ql1.SoDienThoai, "ID_GV": ql1.IDQuanLi}
    return ql