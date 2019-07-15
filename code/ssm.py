
from jinja2 import Template
from .das_table import DasTable
import zipfile, os


class SSM():
    __out_path ="out/"

    def __init__(self, table, columns, package="com.dc"):
        self.das_table = DasTable(table, columns)
        self.meta = self.das_table.get_class_metadata()
        self.meta.package = package
    

    def generate(self):
        self.generate_file(self.tmpl_file('model.java'), self.out(".java"))
        self.generate_file(self.tmpl_file('dto.java'), self.out("Dto.java"))
        self.generate_file(self.tmpl_file('param.java'), self.out("Param.java"))
        self.generate_file(self.tmpl_file('mapper.java'), self.out("Mapper.java"))
        self.generate_file(self.tmpl_file('mapper.xml'), self.out("Mapper.xml"))
        self.zip()
        

    def generate_file(self, tmplFile, outFile):
        with open(tmplFile) as ft:
            template = Template(ft.read())
        code = template.render(meta=self.meta)

        with open(outFile, "w") as f:
            f.write(code)
        

    def tmpl_file(self, fp):
        return './code/templates/ssm/' + fp + ".jinja"

    def out(self, fp):
        return self.__out_path + self.meta.name + fp

    def zip(self):
        zipf = zipfile.ZipFile('./static/code/%s.zip' % self.meta.name, 'w', zipfile.ZIP_DEFLATED)
        self.zip_dir(self.__out_path, zipf)
        zipf.close()


    def zip_dir(self, path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))
                os.remove(os.path.join(root, file))
