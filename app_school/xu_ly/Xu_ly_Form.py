from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, PasswordField, StringField, BooleanField
from wtforms.widgets import PasswordInput
from wtforms import validators, ValidationError

from app_school.xu_ly.Xu_ly_Model import *


class Form_Register(FlaskForm):
    Th_Email = TextField("Email", [validators.Required("Vui lòng nhập vào Email"), validators.Email(
        "Vui lòng nhập vào Email"), validators.Length(min=4, max=30)])
    Th_Taikhoan = TextField("Tên tài khoản đăng nhập", [validators.Required(
        "Vui lòng nhập vào tên đăng nhập"), validators.Length(min=4, max=20)])
    Th_Matkhau = PasswordField("Mật khẩu", [validators.InputRequired(), validators.Length(
        min=4, max=20), validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu đăng nhập phải trùng nhau')])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")


class Form_Login(FlaskForm):
    Th_Vaitro = SelectField("Vai trò", choices=[('gv','Giáo Viên'),('hs','Học Sinh')])
    Th_Taikhoan = TextField("Tên tài khoản đăng nhập", [validators.Required(
        "Vui lòng nhập vào tên đăng nhập"), validators.Length(min=4, max=20)])
    Th_Matkhau = PasswordField(
        "Mật khẩu", [validators.InputRequired(), validators.Length(min=4, max=20)])


class recover_pw(FlaskForm):
    Th_Email = TextField("Email", [validators.Required("Vui lòng nhập vào Email"), validators.Email(
        "Vui lòng nhập vào Email"), validators.Length(min=4, max=30)])


class Form_Feedback(FlaskForm):
    Th_Ho_ten = TextField("Họ và tên", [validators.Required(
        "Vui lòng nhập họ tên."), validators.Length(min=4, max=30)])
    Th_Email = TextField("Email", [validators.Required("Vui lòng nhập vào Email"), validators.Email(
        "Vui lòng nhập vào Email"), validators.Length(min=4, max=30)])
    Th_Feedback = TextAreaField("Feedback", [validators.Required()])


class Form_Update_Gv(FlaskForm):
    Th_Ho_ten = TextField("Họ và tên", [validators.Required(
        "Vui lòng nhập họ tên."), validators.Length(min=4, max=30)])
    Th_Gioi_tinh = SelectField("Giới tính", choices=[
                              ("Nam", "Nam"), ("Nữ", "Nữ"), ("Khác", "Khác")])
    Th_Ngay_sinh = TextField("Ngày sinh", [validators.Required(
        "Vui lòng nhập ngày sinh.")])
    Th_Dia_chi = TextField("Địa chỉ", [validators.Required(
        "Vui lòng nhập vào địa chỉ"), validators.Length(min=4, max=75)])
    Th_Email = TextField("Email", [validators.Required("Vui lòng nhập vào Email"), validators.Email(
        "Vui lòng nhập vào Email"), validators.Length(min=4, max=30)])
    Th_Sdt = TextField("Số điện thoại", [validators.Required(
        "Vui lòng nhập vào số điện thoại"), validators.Length(min=4, max=15)])
    Th_Trinh_do = TextField(
        "Trình độ", [validators.Required("Vui lòng nhập vào trình độ")])
    Th_Chuyen_mon = TextField("Chuyên môn")


class Form_Update_Hs(FlaskForm):
    Th_Ho_ten = TextField("Họ và tên", [validators.Required(
        "Vui lòng nhập họ tên."), validators.Length(min=4, max=30)])
    Th_Gioi_tinh = SelectField("Giới tính", choices=[
                              ("Nam", "Nam"), ("Nữ", "Nữ"), ("Khác", "Khác")])
    Th_Ngay_sinh = TextField("Ngày sinh", [validators.Required(
        "Vui lòng nhập ngày sinh.")])
    Th_Sdt = TextField("Số điện thoại", [validators.Required(
        "Vui lòng nhập vTh_Dia_chiào số điện thoại"), validators.Length(min=4, max=15)])
    Th_Sdt_PH = TextField("Số điện thoại phụ huynh", [validators.Required(
        "Vui lòng nhập vào số điện thoại phụ huynh"), validators.Length(min=4, max=15)])
    Th_Email = TextField("Email", [validators.Required("Vui lòng nhập vào Email"), validators.Email(
        "Vui lòng nhập vào Email"), validators.Length(min=4, max=30)])
    Th_Dia_chi = TextField("Địa chỉ", [validators.Required(
        "Vui lòng nhập vào địa chỉ"), validators.Length(min=4, max=75)])


class Form_Update_Manager(FlaskForm):
    Th_Ho_ten = TextField("Họ và tên", [validators.Required(
        "Vui lòng nhập họ tên."), validators.Length(min=4, max=30)])
    Th_Gioi_tinh = SelectField("Giới tính", choices=[
                              ("M", "Nam"), ("F", "Nữ"), ("D", "Khác")])
    Th_Dia_chi = TextAreaField("Địa chỉ")
    Th_Email = TextField("Email", [validators.Required("Vui lòng nhập vào Email"), validators.Email(
        "Vui lòng nhập vào Email"), validators.Length(min=4, max=30)])
    Th_Tuoi = TextField("Tuổi", [validators.Required(
        "Vui lòng nhập vào tuổi"), validators.Length(min=1, max=3)])
    Th_Sdt = TextField("Số điện thoại", [validators.Required(
        "Vui lòng nhập vào số điện thoại"), validators.Length(min=4, max=15)])
    Th_Matkhau = PasswordField("Mật khẩu", [validators.InputRequired(), validators.Length(
        min=4, max=20), validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu đăng nhập phải trùng nhau')])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")


class Form_Create_Class(FlaskForm):
    Th_Lop = TextField("Tên Lớp", [validators.Required(
        "Vui lòng nhập tên lớp."), validators.Length(min=2, max=30)])
    Th_Dia_diem = TextField("Địa điểm", [validators.Required(
        "Vui lòng nhập địa điểm."), validators.Length(min=5, max=75)])
    Th_Khoi = SelectField("Khối", coerce=int)
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)
    Th_GV_Chu_nhiem = SelectField("GV Chủ nhiệm", coerce=int)


class Form_Them_Nien_khoa(FlaskForm):
    Th_Nien_khoa = SelectField("Niên Khóa")

class Form_Chon_TKB(FlaskForm):
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)
    TH_Lop = SelectField("Lớp", coerce=int)

class Form_Cap_nhat_TKB(FlaskForm):
    Th_Nien_khoa = TextField("Niên Khóa")
    Th_Lop = TextField("Lớp")
    Th_Thu = TextField("Thứ")
    Th_Buoi = TextField("Buổi")
    Th_Tiet = TextField("Tiết")
    Th_Giao_vien = SelectField("Giáo viên", coerce=int)
    Th_Mon = SelectField("Môn", coerce=int)

class Form_Reset_pw(FlaskForm):
    Th_MatkhauCu = PasswordField("Mật khẩu cũ: ", [validators.InputRequired(), validators.Length(min=4, max=20)])
    Th_MatkhauMoi = PasswordField("Mật khẩu mới: ", [validators.InputRequired(), validators.Length(min=4, max=20)])

class Form_Lich_Thi(FlaskForm):
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)
    Th_Khoi = SelectField("Khối", coerce=int)

class Form_Them_Lich_Thi(FlaskForm):
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)
    Th_Khoi = SelectField("Khối", coerce=int)
    Th_Mon = SelectField("Môn", coerce=int)
    Th_NgayThi = TextField("Ngày thi", [validators.Required(
        "Vui lòng nhập ngày thi.")])
    Th_ThoiGian = TextField("Thời Gian" ,[validators.InputRequired()])

class Form_Sua_Lich_Thi(FlaskForm):
    Th_NgayThi = TextField("Ngày thi", [validators.Required(
        "Vui lòng nhập ngày thi.")])
    Th_ThoiGian = TextField("Thời Gian" ,[validators.InputRequired()])

'''class Form_UpdateProfile(FlaskForm) :
    Th_Id = IntegerField("Mã số ID" , [validators.Required("Vui lòng nhập vào mã số ID") ,validators.Length(min=4, max=15)])
    Th_Taikhoan = TextField("Tên tài khoản đăng nhập" , [validators.Required("Vui lòng nhập vào tên đăng nhập"),validators.Length(min=4, max=20)])
    Th_Matkhau = PasswordField("Mật khẩu" , [validators.InputRequired() ,validators.Length(min=4, max=20), validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu đăng nhập phải trùng nhau')])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")
    Th_quyen = RadioField("Chức vụ" , choices=[ ("T", "Giáo viên") , ("H" , "Học sinh") , ("Q" , "Quản lý") ])
    Th_Ho_ten = TextField("Họ và tên" ,[validators.Required("Vui lòng nhập họ tên.") ,validators.Length(min=4, max=30)])
    Th_Lop = IntegerField("Lớp" , [validators.Required("Vui lòng nhập vào lớp") , validators.Length(min=1,max=2)])
    Th_Gioi_tinh = RadioField("Giới tính" , choices=[ ("M" , "Nam") , ("F" , "Nữ") , ("D" , "Khác") ])
    Th_Dia_chi = TextAreaField("Địa chỉ")
    Th_Sdt = IntegerField("Số điện thoại" , [validators.Required("Vui lòng nhập vào số điện thoại") ,validators.Length(min=4, max=15)])
    Th_Email = TextField("Email" , [validators.Required("Vui lòng nhập vào Email") , validators.Email("Vui lòng nhập vào Email") ,validators.Length(min=4, max=30)])
    Th_Confirm = BooleanField('Đồng ý cập nhật thông tin', [validators.InputRequired()])
    Th_Submit = SubmitField("Cập nhật")'''
