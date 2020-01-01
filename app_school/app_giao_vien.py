from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app


@app.route('/giao-vien', methods=['GET','POST'])
def giao_vien():
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    giaovien = session['giaovien']
    return render_template('giao_vien/gv_dashboard.html')

@app.route('/sua-profile', methods=['GEt','POST'])
def edit_giao_vien():
    if session.get("giaovien") == None:
        return redirect(url_for('index'))
    return render_template('giao_vien/gv_edit_profile.html')

@app.route('/danh-sach-lop', methods=['GET','POST'])
def danh_sach_lop():
    return render_template('giao_vien/gv_danh_sach_lop.html')

@app.route('/danh-sach-hoc-sinh/<string:lop>', methods=['GET','POST'])
def danh_sach_hoc_sinh(lop):
    return render_template('giao_vien/gv_danh_sach_hoc_sinh.html')

@app.route('/bang-diem-lop/<string:lop>', methods=['GET', 'POST'])
def bang_diem_lop(lop):
    return render_template('giao_vien/gv_bang_diem_lop.html')

@app.route('/thong-tin-diem-so/<string:hoc_sinh>', methods=['GET','POST'])
def thong_tin_diem_so(hoc_sinh):
    return render_template('giao_vien/gv_bang_diem_hoc_sinh.html')