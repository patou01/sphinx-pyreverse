'''
Created on Oct 1, 2012

@author: alendit
'''
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive
from sphinx.util.compat import make_admonition
from subprocess import call
import os
from PIL import Image

try:
    from IPython import embed
except ImportError, e:
    pass


class UMLGenerateDirective(Directive):
    required_arguments = 1
    optional_arguments = 0
    has_content = False
    
    def run(self):
        env = self.state.document.settings.env
        SRC_DIR = env.srcdir
        DIR_NAME = "uml_images"
        UML_DIR = os.path.join(SRC_DIR, DIR_NAME)
        
        if os.path.basename(UML_DIR) not in os.listdir(SRC_DIR):
            os.mkdir(UML_DIR)
        env.uml_dir = UML_DIR
        module_path = self.arguments[0]
        os.chdir(UML_DIR)
        basename = os.path.basename(module_path).split(".")[0]
        print call(['pyreverse', '-o', 'png', '-p', basename, os.path.abspath(os.path.join(SRC_DIR, module_path))])
        uri = directives.uri(os.path.join(DIR_NAME, "classes_{0}.png".format(basename)))
        i = Image.open(os.path.join(SRC_DIR, uri))
        scale = 100
        max_width = 1000
        image_width = i.size[0]
        if image_width > max_width:
            scale = max_width * scale / image_width 
        img = nodes.image(uri=uri, scale=scale)
        os.chdir(SRC_DIR)
        return [img]

def setup(app):
    app.add_directive('uml', UMLGenerateDirective)