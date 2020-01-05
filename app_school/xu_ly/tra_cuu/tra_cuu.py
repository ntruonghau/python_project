from flask import Markup, url_for
import json
import os
import sqlite3

Thu_muc_du_lieu ="app_school/du_lieu/"
# doc du_lieu tu CSDL
def Doc_danh_sach_hs():
    conn = sqlite3.connect(Thu_muc_du_lieu + "ql_truong_hoc.db")
    list_chtn = []
    cursor = conn.execute("SELECT * FROM HocSinh")
    for row in cursor:        
        list_chtn.append(row)          
    conn.commit()
    conn.close()
    return list_chtn

def Lay_info_theo_ID(ID, Danh_sach_CHTN):
    Danh_sach=list(filter(
        lambda HocSinh: str(ID).strip() == str(HocSinh["IDHocSinh"]).strip() ,Danh_sach_CHTN))
    return Danh_sach[0]
