'''
Created on 24.11.2012

@author: Vendula Poncova
'''

from .editor import *
from .nodemenu import *

def run():
    from . import editor
    editor.run()
