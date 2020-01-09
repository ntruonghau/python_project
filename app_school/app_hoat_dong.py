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
        thamgia = Tham_Gia_Hoat_Dong(IDHoatDong = id_hoat_dong  ,IDHocSinh = hocsinh , NgayDangKy = ngay_dang_ky)
        hd.SoNguoiDaThamGia += 1
        db_session.add(thamgia)
        db_session.flush()
        db_session.commit()
        return redirect('/hoc-sinh/hoat-dong')

@app.route('/hoc-sinh/hoat-dong-da-tham-gia', methods=['GET', 'POST'])
def hoat_dong_da_tham_gia_hs():
    if session.get("hocsinh") == None:
        return redirect(url_for('index'))
    hocsinh = session['hocsinh'] 

    ds_hd = hoat_dong_da_tham_gia(hocsinh)
    return render_template('hoat_dong/hoat_dong_da_tham_gia.html',hoat_dong = ds_hd)