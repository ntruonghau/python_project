from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import GiaoVien
from app_school.xu_ly.Xu_ly_Form import Form_Register


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('trang_chu/index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template("account/login.html")

@app.route('/register', methods=['GET','POST'])
def register():
    form = Form_Register()
    Th_Email = ''
    Th_Taikhoan = ''
    Th_Matkhau = ''
    error = ''
    print('ab')
    if form.validate_on_submit():
        Th_Email = request.form['Th_Email']
        Th_Taikhoan = request.form['Th_Taikhoan']
        Th_Matkhau = request.form['Th_Matkhau']
        print('ab')
        giaovien = GiaoVien(TenDangNhap=Th_Taikhoan, MatKhau=Th_Matkhau, Email=Th_Email)
        print(giaovien.__dict__)
        try:
            print('success')
            db_session.add(giaovien)
            print('success')
            db_session.commit()
            print('success')
            session['giaovien'] = Th_Taikhoan
            print('success')
            return redirect(url_for('giao_vien'))
        except Exception as e:
            db_session.rollback()
            error = 'Tài khoản đã tồn tại'
            pass
    return render_template("account/register.html", form=form, error=error)

@app.route('/lockscreen', methods=['GET','POST'])
def lockscreen():
    return render_template("account/lockscreen.html")

@app.route('/recoverpw', methods=['GET','POST'])
def recoverpw():
    return render_template("account/recoverpw.html")