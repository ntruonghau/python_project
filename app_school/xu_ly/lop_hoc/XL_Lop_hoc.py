from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import Lop, GiaoVien, Khoi, NienKhoa

def doc_danh_sach_lop_hoc(): # select field tupple choice
    ds_lop = []
    try:
        ds_l = db_session.query(Lop).all()
        for lop in ds_l:
            l = lop.__dict__
            del l['_sa_instance_state']
            chu_nhiem = db_session.query(GiaoVien).filter(GiaoVien.IDGiaoVien == l['GV_CN']).one()
            khoi = db_session.query(Khoi).filter(Khoi.IDKhoi == l['IDKhoi']).one()
            nien_khoa = db_session.query(NienKhoa).filter(NienKhoa.ID == l['NamNienKhoa']).one()
            l['Ten_Chu_nhiem'] = chu_nhiem.HoVaTen
            l['Ten_Khoi'] = khoi.TenKhoi
            l['Ten_Nien_khoa'] = nien_khoa.NamNienKhoa
            ds_lop.append(l)
    except:
        pass
    return ds_lop

def lay_nien_khoa_theo_lop(lop):
    try:
        lop = db_session.query(Lop).filter(Lop.IDLop == lop).one()
        nien_khoa = db_session.query(NienKhoa).filter(NienKhoa.ID == lop.NamNienKhoa).one()
    except:
        pass
    return nien_khoa