
from jinja2 import Template
from .das_table import DasTable
import zipfile, os
from .code import Code


# 默认的 ssm 项目
class SSM(Code):

    def generate(self):
        super().generate()
        self.zip()
        
    def zip(self):
        zipf = zipfile.ZipFile('./static/code/%s.zip' % self.meta.name, 'w', zipfile.ZIP_DEFLATED)
        self.zip_dir(self.out_path, zipf)
        zipf.close()

    
    def __str__(self):
        return "其实你懂的这个东西的"