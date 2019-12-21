from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app


@app.route('/giao-vien', methods=['GET','POST'])
def giao_vien():
    return render_template('giao_vien/gv_dashboard.html')
