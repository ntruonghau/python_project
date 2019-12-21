from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app


@app.route('/', methods=['GET','POST'])
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template("account/login.html")

@app.route('/register', methods=['GET','POST'])
def register():
    return render_template("account/register.html")

@app.route('/lockscreen', methods=['GET','POST'])
def lockscreen():
    return render_template("account/lockscreen.html")

@app.route('/recoverpw', methods=['GET','POST'])
def recoverpw():
    return render_template("account/recoverpw.html")