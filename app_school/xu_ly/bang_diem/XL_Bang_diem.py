from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import BangDiem, HocSinh

def doc_danh_sach_bang_diem_hoc(): # select field tupple choice
    ds_bang_diem = []
    try:
        ds_bangdiem = db_session.query(BangDiem).all()
        for bang_diem in ds_bangdiem:
            bd = (bang_diem.IDbang_diem, bang_diem.Tenbang_diem)
            ds_bang_diem.append(bd)
    except:
        pass
    return ds_bang_diem

def tao_bang_diem_cho_hoc_sinh(id_hoc_sinh):
    hoc_sinh = db_session.query(HocSinh).filter(HocSinh.IDHocSinh == id_hoc_sinh).one()
    