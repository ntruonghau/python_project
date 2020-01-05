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
    TKB = {"Lop" : "", "NienKhoa" : "" , "Thu2": [],"Thu3":[],"Thu4":[],"Thu5":[],"Thu6":[], "Thu7":[]}
    lop = db_session.query(Lop).filter(Lop.IDLop == ThoiKhoaBieu.ID_Lop).first()
    ten_lop = lop.TenLop
    nienKhoa = db_session.query(NienKhoa).filter(NienKhoa.ID == lop.NamNienKhoa).first()
    nam_hoc = nienKhoa.NamNienKhoa

    TKB['Lop'] = ten_lop
    TKB['NienKhoa'] = nam_hoc

    Thu2_1 = json.loads(ThoiKhoaBieu.Thu2)
    Thu2_1['Thu2'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu2_1['Thu2'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'])
    Thu2_1['Thu2'][0]['BuoiSang'][0]['Tiet1']['Mon'] = ten_mon(Thu2_1['Thu2'][0]['BuoiSang'][0]['Tiet1']['Mon'])
    
    Thu2_1['Thu2'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu2_1['Thu2'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'])
    Thu2_1['Thu2'][0]['BuoiSang'][1]['Tiet2']['Mon'] = ten_mon(Thu2_1['Thu2'][0]['BuoiSang'][1]['Tiet2']['Mon'])

    Thu2_1['Thu2'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu2_1['Thu2'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'])
    Thu2_1['Thu2'][0]['BuoiSang'][2]['Tiet3']['Mon'] = ten_mon(Thu2_1['Thu2'][0]['BuoiSang'][2]['Tiet3']['Mon'])

    Thu2_1['Thu2'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu2_1['Thu2'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'])
    Thu2_1['Thu2'][0]['BuoiSang'][3]['Tiet4']['Mon'] = ten_mon(Thu2_1['Thu2'][0]['BuoiSang'][3]['Tiet4']['Mon'])

    Thu2_1['Thu2'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu2_1['Thu2'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'])
    Thu2_1['Thu2'][1]['BuoiChieu'][0]['Tiet1']['Mon'] = ten_mon(Thu2_1['Thu2'][1]['BuoiChieu'][0]['Tiet1']['Mon'])
    
    Thu2_1['Thu2'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu2_1['Thu2'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'])
    Thu2_1['Thu2'][1]['BuoiChieu'][1]['Tiet2']['Mon'] = ten_mon(Thu2_1['Thu2'][1]['BuoiChieu'][1]['Tiet2']['Mon'])

    Thu2_1['Thu2'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu2_1['Thu2'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'])
    Thu2_1['Thu2'][1]['BuoiChieu'][2]['Tiet3']['Mon'] = ten_mon(Thu2_1['Thu2'][1]['BuoiChieu'][2]['Tiet3']['Mon'])

    Thu2_1['Thu2'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu2_1['Thu2'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'])
    Thu2_1['Thu2'][1]['BuoiChieu'][3]['Tiet4']['Mon'] = ten_mon(Thu2_1['Thu2'][1]['BuoiChieu'][3]['Tiet4']['Mon'])

#thu 3
    Thu3_1 = json.loads(ThoiKhoaBieu.Thu3)
    Thu3_1['Thu3'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu3_1['Thu3'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'])
    Thu3_1['Thu3'][0]['BuoiSang'][0]['Tiet1']['Mon'] = ten_mon(Thu3_1['Thu3'][0]['BuoiSang'][0]['Tiet1']['Mon'])
    
    Thu3_1['Thu3'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu3_1['Thu3'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'])
    Thu3_1['Thu3'][0]['BuoiSang'][1]['Tiet2']['Mon'] = ten_mon(Thu3_1['Thu3'][0]['BuoiSang'][1]['Tiet2']['Mon'])

    Thu3_1['Thu3'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu3_1['Thu3'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'])
    Thu3_1['Thu3'][0]['BuoiSang'][2]['Tiet3']['Mon'] = ten_mon(Thu3_1['Thu3'][0]['BuoiSang'][2]['Tiet3']['Mon'])

    Thu3_1['Thu3'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu3_1['Thu3'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'])
    Thu3_1['Thu3'][0]['BuoiSang'][3]['Tiet4']['Mon'] = ten_mon(Thu3_1['Thu3'][0]['BuoiSang'][3]['Tiet4']['Mon'])

    Thu3_1['Thu3'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu3_1['Thu3'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'])
    Thu3_1['Thu3'][1]['BuoiChieu'][0]['Tiet1']['Mon'] = ten_mon(Thu3_1['Thu3'][1]['BuoiChieu'][0]['Tiet1']['Mon'])
    
    Thu3_1['Thu3'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu3_1['Thu3'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'])
    Thu3_1['Thu3'][1]['BuoiChieu'][1]['Tiet2']['Mon'] = ten_mon(Thu3_1['Thu3'][1]['BuoiChieu'][1]['Tiet2']['Mon'])

    Thu3_1['Thu3'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu3_1['Thu3'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'])
    Thu3_1['Thu3'][1]['BuoiChieu'][2]['Tiet3']['Mon'] = ten_mon(Thu3_1['Thu3'][1]['BuoiChieu'][2]['Tiet3']['Mon'])

    Thu3_1['Thu3'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu3_1['Thu3'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'])
    Thu3_1['Thu3'][1]['BuoiChieu'][3]['Tiet4']['Mon'] = ten_mon(Thu3_1['Thu3'][1]['BuoiChieu'][3]['Tiet4']['Mon'])

 #Thu 4
    Thu4_1 = json.loads(ThoiKhoaBieu.Thu4)
    Thu4_1['Thu4'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu4_1['Thu4'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'])
    Thu4_1['Thu4'][0]['BuoiSang'][0]['Tiet1']['Mon'] = ten_mon(Thu4_1['Thu4'][0]['BuoiSang'][0]['Tiet1']['Mon'])
    
    Thu4_1['Thu4'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu4_1['Thu4'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'])
    Thu4_1['Thu4'][0]['BuoiSang'][1]['Tiet2']['Mon'] = ten_mon(Thu4_1['Thu4'][0]['BuoiSang'][1]['Tiet2']['Mon'])

    Thu4_1['Thu4'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu4_1['Thu4'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'])
    Thu4_1['Thu4'][0]['BuoiSang'][2]['Tiet3']['Mon'] = ten_mon(Thu4_1['Thu4'][0]['BuoiSang'][2]['Tiet3']['Mon'])

    Thu4_1['Thu4'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu4_1['Thu4'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'])
    Thu4_1['Thu4'][0]['BuoiSang'][3]['Tiet4']['Mon'] = ten_mon(Thu4_1['Thu4'][0]['BuoiSang'][3]['Tiet4']['Mon'])

    Thu4_1['Thu4'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu4_1['Thu4'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'])
    Thu4_1['Thu4'][1]['BuoiChieu'][0]['Tiet1']['Mon'] = ten_mon(Thu4_1['Thu4'][1]['BuoiChieu'][0]['Tiet1']['Mon'])
    
    Thu4_1['Thu4'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu4_1['Thu4'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'])
    Thu4_1['Thu4'][1]['BuoiChieu'][1]['Tiet2']['Mon'] = ten_mon(Thu4_1['Thu4'][1]['BuoiChieu'][1]['Tiet2']['Mon'])

    Thu4_1['Thu4'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu4_1['Thu4'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'])
    Thu4_1['Thu4'][1]['BuoiChieu'][2]['Tiet3']['Mon'] = ten_mon(Thu4_1['Thu4'][1]['BuoiChieu'][2]['Tiet3']['Mon'])

    Thu4_1['Thu4'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu4_1['Thu4'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'])
    Thu4_1['Thu4'][1]['BuoiChieu'][3]['Tiet4']['Mon'] = ten_mon(Thu4_1['Thu4'][1]['BuoiChieu'][3]['Tiet4']['Mon'])

#thu 5
    Thu5_1 = json.loads(ThoiKhoaBieu.Thu5)
    Thu5_1['Thu5'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu5_1['Thu5'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'])
    Thu5_1['Thu5'][0]['BuoiSang'][0]['Tiet1']['Mon'] = ten_mon(Thu5_1['Thu5'][0]['BuoiSang'][0]['Tiet1']['Mon'])
    
    Thu5_1['Thu5'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu5_1['Thu5'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'])
    Thu5_1['Thu5'][0]['BuoiSang'][1]['Tiet2']['Mon'] = ten_mon(Thu5_1['Thu5'][0]['BuoiSang'][1]['Tiet2']['Mon'])

    Thu5_1['Thu5'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu5_1['Thu5'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'])
    Thu5_1['Thu5'][0]['BuoiSang'][2]['Tiet3']['Mon'] = ten_mon(Thu5_1['Thu5'][0]['BuoiSang'][2]['Tiet3']['Mon'])

    Thu5_1['Thu5'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu5_1['Thu5'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'])
    Thu5_1['Thu5'][0]['BuoiSang'][3]['Tiet4']['Mon'] = ten_mon(Thu5_1['Thu5'][0]['BuoiSang'][3]['Tiet4']['Mon'])

    Thu5_1['Thu5'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu5_1['Thu5'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'])
    Thu5_1['Thu5'][1]['BuoiChieu'][0]['Tiet1']['Mon'] = ten_mon(Thu5_1['Thu5'][1]['BuoiChieu'][0]['Tiet1']['Mon'])
    
    Thu5_1['Thu5'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu5_1['Thu5'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'])
    Thu5_1['Thu5'][1]['BuoiChieu'][1]['Tiet2']['Mon'] = ten_mon(Thu5_1['Thu5'][1]['BuoiChieu'][1]['Tiet2']['Mon'])

    Thu5_1['Thu5'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu5_1['Thu5'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'])
    Thu5_1['Thu5'][1]['BuoiChieu'][2]['Tiet3']['Mon'] = ten_mon(Thu5_1['Thu5'][1]['BuoiChieu'][2]['Tiet3']['Mon'])

    Thu5_1['Thu5'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu5_1['Thu5'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'])
    Thu5_1['Thu5'][1]['BuoiChieu'][3]['Tiet4']['Mon'] = ten_mon(Thu5_1['Thu5'][1]['BuoiChieu'][3]['Tiet4']['Mon'])

#thu 6
    Thu6_1 = json.loads(ThoiKhoaBieu.Thu6)
    Thu6_1['Thu6'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu6_1['Thu6'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'])
    Thu6_1['Thu6'][0]['BuoiSang'][0]['Tiet1']['Mon'] = ten_mon(Thu6_1['Thu6'][0]['BuoiSang'][0]['Tiet1']['Mon'])
    
    Thu6_1['Thu6'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu6_1['Thu6'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'])
    Thu6_1['Thu6'][0]['BuoiSang'][1]['Tiet2']['Mon'] = ten_mon(Thu6_1['Thu6'][0]['BuoiSang'][1]['Tiet2']['Mon'])

    Thu6_1['Thu6'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu6_1['Thu6'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'])
    Thu6_1['Thu6'][0]['BuoiSang'][2]['Tiet3']['Mon'] = ten_mon(Thu6_1['Thu6'][0]['BuoiSang'][2]['Tiet3']['Mon'])

    Thu6_1['Thu6'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu6_1['Thu6'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'])
    Thu6_1['Thu6'][0]['BuoiSang'][3]['Tiet4']['Mon'] = ten_mon(Thu6_1['Thu6'][0]['BuoiSang'][3]['Tiet4']['Mon'])

    Thu6_1['Thu6'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu6_1['Thu6'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'])
    Thu6_1['Thu6'][1]['BuoiChieu'][0]['Tiet1']['Mon'] = ten_mon(Thu6_1['Thu6'][1]['BuoiChieu'][0]['Tiet1']['Mon'])
    
    Thu6_1['Thu6'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu6_1['Thu6'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'])
    Thu6_1['Thu6'][1]['BuoiChieu'][1]['Tiet2']['Mon'] = ten_mon(Thu6_1['Thu6'][1]['BuoiChieu'][1]['Tiet2']['Mon'])

    Thu6_1['Thu6'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu6_1['Thu6'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'])
    Thu6_1['Thu6'][1]['BuoiChieu'][2]['Tiet3']['Mon'] = ten_mon(Thu6_1['Thu6'][1]['BuoiChieu'][2]['Tiet3']['Mon'])

    Thu6_1['Thu6'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu6_1['Thu6'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'])
    Thu6_1['Thu6'][1]['BuoiChieu'][3]['Tiet4']['Mon'] = ten_mon(Thu6_1['Thu6'][1]['BuoiChieu'][3]['Tiet4']['Mon'])
#thu 7
    Thu7_1 = json.loads(ThoiKhoaBieu.Thu7)
    Thu7_1['Thu7'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu7_1['Thu7'][0]['BuoiSang'][0]['Tiet1']['GiaoVien'])
    Thu7_1['Thu7'][0]['BuoiSang'][0]['Tiet1']['Mon'] = ten_mon(Thu7_1['Thu7'][0]['BuoiSang'][0]['Tiet1']['Mon'])
    
    Thu7_1['Thu7'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu7_1['Thu7'][0]['BuoiSang'][1]['Tiet2']['GiaoVien'])
    Thu7_1['Thu7'][0]['BuoiSang'][1]['Tiet2']['Mon'] = ten_mon(Thu7_1['Thu7'][0]['BuoiSang'][1]['Tiet2']['Mon'])

    Thu7_1['Thu7'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu7_1['Thu7'][0]['BuoiSang'][2]['Tiet3']['GiaoVien'])
    Thu7_1['Thu7'][0]['BuoiSang'][2]['Tiet3']['Mon'] = ten_mon(Thu7_1['Thu7'][0]['BuoiSang'][2]['Tiet3']['Mon'])

    Thu7_1['Thu7'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu7_1['Thu7'][0]['BuoiSang'][3]['Tiet4']['GiaoVien'])
    Thu7_1['Thu7'][0]['BuoiSang'][3]['Tiet4']['Mon'] = ten_mon(Thu7_1['Thu7'][0]['BuoiSang'][3]['Tiet4']['Mon'])

    Thu7_1['Thu7'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'] = ten_giao_vien(Thu7_1['Thu7'][1]['BuoiChieu'][0]['Tiet1']['GiaoVien'])
    Thu7_1['Thu7'][1]['BuoiChieu'][0]['Tiet1']['Mon'] = ten_mon(Thu7_1['Thu7'][1]['BuoiChieu'][0]['Tiet1']['Mon'])
    
    Thu7_1['Thu7'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'] = ten_giao_vien(Thu7_1['Thu7'][1]['BuoiChieu'][1]['Tiet2']['GiaoVien'])
    Thu7_1['Thu7'][1]['BuoiChieu'][1]['Tiet2']['Mon'] = ten_mon(Thu7_1['Thu7'][1]['BuoiChieu'][1]['Tiet2']['Mon'])

    Thu7_1['Thu7'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'] = ten_giao_vien(Thu7_1['Thu7'][1]['BuoiChieu'][2]['Tiet3']['GiaoVien'])
    Thu7_1['Thu7'][1]['BuoiChieu'][2]['Tiet3']['Mon'] = ten_mon(Thu7_1['Thu7'][1]['BuoiChieu'][2]['Tiet3']['Mon'])

    Thu7_1['Thu7'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'] = ten_giao_vien(Thu7_1['Thu7'][1]['BuoiChieu'][3]['Tiet4']['GiaoVien'])
    Thu7_1['Thu7'][1]['BuoiChieu'][3]['Tiet4']['Mon'] = ten_mon(Thu7_1['Thu7'][1]['BuoiChieu'][3]['Tiet4']['Mon'])


    TKB['Thu2'].append(Thu2_1['Thu2'])
    TKB['Thu3'].append(Thu3_1['Thu3'])
    TKB['Thu4'].append(Thu4_1['Thu4'])
    TKB['Thu5'].append(Thu5_1['Thu5'])
    TKB['Thu6'].append(Thu6_1['Thu6'])
    TKB['Thu7'].append(Thu7_1['Thu7'])

    return TKB