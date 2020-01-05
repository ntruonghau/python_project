from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import *
import json

def ten_giao_vien(giao_vien):
    gv = db_session.query(GiaoVien).filter(GiaoVien.TenDangNhap == giao_vien).first()
    return gv.HoVaTen

def ten_mon(mon):
    mon = db_session.query(Mon).filter(Mon.IDMon == mon).first()
    return mon.TenMon

def tao_thoi_khoa_bieu(ThoiKhoaBieu):
    TKB = {}
    Thu2 =json.loads(ThoiKhoaBieu.Thu2)
    for i in range(1,5):
        Thu2['Sang'][str(i)]['GiaoVien'] = ten_giao_vien( Thu2['Sang'][str(i)]['GiaoVien'])
        Thu2['Sang'][str(i)]['Mon'] = ten_mon( Thu2['Sang'][str(i)]['Mon'])

        Thu2['Chieu'][str(i)]['GiaoVien'] = ten_giao_vien( Thu2['Chieu'][str(i)]['GiaoVien'])
        Thu2['Chieu'][str(i)]['Mon'] = ten_mon( Thu2['Chieu'][str(i)]['Mon'])

    Thu3 =json.loads(ThoiKhoaBieu.Thu3) 
    for i in range(1,5):
        Thu3['Sang'][str(i)]['GiaoVien'] = ten_giao_vien( Thu3['Sang'][str(i)]['GiaoVien'])
        Thu3['Sang'][str(i)]['Mon'] = ten_mon( Thu3['Sang'][str(i)]['Mon'])

        Thu3['Chieu'][str(i)]['GiaoVien'] = ten_giao_vien( Thu3['Chieu'][str(i)]['GiaoVien'])
        Thu3['Chieu'][str(i)]['Mon'] = ten_mon( Thu3['Chieu'][str(i)]['Mon'])   

    Thu4 =json.loads(ThoiKhoaBieu.Thu4)  
    for i in range(1,5):
        Thu4['Sang'][str(i)]['GiaoVien'] = ten_giao_vien( Thu4['Sang'][str(i)]['GiaoVien'])
        Thu4['Sang'][str(i)]['Mon'] = ten_mon( Thu4['Sang'][str(i)]['Mon'])

        Thu4['Chieu'][str(i)]['GiaoVien'] = ten_giao_vien( Thu4['Chieu'][str(i)]['GiaoVien'])
        Thu4['Chieu'][str(i)]['Mon'] = ten_mon( Thu4['Chieu'][str(i)]['Mon'])  

    Thu5 =json.loads(ThoiKhoaBieu.Thu5)  
    for i in range(1,5):
        Thu5['Sang'][str(i)]['GiaoVien'] = ten_giao_vien( Thu5['Sang'][str(i)]['GiaoVien'])
        Thu5['Sang'][str(i)]['Mon'] = ten_mon( Thu5['Sang'][str(i)]['Mon'])

        Thu5['Chieu'][str(i)]['GiaoVien'] = ten_giao_vien( Thu5['Chieu'][str(i)]['GiaoVien'])
        Thu5['Chieu'][str(i)]['Mon'] = ten_mon( Thu5['Chieu'][str(i)]['Mon'])  

    Thu6 =json.loads(ThoiKhoaBieu.Thu6)  
    for i in range(1,5):
        Thu6['Sang'][str(i)]['GiaoVien'] = ten_giao_vien( Thu6['Sang'][str(i)]['GiaoVien'])
        Thu6['Sang'][str(i)]['Mon'] = ten_mon( Thu6['Sang'][str(i)]['Mon'])

        Thu6['Chieu'][str(i)]['GiaoVien'] = ten_giao_vien( Thu6['Chieu'][str(i)]['GiaoVien'])
        Thu6['Chieu'][str(i)]['Mon'] = ten_mon( Thu6['Chieu'][str(i)]['Mon'])  

    Thu7 =json.loads(ThoiKhoaBieu.Thu7)  
    for i in range(1,5):
        Thu7['Sang'][str(i)]['GiaoVien'] = ten_giao_vien( Thu7['Sang'][str(i)]['GiaoVien'])
        Thu7['Sang'][str(i)]['Mon'] = ten_mon( Thu7['Sang'][str(i)]['Mon'])

        Thu7['Chieu'][str(i)]['GiaoVien'] = ten_giao_vien( Thu7['Chieu'][str(i)]['GiaoVien'])
        Thu7['Chieu'][str(i)]['Mon'] = ten_mon( Thu7['Chieu'][str(i)]['Mon']) 
         
    TKB['Thu2'] = Thu2
    TKB['Thu3'] = Thu3
    TKB['Thu4'] = Thu4
    TKB['Thu5'] = Thu5
    TKB['Thu6'] = Thu6
    TKB['Thu7'] = Thu7

    TKB['Lop'] = ""
    TKB['NienKhoa'] = ""
    return TKB