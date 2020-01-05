from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import GiaoVien
from app_school.xu_ly.Xu_ly_Form import Form_Register, Form_Login
from app_school.xu_ly.tra_cuu.tra_cuu import *


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

    return render_template('index/lien_he.html')

@app.route('/trang-chu/tra-cuu', methods=['GET','POST'])
def trang_tra_cuu():
    Dia_chi_MH = "/trang-chu/tra-cuu"
    if request.method == 'POST':
        Ma_so = request.form.get('Th_Ma_so')
        if Ma_so == "TRA_CUU":
            Chuoi_Tra_cuu = request.form.get('Th_Chuoi_Tra_cuu')
            Dia_chi_MH = "/trang-chu/tra-cuu/" + Chuoi_Tra_cuu + "/"


    return render_template('trang_chu/tra-cuu-hoc-sinh.html')

@app.route('/trang-chu/tra-cuu/<string:Chuoi_Tra_cuu>/', methods=['GET','POST'])
def trang_tra_cuu_theo_id(Chuoi_Tra_cuu):
    print("Chuoi tra cuu la :" , Chuoi_Tra_cuu)
    Danh_sach_hs = Doc_danh_sach_hs()
    print("Successsssssssssssssssss")
    print(Danh_sach_hs) 
    Danh_sach_hs_chon = Danh_sach_hs
    Danh_sach_hs_chon = Lay_info_theo_ID( Chuoi_Tra_cuu , Danh_sach_hs )
    print("Success")
    print(Danh_sach_hs_chon)
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
    return render_template('trang_chu/tra-cuu-hoc-sinh.html' , Chuoi_Tra_cuu=Chuoi_Tra_cuu , Danh_sach_hs_chon=Danh_sach_hs_chon , Id = Id,
        HoVaTen=HoVaTen , GioiTinh=GioiTinh , DiaChi=DiaChi , Email=Email , NgaySinh=NgaySinh , SoDienThoai=SoDienThoai , 
        SoDienThoaiPhuHuynh=SoDienThoaiPhuHuynh , IDLop=IDLop , NienKhoa=NienKhoa)



# @app.route('/tra-cuu/<string:Chuoi_tra_cuu>/', methods=['GET','POST'])
# def trang_tra_cuu(Chuoi_tra_cuu):
#     id = ""
#     if request.form.get(Chuoi_tra_cuu) :
#         id = Chuoi_tra_cuu
#         danh_sach_hs = Doc_danh_sach_hs()
#         thong_tin_hs = Lay_info_theo_ID( id , danh_sach_hs )

#     return render_template('trang_chu/tra-cuu-hoc-sinh.html' , thong_tin_hs = thong_tin_hs )

