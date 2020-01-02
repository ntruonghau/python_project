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


@app.route('/thong-tin-diem-so/<string:hoc_sinh>', methods=['GET','POST'])
def thong_tin_diem_so(hoc_sinh):
    return render_template('giao_vien/gv_bang_diem_hoc_sinh.html')
