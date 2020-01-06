from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import GiaoVien
from app_school.xu_ly.Xu_ly_Form import Form_Register, Form_Login
from app_school.xu_ly.tra_cuu.tra_cuu import *
from app_school.xu_ly.lien_he.xu_ly_lien_he import *


@app.route('/trang-chu/thong-tin', methods=['GET','POST'])
def trang_thong_tin():
    return render_template('index/thong_tin.html')
    
@app.route('/trang-chu/dich-vu', methods=['GET','POST'])
def trang_dich_vu():

    return render_template('index/dich_vu.html')

@app.route('/trang-chu/thu-vien', methods=['GET','POST'])
def trang_thu_vien():

    return render_template('index/thu_vien.html')

@app.route('/trang-chu/doi-ngu', methods=['GET','POST'])
def trang_doi_ngu():

    return render_template('index/doi_ngu.html')

@app.route('/trang-chu/doi-ngu/truong-hau', methods=['GET','POST'])
def trang_doi_ngu_1():

    return render_template('index/doi_ngu_truong_hau.html')

@app.route('/trang-chu/doi-ngu/tuan-anh', methods=['GET','POST'])
def trang_doi_ngu_2():
    return render_template('index/doi_ngu_tuan_anh.html')

@app.route('/trang-chu/doi-ngu/thanh-hoa', methods=['GET','POST'])
def trang_doi_ngu_3():

    return render_template('index/doi_ngu_thanh_hoa.html')

@app.route('/trang-chu/lien-he', methods=['GET','POST'])
def trang_lien_he():
    Ho_va_ten = ""
    Email = ""
    Noi_dung = ""
    if request.form.get("Th_Ho_va_ten") :
        Ho_va_ten = request.form.get("Th_Ho_va_ten")
        Email = request.form.get("Th_email")
        Noi_dung = request.form.get("Th_noi_dung")
        danh_sach_contact = {"Ho_va_ten" : Ho_va_ten , "Email" : Email , "Noi_dung" : Noi_dung }
        ghi_info_contact(danh_sach_contact)
    return render_template('index/lien_he.html')

@app.route('/trang-chu/tra-cuu', methods=['GET','POST'])
def trang_tra_cuu():
    Chuoi_Tra_cuu = ""
    dia_chi_mh = "/trang-chu/tra-cuu/0"
    Danh_sach_hs = Doc_danh_sach_hs_id()
    dem = len(Danh_sach_hs)
    if request.form.get("Th_Chuoi_Tra_cuu") :
        Chuoi_Tra_cuu = request.form.get("Th_Chuoi_Tra_cuu")
        dia_chi_mh = "/trang-chu/tra-cuu/" + Chuoi_Tra_cuu
        if int(Chuoi_Tra_cuu) > int(dem) :
            dia_chi_mh = "/trang-chu/tra-cuu/0"
    return render_template('trang_chu/tra-cuu-hoc-sinh.html' , dia_chi_mh=dia_chi_mh)

@app.route('/trang-chu/tra-cuu/<string:Chuoi_Tra_cuu>/', methods=['GET','POST'])
def trang_tra_cuu_theo_id(Chuoi_Tra_cuu):
    Danh_sach_hs = Doc_danh_sach_hs()
    Danh_sach_hs_chon = Danh_sach_hs
    Danh_sach_hs_chon = Lay_info_theo_ID( Chuoi_Tra_cuu , Danh_sach_hs )
    Id = Danh_sach_hs_chon['IDHocSinh']
    HoVaTen = Danh_sach_hs_chon['HoVaTen']
    GioiTinh = Danh_sach_hs_chon['GioiTinh']
    DiaChi = Danh_sach_hs_chon['DiaChi']
    Email = Danh_sach_hs_chon['Email']
    NgaySinh = Danh_sach_hs_chon['NgaySinh']
    SoDienThoai = Danh_sach_hs_chon['SoDienThoai']
    SoDienThoaiPhuHuynh = Danh_sach_hs_chon['SoDienThoaiPhuHuynh']
    IDLop = Danh_sach_hs_chon['IDLop']
    NienKhoa = Danh_sach_hs_chon['NienKhoa']

    dia_chi_mh = "/trang-chu/tra-cuu/" + Chuoi_Tra_cuu
    return render_template('index/tra_cuu_chon.html' , Chuoi_Tra_cuu=Chuoi_Tra_cuu , Danh_sach_hs_chon=Danh_sach_hs_chon , Id = Id,
        HoVaTen=HoVaTen , GioiTinh=GioiTinh , DiaChi=DiaChi , Email=Email , NgaySinh=NgaySinh , SoDienThoai=SoDienThoai , 
        SoDienThoaiPhuHuynh=SoDienThoaiPhuHuynh , IDLop=IDLop , NienKhoa=NienKhoa , dia_chi_mh=dia_chi_mh)



