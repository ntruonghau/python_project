from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField, PasswordField, StringField , BooleanField
from wtforms.widgets import PasswordInput
from wtforms import validators, ValidationError 

from app_school.xu_ly.Xu_ly_Model import *

class Form_Register(FlaskForm) :
    Th_Email = TextField("Email" , [validators.Required("Vui lòng nhập vào Email") , validators.Email("Vui lòng nhập vào Email") ,validators.Length(min=4, max=30)])
    Th_Taikhoan = TextField("Tên tài khoản đăng nhập" , [validators.Required("Vui lòng nhập vào tên đăng nhập"),validators.Length(min=4, max=20)])
    Th_Matkhau = PasswordField("Mật khẩu" , [validators.InputRequired() ,validators.Length(min=4, max=20), validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu đăng nhập phải trùng nhau')])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")
    Th_Confirm = BooleanField('Đồng ý tạo tài khoản !', [validators.InputRequired()])
    Th_Submit = SubmitField("Đăng kí")

class recover_pw(FlaskForm) :
    Th_Email = TextField("Email" , [validators.Required("Vui lòng nhập vào Email") , validators.Email("Vui lòng nhập vào Email") ,validators.Length(min=4, max=30)])
    Th_Confirm = BooleanField('Đồng ý chọn Email', [validators.InputRequired()])
    Th_Submit = SubmitField("Gửi")

class Form_Feedback(FlaskForm) :
    Th_Ho_ten = TextField("Họ và tên" ,[validators.Required("Vui lòng nhập họ tên.") ,validators.Length(min=4, max=30)])
    Th_Email = TextField("Email" , [validators.Required("Vui lòng nhập vào Email") , validators.Email("Vui lòng nhập vào Email") ,validators.Length(min=4, max=30)])
    Th_Feedback = TextAreaField("Feedback" , [validators.Required()])

class Form_Update_Gv(FlaskForm) :
    Th_Id = IntegerField("Mã số ID" , [validators.Required("Vui lòng nhập vào mã số ID") ,validators.Length(min=4, max=15)])
    Th_Ho_ten = TextField("Họ và tên" ,[validators.Required("Vui lòng nhập họ tên.") ,validators.Length(min=4, max=30)])
    Th_Gioi_tinh = RadioField("Giới tính" , choices=[ ("M" , "Nam") , ("F" , "Nữ") , ("D" , "Khác") ])
    Th_Dia_chi = TextAreaField("Địa chỉ")
    Th_Email = TextField("Email" , [validators.Required("Vui lòng nhập vào Email") , validators.Email("Vui lòng nhập vào Email") ,validators.Length(min=4, max=30)])
    Th_Tuoi = IntegerField("Tuổi" , [validators.Required("Vui lòng nhập vào tuổi") , validators.Length(min=1 , max =3)])
    Th_Sdt = IntegerField("Số điện thoại" , [validators.Required("Vui lòng nhập vào số điện thoại") ,validators.Length(min=4, max=15)])
    Th_Trinh_do = TextField("Trình độ" , [validators.Required("Vui lòng nhập vào trình độ")])
    Th_Chuyen_mon = TextField("Chuyên môn")
    Th_Matkhau = PasswordField("Mật khẩu" , [validators.InputRequired() ,validators.Length(min=4, max=20), validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu đăng nhập phải trùng nhau')])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")
    Th_Confirm = BooleanField('Đồng ý cập nhật thông tin', [validators.InputRequired()])
    Th_Submit = SubmitField("Cập nhật")

class Form_Update_Hs(FlaskForm) :
    Th_Id = IntegerField("Mã số ID" , [validators.Required("Vui lòng nhập vào mã số ID") ,validators.Length(min=4, max=15)])
    Th_Ho_ten = TextField("Họ và tên" ,[validators.Required("Vui lòng nhập họ tên.") ,validators.Length(min=4, max=30)])
    Th_Lop = IntegerField("Lớp" , [validators.Required("Vui lòng nhập vào lớp")])
    Th_Gioi_tinh = RadioField("Giới tính" , choices=[ ("M" , "Nam") , ("F" , "Nữ") , ("D" , "Khác") ])
    Th_Sdt = IntegerField("Số điện thoại" , [validators.Required("Vui lòng nhập vào số điện thoại") ,validators.Length(min=4, max=15)])
    Th_Sdt_PH = IntegerField("Số điện thoại phụ huynh" , [validators.Required("Vui lòng nhập vào số điện thoại phụ huynh") ,validators.Length(min=4, max=15)])
    Th_Tuoi = IntegerField("Tuổi" , [validators.Required("Vui lòng nhập vào tuổi") , validators.Length(min=1 , max =3)])
    Th_Email = TextField("Email" , [validators.Required("Vui lòng nhập vào Email") , validators.Email("Vui lòng nhập vào Email") ,validators.Length(min=4, max=30)])
    Th_Dia_chi = TextAreaField("Địa chỉ")
    Th_Matkhau = PasswordField("Mật khẩu" , [validators.InputRequired() ,validators.Length(min=4, max=20), validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu đăng nhập phải trùng nhau')])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")
    Th_Confirm = BooleanField('Đồng ý cập nhật thông tin', [validators.InputRequired()])
    Th_Submit = SubmitField("Cập nhật")

class Form_Update_Manager(FlaskForm) :
    Th_Id = IntegerField("Mã số ID" , [validators.Required("Vui lòng nhập vào mã số ID") ,validators.Length(min=4, max=15)])
    Th_Ho_ten = TextField("Họ và tên" ,[validators.Required("Vui lòng nhập họ tên.") ,validators.Length(min=4, max=30)])
    Th_Gioi_tinh = RadioField("Giới tính" , choices=[ ("M" , "Nam") , ("F" , "Nữ") , ("D" , "Khác") ])
    Th_Dia_chi = TextAreaField("Địa chỉ")
    Th_Email = TextField("Email" , [validators.Required("Vui lòng nhập vào Email") , validators.Email("Vui lòng nhập vào Email") ,validators.Length(min=4, max=30)])
    Th_Tuoi = IntegerField("Tuổi" , [validators.Required("Vui lòng nhập vào tuổi") , validators.Length(min=1 , max =3)])
    Th_Sdt = IntegerField("Số điện thoại" , [validators.Required("Vui lòng nhập vào số điện thoại") ,validators.Length(min=4, max=15)])
    Th_Matkhau = PasswordField("Mật khẩu" , [validators.InputRequired() ,validators.Length(min=4, max=20), validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu đăng nhập phải trùng nhau')])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")
    Th_Confirm = BooleanField('Đồng ý cập nhật thông tin', [validators.InputRequired()])
    Th_Submit = SubmitField("Cập nhật")   



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