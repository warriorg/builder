
from jinja2 import Template
from .das_table import DasTable
import zipfile, os
from .code import Code


# 默认的 ssm 项目
class SSM(Code):

    def generate(self):
        super().generate()
        self.zip()

    def tmpl_file_dict(self):
        dict = super().tmpl_file_dict()
        dict["model.java"] = {'tmpl': "./code/templates/ssm/model.java.jinja", 'name': '.java', 'package': 'model'}
        dict["dto.java"] = {'tmpl': "./code/templates/ssm/dto.java.jinja", 'name': 'Dto.java', 'package': 'dto'}
        dict["param.java"] = {'tmpl': "./code/templates/ssm/param.java.jinja", 'name': 'Param.java', 'package': 'dto'}
        dict["mapper.java"] = {'tmpl': "./code/templates/ssm/mapper.java.jinja", 'name': 'Mapper.java', 'package': 'dao'}
        dict["mapper.xml"] = {'tmpl': "./code/templates/ssm/mapper.xml.jinja", 'name': 'Mapper.xml', 'package': 'dao'}
        dict["mapper.java"] = {'tmpl': "./code/templates/ssm/mapper.java.jinja", 'name': 'Mapper.java', 'package': 'dao'}
        dict["mapper.xml"] = {'tmpl': "./code/templates/ssm/mapper.xml.jinja", 'name': 'Mapper.xml', 'package': 'dao'}
        dict["dtoMpper.java"] = {'tmpl': "./code/templates/ssm/dtoMapper.java.jinja", 'name': 'DtoMapper.java', 'package': 'mapper'}
        dict["service.java"] = {'tmpl': "./code/templates/ssm/service.java.jinja", 'name': 'Service.java', 'package': 'service'}
        dict["serviceImpl.java"] = {'tmpl': "./code/templates/ssm/serviceImpl.java.jinja", 'name': 'ServiceImpl.java', 'package': 'service.impl'}
        dict["controller.java"] = {'tmpl': "./code/templates/ssm/controller.java.jinja", 'name': 'Controller.java', 'package': 'api'}
        
        return dict
        
    def zip(self):
        zipf = zipfile.ZipFile('./static/code/%s.zip' % self.meta.name, 'w', zipfile.ZIP_DEFLATED)
        self.zip_dir(self.out_path, zipf)
        zipf.close()
    
    
    def __str__(self):
        return "其实你懂的这个东西的"