'''
Created on 7.12.2012

@author: Vendula Poncova
'''

import wx

class ToolTip(object):
    '''
    Tip for a tool.
    '''

    def __init__(self, control):
        self.control = control
        self.texttip = ""
        self.visible = True
        
    def setTip(self, tip):
        self.texttip = tip
        
    def show(self, visible = True):
        self.visible = visible
    
    def draw(self, gcdc):
        
        gc = gcdc.GetGraphicsContext()
        
        gcdc.DrawLabel("TOOLTIP", (100, 10, 0, 0), wx.ALIGN_CENTER)
        
        
