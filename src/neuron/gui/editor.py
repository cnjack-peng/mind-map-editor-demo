'''
Created on 24.11.2012

@author: Vendula Poncova
'''

from neuron.gui import template, test
from neuron.gui.maptree import MapTree
import wx

def run():
    
    app = wx.App(False)
    frame = MapEditor()
    frame.Show(True)
    app.MainLoop()


class MapEditor (template.MainFrame):
    '''
    Editor.
    '''

    def __init__(self):
        template.MainFrame.__init__(self, None)
        
        self.edit_node = None
        self.map_editor = None
        
        self.priorityChoice.Append("0")
        self.priorityChoice.Append("1")
        self.priorityChoice.Append("2")

        self.treeList = MapTree(self.treeScrolledWindow, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_SINGLE )
        self.treeList.SetSize(wx.Size(300,1024))

        self.mapctrl = self.setMap()
        self.treeList.setMapControler(self.mapctrl)
        
    def setMap(self):   
              
        # tests: 0,1,2,3,4
        mapctrl = test.test5(self)
        
        # save the variable
        return mapctrl
           
    def getCanvas(self):
        return self.canvasPanel
    
    def getTreeList(self):
        return self.treeList
    
    def deleteEditNode(self):
        self.edit_node = None
        
        self.nodeName.SetValue("")
        self.priorityChoice.SetSelection(1)      
    
    def setEditNode(self, node):
        
        self.edit_node = node
        
        # set the NodePanel
        self.nodeName.SetValue(node.getLabel())        
        self.priorityChoice.SetSelection(node.getPriority())
        self.colourChoice.SetColour(node.getColor())

        # set the icon
        self.nodeNote.SetValue(node.getNote())
        
    def changeNodeProperties(self, event):
        
        if self.edit_node:
            self.edit_node.setLabel(self.nodeName.GetValue())
            self.edit_node.setPriority(self.priorityChoice.GetSelection())
            self.edit_node.setColor(self.colourChoice.GetColour())
            self.edit_node.setNote(self.nodeNote.GetValue())
            
            self.mapctrl.repaint()
            
        
