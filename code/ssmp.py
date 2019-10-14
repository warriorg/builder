
from jinja2 import Template
from .das_table import DasTable
import zipfile, os
from .code import Code

class SSMP(Code):
    '''
    这个项目中使用mybatis plus
    '''

    def tmpl_file(self, fp):
        return './code/templates/ssmp/' + fp + ".jinja"

