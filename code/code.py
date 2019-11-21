
from jinja2 import Template
from .das_table import DasTable
import zipfile, os, errno


class Code():
    '''
    代码生成的基类
    '''

    out_path ="out/"

    def __init__(self, table, columns, package="com.dc"):
        self.das_table = DasTable(table, columns)
        self.meta = self.das_table.get_class_metadata()
        self.meta.package = package
    

    def generate(self):
        tmpl_dict = self.tmpl_file_dict()
        for key in tmpl_dict:
            tmpl_meta = tmpl_dict[key]
            self.generate_file(tmpl_meta["tmpl"], self.out(tmpl_meta))
            
    def tmpl_file_dict(self):
        '''
        提供动态检查文件是否许哟啊覆盖
        '''
        return {
            "model.java": {'tmpl': "./code/templates/basic/model.java.jinja", 'name': '.java', 'package': 'model'},
            "dto.java": {'tmpl': "./code/templates/basic/dto.java.jinja", 'name': 'Dto.java', 'package': 'dto'},
            "param.java": {'tmpl': "./code/templates/basic/param.java.jinja", 'name': 'Param.java', 'package': 'dto'},
            "mapper.java": {'tmpl': "./code/templates/basic/mapper.java.jinja", 'name': 'Mapper.java', 'package': 'dao'},
            "mapper.xml": {'tmpl': "./code/templates/basic/mapper.xml.jinja", 'name': 'Mapper.xml', 'package': 'dao'}, 
        }
    

    def generate_file(self, tmplFile, outFile):
        with open(tmplFile) as ft:
            template = Template(ft.read())
        code = template.render(meta=self.meta)

        if not os.path.exists(os.path.dirname(outFile)):
            try:
                os.makedirs(os.path.dirname(outFile))
            except OSError as exc: 
                if exc.errno != errno.EEXIST:
                    raise

        with open(outFile, "w") as f:
            f.write(code)
        

    def out(self, tmpl_meta):
        out_file = self.out_path
        if 'package' in tmpl_meta:
           out_file += tmpl_meta['package'] + '/'

        out_file += self.meta.name + tmpl_meta['name']
        return out_file


    def zip_dir(self, path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))
                os.remove(os.path.join(root, file))