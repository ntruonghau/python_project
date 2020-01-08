from flask import Markup, request, render_template, url_for, session, redirect
from app_school.xu_ly.Xu_ly_Form import *
from app_school.xu_ly.lop_hoc.XL_Lop_hoc import lay_nien_khoa_theo_lop, cap_nhat_si_so
from app_school.xu_ly.giao_vien.XL_Giao_vien import Profile_Giao_Vien
from app_school.xu_ly.bang_diem.XL_Bang_diem import tao_bang_diem_cho_hoc_sinh, doc_bang_diem_theo_hoc_sinh
from app_school.xu_ly.hoc_sinh.XL_Hoc_sinh import Profile_hoc_sinh
from app_school.xu_ly.Xu_ly_Model import HocSinh, Lop
from app_school.xu_ly.hoc_sinh.XL_Hoc_sinh import *
from app_school.xu_ly.quan_li.xu_ly_doc_lien_he import *
from app_school import app, db_session
from datetime import date
from flask_mail import Mail , Message

@app.route("/quan-li" , methods = ['GET','POST'])
def trang_quan_li() :
    return render_template('web_layout/quan-ly-master.html')


@app.route("/quan-li/doc-lien-he" , methods = ['GET','POST'])
def trang_doc_lien_he() :
    Danh_sach_lh = Doc_danh_sach_lh()
    print(Danh_sach_lh)

    form = Form_Feedback()
    # form.Th_Email.choices 


    return render_template("quan_ly/doc_lien_he.html" , Danh_sach_lh=Danh_sach_lh)

@app.route("/quan-li/doc-lien-he/<string:Chuoi_tra_cuu>/" , methods=['GET','POST'])
def trang_tra_loi_lien_he(Chuoi_tra_cuu) :
    danh_sach = Doc_danh_sach_lh()
    danh_sach_chon = Lay_info_theo_Email(Chuoi_tra_cuu , danh_sach)
    print("danh sách nè",danh_sach_chon)
    noi_dung = ""
    if request.form.get("Th_noi_dung") :
        noi_dung = request.form.get("Th_noi_dung")
        print("nội dung là :",noi_dung)

        app.config['MAIL_SERVER'] = "smtp.gmail.com"
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = 'thanhhoa6621@gmail.com'    #Muốn test thì thay email vào nhe
        app.config['MAIL_PASSWORD'] = 'password'                #Pass email
        app.config['MAIL_USE_TLS'] = False  
        app.config['MAIL_USE_SSL'] = True
        mail = Mail(app)

        msg = Message("Thông tin liên hệ", sender='thanhhoa6621@gmail.com', recipients=[Chuoi_tra_cuu])
        msg.body= "Kính chào " + danh_sach_chon['Người gửi'] + "\nChúng tôi đã nhận được liên hệ của bạn với nội dung " + danh_sach_chon['Nội dung'] + "\n Chúng tôi đã có những hồi đáp như sau : " + noi_dung
        mail.send(msg)

    return render_template("quan_ly/tra_loi_lien_he.html" ,danh_sach_chon=danh_sach_chon)