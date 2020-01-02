from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app

@app.route('/danh-sach-lop', methods=['GET','POST'])
def danh_sach_lop():
    return render_template('lop_hoc/l_danh_sach_lop.html')

    
@app.route('/chi-tiet-lop/<string:lop>', methods=['GET','POST'])
def danh_sach_hoc_sinh(lop):
    return render_template('lop_hoc/l_chi_tiet_lop.html')

    
@app.route('/bang-diem-lop/<string:lop>', methods=['GET', 'POST'])
def bang_diem_lop(lop):
    return render_template('lop_hoc/l_bang_diem_lop.html')


@app.route('/them-lop-hoc', methods=['GET','POST'])
def them_lop_hoc():
    
    return render_template('lop_hoc/l_them_lop.html')