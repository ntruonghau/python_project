from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app


@app.route('/hoc-sinh', methods=['GET','POST'])
def hoc_sinh():
    return render_template('hoc_sinh/hs_dashboard.html')
