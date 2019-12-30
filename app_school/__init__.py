from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__, static_folder="", template_folder="")
app = Flask(__name__)
app.config['SECRET_KEY'] = '2019'
db = SQLAlchemy(app)

app.config['DATABASE_FILE'] = 'du_lieu/qlTruongHoc.db?check_same_thread=False'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True


from app_school.xu_ly.Xu_ly_Model import Base, db_session
import app_school.app_gateway
import app_school.app_giao_vien
import app_school.app_hoc_sinh
import app_school.app_quan_ly