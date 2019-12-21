from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app


@app.route('/quan-ly', methods=['GET','POST'])
def quan_ly():
    return render_template('quan_ly/ql_dashboard.html')
