from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table,Column,ForeignKey,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#create memory database
DuongDan ='sqlite:///app_school/du_lieu/ql_truong_hoc.db?check_same_thread =False' 
engine = create_engine(DuongDan)
Base = declarative_base()

class Khoi(Base):
    __tablename__ = 'Khoi'
    IDKhoi = Column(String(20),nullable = False, primary_key = True)
    TenKhoi = Column(String(100), nullable = False , unique=True)
    def __str__(self):
        return self.TenKhoi

class Mon(Base):
    __tablename__ = 'Mon'
    IDMon = Column(String(20),nullable = False, primary_key = True)
    TenMon = Column(String(100), nullable = False, unique=True )
    def __str__(self):
        return self.TenMon

class NienKhoa(Base):
    __tablename__ = 'NienKhoa'
    ID = Column(String(20),nullable = False, primary_key = True)
    NamNienKhoa = Column(String(100), nullable = False , unique=True)
    def __str__(self):
        return self.NamNienKhoa

class GiaoVien(Base):
    __tablename__ = 'GiaoVien'
    IDGiaoVien = Column(String(20),nullable = False, primary_key = True)
    TenDangNhap = Column(String(100), nullable = False , unique=True)
    MatKhau = Column(String(100), nullable = False )
    HoVaTen = Column(String(100), nullable = False )
    GioiTinh = Column(String(10), nullable = False )
    DiaChi =  Column(String(100), nullable = False )
    Email = Column(String(100), nullable = False )
    NgaySinh = Column(String(30), nullable = False )
    SoDienThoai = Column(String(11), nullable = False )
    TrinhDo =  Column(String(100), nullable = False )
    ChuyenMon = Column(String(100), nullable = False )

    def __str__(self):
        return self.HoVaTen

class Lop(Base):
    __tablename__ = 'Lop'
    IDLop = Column(String(20),nullable = False, primary_key = True)
    TenLop = Column(String(100), nullable = False , unique=True)
    DiaDiem = Column(String(100), nullable = False )
    child = relationship("GiaoVien", backref="Lop")
    TongSoHS = Column(Float, nullable = False )
    NamNienKhoa = Column(String(20), nullable = False )

    GV_CN = Column(String(20), ForeignKey(GiaoVien.IDGiaoVien))
    FK_GiaoVien = relationship('GiaoVien', foreign_keys='Lop.GV_CN')

    IDKhoi  = Column(String(20), ForeignKey(Khoi.IDKhoi))
    FK_Khoi = relationship('Khoi', foreign_keys='Lop.IDKhoi')
    def __str__(self):
        return self.TenLop

class HocSinh(Base):
    __tablename__ = 'HocSinh'
    IDHocSinh = Column(String(20),nullable = False, primary_key = True)
    HoVaTen = Column(String(100), nullable = False )
    GioiTinh = Column(String(10), nullable = False )
    DiaChi =  Column(String(100), nullable = False )
    Email = Column(String(100), nullable = False )
    NgaySinh = Column(String(100), nullable = False )
    SoDienThoai = Column(String(11), nullable = False )
    SoDienThoaiPhuHuynh = Column(String(11), nullable = False )

    IDLop = Column(String(20), ForeignKey(Lop.IDLop))
    FK_Lop = relationship('Lop', foreign_keys='HocSinh.IDLop')

    IDNienKhoa = Column(String(20), ForeignKey(NienKhoa.ID))
    FK_Lop = relationship('NienKhoa', foreign_keys='HocSinh.IDNienKhoa')

    def __str__(self):
        return self.HoVaTen

class BangDiem(Base):
    __tablename__ = 'BangDiem'
    IDHocSinh = Column(String(20) , ForeignKey(HocSinh.IDHocSinh), primary_key = True,nullable = False)
    IDMon = Column(String(20),ForeignKey(Mon.IDMon),primary_key = True,nullable = False)

    FK_HocSinh = relationship('HocSinh', foreign_keys='HocSinh.IDHocSinh')
    FK_Mon = relationship('Mon', foreign_keys='Mon.IDMon')

    HocKy = Column(String(100), nullable = False )
    _15Phut_1_ = Column(Float, nullable = True )
    _15Phut_2_ = Column(Float, nullable = True )
    _15Phut_3_ = Column(Float, nullable = True )
    _45Phut_1_ = Column(Float, nullable = True )
    _45Phut_2_ = Column(Float, nullable = True )
    _45Phut_3_ = Column(Float, nullable = True )
    TrungBinhMon = Column(Float, nullable = True )
    GhiChu = Column(String(100), nullable = True )
    def __str__(self):
        return self.HoVaTen



Base.metadata.create_all(engine)
##############################################