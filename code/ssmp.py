
from jinja2 import Template
from .das_table import DasTable
import zipfile, os
from .code import Code

class SSMP(Code):
    '''
    这个项目中使用mybatis plus
    '''

    def tmpl_file_dict(self):
        dict = super().tmpl_file_dict()
        dict["model.java"] = {'tmpl': "./code/templates/ssmp/model.java.jinja", 'name': '.java'}
        dict["dto.java"] = {'tmpl': "./code/templates/ssmp/dto.java.jinja", 'name': 'Dto.java'}
        return dict

    def __str__(self):
       return "其实你懂的这个东西的"