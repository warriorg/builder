
from jinja2 import Template
from .das_table import DasTable
import zipfile, os


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
            self.generate_file(tmpl_meta["tmpl"], tmpl_meta["name"])
            
        self.zip()

    def tmpl_file_dict(self, fp):
        return {
            "model.java": {'tmpl': "./code/templates/basic/model.java.jinja", 'name': '.java'},
            "dto.java": {'tmpl': "./code/templates/basic/dto.java.jinja", 'name': 'Dto.java'},
            "param.java": {'tmpl': "./code/templates/basic/param.java.jinja", 'name': 'Param.java'},
            "mapper.java": {'tmpl': "./code/templates/basic/mapper.java.jinja", 'name': 'Mapper.java'},
            "mapper.xml": {'tmpl': "./code/templates/basic/mapper.xml.jinja", 'name': 'Mapper.xml'}, 
        }
    

    def generate_file(self, tmplFile, outFile):
        with open(tmplFile) as ft:
            template = Template(ft.read())
        code = template.render(meta=self.meta)

        with open(outFile, "w") as f:
            f.write(code)
        

    def out(self, fp):
        return self.out_path + self.meta.name + fp

    def zip(self):
        zipf = zipfile.ZipFile('./static/code/%s.zip' % self.meta.name, 'w', zipfile.ZIP_DEFLATED)
        self.zip_dir(self.out_path, zipf)
        zipf.close()


    def zip_dir(self, path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))
                os.remove(os.path.join(root, file))