from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import GiaoVien
from app_school.xu_ly.Xu_ly_Form import Form_Register, Form_Login

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error_page/pages-404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error_page/pages-500.html'), 404

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('trang_chu/index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = Form_Login()
    Th_Taikhoan = ''
    Th_Matkhau = ''
    error = ''
    if form.validate_on_submit():
        Th_Taikhoan = request.form['Th_Taikhoan']
        Th_Matkhau = request.form['Th_Matkhau']
        try:
            giaovien = db_session.query(GiaoVien).filter(GiaoVien.TenDangNhap == Th_Taikhoan).one()
            if giaovien.MatKhau == Th_Matkhau:
                session['giaovien'] = Th_Taikhoan
                return redirect(url_for('giao_vien'))
            else:
                error = 'Tài khoản hoặc mật khẩu không đúng'
        except Exception as e:
            print(str(e))
            pass
    return render_template("account/login.html", form=form, error=error)

@app.route('/register', methods=['GET','POST'])
def register():
    form = Form_Register()
    Th_Email = ''
    Th_Taikhoan = ''
    Th_Matkhau = ''
    error = ''
    if form.validate_on_submit():
        Th_Email = request.form['Th_Email']
        Th_Taikhoan = request.form['Th_Taikhoan']
        Th_Matkhau = request.form['Th_Matkhau']
        giaovien = GiaoVien(TenDangNhap=Th_Taikhoan, MatKhau=Th_Matkhau, Email=Th_Email)
        try:
            db_session.add(giaovien)
            db_session.commit()
            session['giaovien'] = Th_Taikhoan
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