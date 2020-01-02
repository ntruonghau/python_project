from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import HocSinh,Lop,NienKhoa

def doc_danh_sach_hoc_sinh_theo_lop(lop): # select field tupple choice
    ds_hoc_sinh = []
    try:
        ds_hs = db_session.query(HocSinh).filter(HocSinh.IDLop == lop).all()
        for hoc_sinh in ds_hs:
            hs = hoc_sinh.__dict__
            del hs['_sa_instance_state']
            lop_hoc = db_session.query(Lop).filter(Lop.IDLop == lop).one()
            nien_khoa = db_session.query(NienKhoa).filter(NienKhoa.ID == hs['IDNienKhoa']).one()
            hs['Ten_Lop'] = lop_hoc.TenLop
            hs['Ten_Nien_khoa'] = nien_khoa.NamNienKhoa
            ds_hoc_sinh.append(hs)
    except:
        pass
    return ds_hoc_sinh