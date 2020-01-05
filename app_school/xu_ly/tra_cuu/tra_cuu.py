from flask import Markup, url_for
import json
import os
import sqlite3

Thu_muc_du_lieu ="app_school/du_lieu/"
# doc du_lieu tu CSDL
def Doc_danh_sach_hs_CSDL():
    conn = sqlite3.connect(Thu_muc_du_lieu + "ql_truong_hoc.db")
    list_dshs = []
    cursor = conn.execute("SELECT * FROM HocSinh")
    for row in cursor:        
        list_dshs.append(row)          
    conn.commit()
    conn.close()
    return list_dshs

def Doc_danh_sach_hs():
    Danh_sach = []    
    danh_sach_hs = Doc_danh_sach_hs_CSDL()
    for HocSinh in danh_sach_hs:    
        info_hs = {}
        info_hs["IDHocSinh"] = HocSinh[0]
        info_hs["HoVaTen"] = HocSinh[1]
        info_hs["GioiTinh"] = HocSinh[2]
        info_hs["DiaChi"] = HocSinh[3]
        info_hs["Email"] = HocSinh[4]
        info_hs["NgaySinh"] = HocSinh[5]
        info_hs["SoDienThoai"] = HocSinh[6]
        info_hs["SoDienThoaiPhuHuynh"] = HocSinh[7]
        info_hs["IDLop"] = HocSinh[8]
        info_hs["NienKhoa"] = HocSinh[9]
        Danh_sach.append(info_hs)
    return Danh_sach

def Lay_info_theo_ID(ID, Danh_sach_CHTN):
    Danh_sach=list(filter(
        lambda HocSinh: str(ID).strip() == str(HocSinh["IDHocSinh"]).strip() ,Danh_sach_CHTN))
    return Danh_sach[0]