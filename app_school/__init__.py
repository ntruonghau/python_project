from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__, static_folder="", template_folder="")
app = Flask(__name__)
app.config['SECRET_KEY'] = '2019'
app.config['DATABASE_FILE'] = 'du_lieu/qlTruongHoc.db?check_same_thread=False'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True

import app_school.app_gateway
import app_school.app_giao_vien
import app_school.app_hoc_sinh
import app_school.app_quan_ly
