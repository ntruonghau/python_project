from flask import Markup, request, render_template, url_for, session, redirect
from app_school.xu_ly.Xu_ly_Form import *
from app_school.xu_ly.Xu_ly_Model import *
from app_school.xu_ly.hoc_sinh.XL_Hoc_sinh import * 
from app_school.xu_ly.hoat_dong.XL_Hoat_dong import *
from app_school.xu_ly.nien_khoa.XL_Nien_khoa import *

from app_school import app, db_session

@app.route('/hoc-sinh/hoat-dong', methods=['GET', 'POST'])
def hoat_dong_hs():
    if session.get("hocsinh") == None:
        return redirect(url_for('index'))
    hocsinh = session['hocsinh']    

    hs = db_session.query(HocSinh).filter(HocSinh.IDHocSinh == hocsinh).one()
    hdong = load_danh_sach_hoat_dong(hs.IDNienKhoa,hs)
    if request.args.get('message'):
        message = request.args.get('message')
        print(message)
        
    return render_template('hoat_dong/hs_xem_hoat_dong.html',hoat_dong = hdong)

@app.route('/hoc-sinh/hoat-dong/tham-gia/<string:id_hoat_dong>', methods=['GET', 'POST'])
def tham_gia_hoat_dong_hs(id_hoat_dong):
    if session.get("hocsinh") == None:
        return redirect(url_for('index'))
    hocsinh = session['hocsinh']   
    ngay_dang_ky = datetime.now()
    
    hd = db_session.query(Hoat_Dong).filter(Hoat_Dong.IDHoatDong == id_hoat_dong).first()
    HanDangKy = datetime.strptime( hd.ThoiHanDangKy, '%d-%m-%Y')
    if ngay_dang_ky > HanDangKy:
        return redirect(url_for('hoat_dong_hs', message='Đã Quá Hạn Đăng Ký'))
    else: 
        ngay_dang_ky = datetime.now().date()
        ngay_dang_ky = ngay_dang_ky.strftime("%d-%m-%Y")
        thamgia = Tham_Gia_Hoat_Dong(IDHoatDong = id_hoat_dong  ,IDHocSinh = hocsinh , NgayDangKy = ngay_dang_ky)
        hd.SoNguoiDaThamGia += 1
        db_session.add(thamgia)
        db_session.flush()
        db_session.commit()
        return redirect('/hoc-sinh/hoat-dong')

@app.route('/hoc-sinh/hoat-dong/huy-tham-gia/<string:id_hoat_dong>', methods=['GET', 'POST'])
def huy_tham_gia_hoat_dong_hs(id_hoat_dong):
    if session.get("hocsinh") == None:
        return redirect(url_for('index'))
    hocsinh = session['hocsinh']   
    hd = db_session.query(Hoat_Dong).filter(Hoat_Dong.IDHoatDong == id_hoat_dong).first()
    hd.SoNguoiDaThamGia -= 1 
    db_session.delete(db_session.query(Tham_Gia_Hoat_Dong).filter(Tham_Gia_Hoat_Dong.IDHoatDong == id_hoat_dong, Tham_Gia_Hoat_Dong.IDHocSinh == hocsinh).one())
    db_session.flush()
    db_session.commit()
    return redirect('/hoc-sinh/hoat-dong')


@app.route('/hoc-sinh/hoat-dong-da-tham-gia', methods=['GET', 'POST'])
def hoat_dong_da_tham_gia_hs():
    if session.get("hocsinh") == None:
        return redirect(url_for('index'))
    hocsinh = session['hocsinh'] 

    ds_hd = hoat_dong_da_tham_gia(hocsinh)
    return render_template('hoat_dong/hs_hoat_dong_da_tham_gia.html',hoat_dong = ds_hd)

@app.route('/giao-vien/hoat-dong', methods=['GET', 'POST'])
def hoat_dong_gv():
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    giaovien = session['giaovien']
    ds_hd = []

    form = Form_Xem_Hoat_Dong()
    ds_nien_khoa = doc_danh_sach_nien_khoa_select()
    nien_khoa = ds_nien_khoa[0][0]
    form.Th_Nien_khoa.choices = ds_nien_khoa
    if form.validate_on_submit():
        nien_khoa = request.form['Th_Nien_khoa']
    ds_hd =  load_danh_sach_hoat_dong_gv(nien_khoa)
    return render_template('hoat_dong/gv_xem_hoat_dong.html', hoat_dong=ds_hd, form = form)

@app.route('/giao-vien/hoat-dong/danh-sach-nguoi-tham-gia/<string:id_hoat_dong>', methods=['GET', 'POST'])
def danh_sach_nguoi_tham_gia(id_hoat_dong):
    if session.get("giaovien") == None:
        return redirect(url_for('index'))   
    giaovien = session['giaovien']

    hdong = db_session.query(Tham_Gia_Hoat_Dong).filter(Tham_Gia_Hoat_Dong.IDHoatDong == id_hoat_dong).all()
    ds = []
    for i in hdong:
        hs = db_session.query(HocSinh).filter(HocSinh.IDHocSinh == i.IDHocSinh).first()
        t = {}
        t['HocSinh'] = hs.HoVaTen
        t['Lop'] = ten_lop(hs.IDLop)
        t['NgayDangKy'] = datetime.strptime(i.NgayDangKy, '%d-%m-%Y')
        ds.append(t)
    
    danhsach = ds
    So_nguoi = len(danhsach)
    

    return render_template('hoat_dong/gv_xem_danh_sach_nguoi_tham_gia.html',danhsach=danhsach,So_nguoi=So_nguoi)