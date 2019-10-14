
from jinja2 import Template
from .das_table import DasTable
import zipfile, os
from .code import Code


# 默认的 ssm 项目
class SSM(Code):
    
    def __str__(self):
        return "其实你懂的这个东西的"