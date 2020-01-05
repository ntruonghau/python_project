from flask import Markup, request, render_template, url_for, session, redirect
from app_school.xu_ly.giao_vien.XL_Giao_vien import *
from app_school.xu_ly.bang_diem.XL_Bang_diem import doc_bang_diem_theo_id_bang_diem, cap_nhat_bang_diem
from app_school.xu_ly.hoc_sinh.XL_Hoc_sinh import Profile_hoc_sinh
from app_school.xu_ly.thoi_khoa_bieu.XL_TKB import *
from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import GiaoVien, Mon, HocSinh, BangDiem
from app_school.xu_ly.Xu_ly_Form import *
import json

@app.route('/giao-vien', methods=['GET','POST'])
def giao_vien():
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    giaovien = session['giaovien']
    message = ''
    giao_vien = Profile_Giao_Vien(giaovien)
    if request.args.get('message'):
        message = request.args.get('message')
        print(message)

    return render_template('giao_vien/gv_dashboard.html',giao_vien = giao_vien, message=message)

@app.route('/sua-profile', methods=['GEt','POST'])
def edit_giao_vien():
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    error = ''
    giaovien = session['giaovien']
    giao_vien = Profile_Giao_Vien(giaovien)
    form = Form_Update_Gv()
    if form.validate_on_submit():
        HoVaTen = request.form['Th_Ho_ten']
        GioiTinh = request.form['Th_Gioi_tinh']
        NgaySinh = request.form['Th_Ngay_sinh']
        DiaChi = request.form['Th_Dia_chi']
        Email = request.form['Th_Email']
        SoDienThoai = request.form['Th_Sdt']
        TrinhDo = request.form['Th_Trinh_do']
        ChuyenMon = request.form['Th_Chuyen_mon']

        gv = {"HoVaTen": HoVaTen, "GioiTinh": GioiTinh, "NgaySinh": NgaySinh, "Email": Email, "DiaChi" : DiaChi,
         "SoDienThoai": SoDienThoai, "TrinhDo": TrinhDo,"ChuyenMon": ChuyenMon}

        value = db_session.query(GiaoVien).filter(GiaoVien.TenDangNhap == giaovien).first()

        value.HoVaTen = gv['HoVaTen']
        value.GioiTinh = gv['GioiTinh']
        value.NgaySinh =  datetime.strptime(gv['NgaySinh'],'%Y-%m-%d' ).date()
        value.Email = gv['Email']
        value.DiaChi = gv['DiaChi']
        value.SoDienThoai = gv['SoDienThoai']
        value.TrinhDo = gv['TrinhDo']
        value.ChuyenMon = gv['ChuyenMon']
        db_session.flush()
        db_session.commit()
        return redirect(url_for('giao_vien', message='Cập nhật thành công'))

    form.Th_Gioi_tinh.default = giao_vien['GioiTinh']
    form.process()
    return render_template('giao_vien/gv_edit_profile.html' ,giao_vien = giao_vien, form=form, error=error)

@app.route('/cham-diem/<string:id_hoc_sinh>/<string:id_bd>', methods=['GET','POST'])
def cham_diem(id_hoc_sinh, id_bd):
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    error = ''
    giaovien = session['giaovien']
    giao_vien = Profile_Giao_Vien(giaovien)
    bang_diem = doc_bang_diem_theo_id_bang_diem(id_bd)
    hoc_sinh = Profile_hoc_sinh(id_hoc_sinh)
    print(bang_diem)
    return render_template('giao_vien/gv_cham_diem.html', bang_diem=bang_diem, ten_hs = hoc_sinh['HoVaTen'],id_hoc_sinh=id_hoc_sinh,id_bd=id_bd)

@app.route('/cap-nhat-diem/<string:id_hoc_sinh>/<string:id_bd>', methods=['GET','POST'])
def cap_nhat_diem(id_hoc_sinh, id_bd):
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    error = ''
    giaovien = session['giaovien']
    giao_vien = Profile_Giao_Vien(giaovien)
    print(request.form.get('name'))
    print(request.form.get('value'))
    cap_nhat_bang_diem(id_bd, request.form.get('name'),request.form.get('value'))
    return redirect(url_for('cham_diem', id_hoc_sinh=id_hoc_sinh, id_bd=id_bd))


@app.route('/doi-mat-khau', methods=['GET','POST'])
def Doi_mat_khau():
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    giaovien = session['giaovien']
    giao_vien = Profile_Giao_Vien(giaovien)
    ThongBao = ""
    form = Form_Reset_pw()

    if form.validate_on_submit():
        MatkhauCu = request.form['Th_MatkhauCu']
        MatkhauMoi = request.form['Th_MatkhauMoi']
        print(MatkhauMoi)
        ThongBao = gv_doi_mat_khau(giaovien,MatkhauCu,MatkhauMoi)
        if ThongBao == "Đổi Mật Khẩu Thành Công":
            return redirect('/giao-vien')
    return render_template('giao_vien/gv_doi_mat_khau.html' , form=form,ThongBao=ThongBao)


@app.route('/dang-xuat', methods=['GET','POST'])
def dang_xuat():
    if session.get("giaovien") != None:
        session.pop("giaovien", None)
    return redirect('/')

@app.route('/thoi-khoa-bieu', methods=['GET','POST'])
def thoi_khoa_bieu():
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    giaovien = session['giaovien']
    
    TKB = db_session.query(ThoiKhoaBieu).first()
    t = tao_thoi_khoa_bieu(TKB)
    return render_template('thoi_khoa_bieu/thoi-khoa-bieu.html' ,TKB = t )
    