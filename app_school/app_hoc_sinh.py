from flask import Markup, request, render_template, url_for, session, redirect
from app_school.xu_ly.Xu_ly_Form import *
from app_school.xu_ly.lop_hoc.XL_Lop_hoc import lay_nien_khoa_theo_lop
from app_school.xu_ly.Xu_ly_Model import HocSinh
from app_school.xu_ly.hoc_sinh.XL_Hoc_sinh import *
from app_school import app, db_session
from datetime import date

@app.route('/them-hoc-sinh/<string:lop>', methods=['GET', 'POST'])
def them_hoc_sinh(lop):
    form = Form_Update_Hs()
    error = ''
    if form.validate_on_submit():
        HoVaTen = request.form['Th_Ho_ten']
        GioiTinh = request.form['Th_Gioi_tinh']
        DiaChi = request.form['Th_Dia_chi']
        Email = request.form['Th_Email']
        NgaySinh = request.form['Th_Ngay_sinh']
        SoDienThoai = request.form['Th_Sdt']
        SoDienThoaiPhuHuynh = request.form['Th_Sdt_PH']
        IDLop = lop
        nien_khoa = lay_nien_khoa_theo_lop(lop)
        IDNienKhoa = nien_khoa.ID
        hoc_sinh = HocSinh(HoVaTen=HoVaTen, GioiTinh=GioiTinh, DiaChi=DiaChi, Email=Email, NgaySinh=NgaySinh,
                           SoDienThoai=SoDienThoai, SoDienThoaiPhuHuynh=SoDienThoaiPhuHuynh, IDLop=IDLop, IDNienKhoa=IDNienKhoa)
        try:
            db_session.add(hoc_sinh)
            db_session.commit()
            return redirect("/chi-tiet-lop/" + lop)
        except:
            error = 'Học sinh đã tồn tại'
            db_session.rollback()
            pass
    return render_template('hoc_sinh/hs_them_hoc_sinh.html', form=form, error=error)


@app.route('/thong-tin-diem-so/<string:hoc_sinh>', methods=['GET','POST'])
def thong_tin_diem_so(hoc_sinh):
    return render_template('giao_vien/gv_bang_diem_hoc_sinh.html')


@app.route('/thong-tin-hoc-sinh/<string:hoc_sinh>', methods=['GET','POST'])
def thong_tin_hoc_sinh(hoc_sinh):
    id_hoc_sinh = hoc_sinh
    HocSinh = Profile_hoc_sinh(id_hoc_sinh)
    print(HocSinh)
    return render_template('hoc_sinh/hs_thong_tin_hoc_sinh.html',HocSinh=HocSinh)

@app.route('/thong-tin-hoc-sinh/<string:hoc_sinh>/sua-hoc-sinh', methods=['GET','POST'])
def sua_thong_tin_hoc_sinh(hoc_sinh):
    form = Form_Update_Hs()
    id_hoc_sinh = hoc_sinh
    HocSinh = Profile_hoc_sinh(id_hoc_sinh)
    print(HocSinh)
    return render_template('hoc_sinh/hs_sua_thong_tin.html',HocSinh=HocSinh,form=form )