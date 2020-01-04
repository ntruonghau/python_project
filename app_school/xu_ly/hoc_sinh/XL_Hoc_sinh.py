from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import HocSinh,Lop,NienKhoa
from datetime import datetime

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

def Profile_hoc_sinh(id_hs):
    hoc_sinh = db_session.query(HocSinh).filter(HocSinh.IDHocSinh == id_hs).first()
    lop_hoc = db_session.query(Lop).filter(Lop.IDLop == hoc_sinh.IDLop).first()
    nien_khoa = db_session.query(NienKhoa).filter(NienKhoa.ID == hoc_sinh.IDNienKhoa).first()
    hs = {"IDHocSinh": hoc_sinh.IDHocSinh,"HoVaTen": hoc_sinh.HoVaTen, "GioiTinh": hoc_sinh.GioiTinh, "NgaySinh": datetime.strptime(hoc_sinh.NgaySinh,'%Y-%m-%d' ).date(), "Email": hoc_sinh.Email, "DiaChi" : hoc_sinh.DiaChi,
         "SoDienThoai": hoc_sinh.SoDienThoai, "SoDienThoaiPH":hoc_sinh.SoDienThoaiPhuHuynh,"Lop": lop_hoc.TenLop,"NienKhoa": nien_khoa.NamNienKhoa }
    return hs
    