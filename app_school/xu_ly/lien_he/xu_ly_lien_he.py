from flask import   Markup, url_for
import json
import os
from datetime import datetime
from xml.dom.minidom import Document
import xml.dom.minidom
import os.path

Thu_muc_contact = "app_school/du_lieu/contact/"

def tao_form_contact(Info) :
    doc = Document()
    
    root_xml = doc.createElement("Liên_hệ")
    doc.appendChild(root_xml)

    info_node = doc.createElement("Chi_tiết_liên_hệ")
    info_node.setAttribute("Họ_và_tên" , Info['Ho_va_ten'])
    info_node.setAttribute("Email" , str(Info['Email']))
    info_node.setAttribute("Nội_dung" , str(Info['Noi_dung']) )
    root_xml.appendChild(info_node)

    return doc

def ghi_info_contact(Info) :
    Ten_tap_tin = Thu_muc_contact + str(Info['Email']) +".xml"
    tao_form_contact(Info).writexml(open(file=Ten_tap_tin, mode ='w',encoding='utf8' ), indent='', addindent='', newl='')
    return True    
