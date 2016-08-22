'''
Created on 30.11.2012

@author: Vendula Poncova
'''

from wx.lib.mixins.treemixin import VirtualTree
import wx

class MapTree(VirtualTree, wx.TreeCtrl):
    '''
    Tree representation of the mind map.
    '''
    
    def __init__(self, *args, **kw):
        super(MapTree, self).__init__(*args, **kw)
        self.mapctrl = None
        self.indexlist = {}
        
        self.Bind(wx.EVT_LEFT_DCLICK, self.onLeftDouble, self)

    def setMapControler(self, ctrl):
        self.mapctrl = ctrl
        self.actualize()
        
    def findNode(self, indices):
        
        # fiktivni root    
        if indices == () : return None
        
        # prochazeni od roota mapy
        node = self.mapctrl.getMap().getRoot()
        
        # vyhledej prislusny uzel
        for index in indices[1:] :
            
            if index != None :
                node = node.getChildren()[index]
        
        return node  

    def actualize(self):

        # aktualizace uzlu
        self.RefreshItems()
        self.ExpandAll()
        
    def OnGetItemFont(self, indices) :
        
        font = self.GetFont()
        
        if self.mapctrl == None : return font
    
        # vyhledej uzel
        node = self.findNode(indices)
        
        # falesny uze;
        if node == None : return font
        
        # vrat popisek uzlu
        if node == self.mapctrl.getRoot():
            
            font.SetWeight(wx.FONTWEIGHT_BOLD)
            return font
        
        else :        
            return font


    def OnGetItemText(self, indices):
    
        if self.mapctrl == None : return ""
    
        # vyhledej uzel
        node = self.findNode(indices)
        
        # falesny uze;
        if node == None : return "root"
        
        # vrat popisek uzlu        
        return node.getLabel()
    
    def OnGetChildrenCount(self, indices):

        if self.mapctrl == None : return 0

        # vyhledej uzel
        node = self.findNode(indices)
        
        # falesny uze;
        if node == None : return 1
        
        # vrat pocet nasledniku uzlu        
        return len(node.getChildren())
    

    def onLeftDouble(self, event):
        
        
        # zjisti index polozky, na kterou se kliklo
        item, flags = self.HitTest(event.GetPosition())
        index = self.GetIndexOfItem(item)
        
        # najdi uzel na indexu
        node = self.findNode(index)
        # nastav jej jako root
        if node: 
            #print(node.getLabel())
            self.mapctrl.showView(node)
        
        
        
