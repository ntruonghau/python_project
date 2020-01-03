from flask import Markup, request, render_template, url_for, session, redirect
from app_school.xu_ly.giao_vien.XL_Giao_vien import *
from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import GiaoVien
from app_school.xu_ly.Xu_ly_Form import Form_Update_Gv


@app.route('/giao-vien', methods=['GET','POST'])
def giao_vien():
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    giaovien = session['giaovien']

    giao_vien = Profile_Giao_Vien(giaovien)
    print(giao_vien)

    return render_template('giao_vien/gv_dashboard.html',giao_vien = giao_vien)

@app.route('/sua-profile', methods=['GEt','POST'])
def edit_giao_vien():
    if session.get("giaovien") == None:
        return redirect(url_for('index'))

    giaovien = session['giaovien']
    giao_vien = Profile_Giao_Vien(giaovien)

    form = Form_Update_Gv()
    if request.method == 'POST':
        HoVaTen = request.form.get('Th_HoVaTen')
        GioiTinh = request.form.get('Th_gioiTinh')
        NgaySinh = request.form.get('Th_NgaySinh')
        DiaChi = request.form.get('Th_DiaChi')
        Email = request.form.get('Th_Email')
        SoDienThoai = request.form.get('Th_SoDienThoai')
        TrinhDo = request.form.get('Th_TrinhDo')
        ChuyenMon = request.form.get('Th_ChuyenMon')

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

        print(gv)
    return render_template('giao_vien/gv_edit_profile.html' ,giao_vien = giao_vien )
