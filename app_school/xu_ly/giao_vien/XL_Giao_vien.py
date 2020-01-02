from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import GiaoVien

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