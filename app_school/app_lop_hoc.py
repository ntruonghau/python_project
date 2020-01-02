from flask import Markup, request, render_template, url_for, session, redirect
from app_school.xu_ly.Xu_ly_Form import Form_Create_Class
from app_school.xu_ly.nien_khoa.XL_Nien_khoa import doc_danh_sach_nien_khoa_select
from app_school.xu_ly.khoi.XL_Khoi import doc_danh_sach_khoi_select
from app_school.xu_ly.giao_vien.XL_Giao_vien import doc_danh_sach_gv_select
from app_school.xu_ly.lop_hoc.XL_Lop_hoc import doc_danh_sach_lop_hoc
from app_school.xu_ly.Xu_ly_Model import Lop
from app_school import app, db_session

@app.route('/danh-sach-lop', methods=['GET','POST'])
def danh_sach_lop():
    ds_lop_hoc = doc_danh_sach_lop_hoc()
    return render_template('lop_hoc/l_danh_sach_lop.html', ds_lop_hoc = ds_lop_hoc)

    
@app.route('/chi-tiet-lop/<string:lop>', methods=['GET','POST'])
def danh_sach_hoc_sinh(lop):
    return render_template('lop_hoc/l_chi_tiet_lop.html')

    
@app.route('/bang-diem-lop/<string:lop>', methods=['GET', 'POST'])
def bang_diem_lop(lop):
    return render_template('lop_hoc/l_bang_diem_lop.html')


@app.route('/them-lop-hoc', methods=['GET','POST'])
def them_lop_hoc():
    form = Form_Create_Class()
    ds_nien_khoa = doc_danh_sach_nien_khoa_select()
    ds_khoi = doc_danh_sach_khoi_select()
    ds_gv = doc_danh_sach_gv_select()
    form.Th_Nien_khoa.choices = ds_nien_khoa
    form.Th_Khoi.choices = ds_khoi
    form.Th_GV_Chu_nhiem.choices = ds_gv
    error = ''
    if form.validate_on_submit():
        TenLop = request.form['Th_Lop']
        DiaDiem = request.form['Th_Dia_diem']
        TongSoHS = 0
        NamNienKhoa = int(request.form['Th_Nien_khoa'])
        GV_CN = int(request.form['Th_GV_Chu_nhiem'])
        IDKhoi  = int(request.form['Th_Khoi'])
        lop_hoc = Lop(TenLop=TenLop, DiaDiem=DiaDiem, TongSoHS=TongSoHS, NamNienKhoa=NamNienKhoa, GV_CN=GV_CN, IDKhoi=IDKhoi)
        try:
            db_session.add(lop_hoc)
            db_session.commit()
            return redirect(url_for('danh_sach_lop'))
        except:
            db_session.rollback()
            error = 'Lớp học đã tồn tại'
            pass
    return render_template('lop_hoc/l_them_lop.html', form=form, error=error)