'''
Created on 28.11.2012

@author: Vendula Poncova
'''

from neuron import lib
import wx

class NodeMenu(object):
    '''
    Menu for the node.
    '''
    control = None
    
    icons = {}
    iconsize = 0
    iconspace = 0
        
    highlighted = None
        
    def __init__(self, control):
        '''
        Constructor
        '''
        self.control = control
        
        self.icons = lib.NodeIcons.getIcons()
        self.iconsize = lib.NodeIcons.getSize()
        self.iconspace = lib.NodeIcons.getSpace()       
       
    def show(self, editnode):
        self.edit_node = editnode
        
    def hide(self):
        self.edit_node = None
        self.highlighted = None
    
    def getPosition (self, (node, level)):
        boundary = self.control.getNodeBoundary(node)
        return lib.NodeIcons.getPosition(level, boundary) 
        
    def highlightedToolName(self, tool):
        return tool + "_color"
    
    def oppositeToolName(self, tool):
        return tool + "_opposite"
        
    def getTools(self, (node, level)):
        
        hasNote = node.getNote()
        hasChildren = node.getChildren()     
        
        tools = ["plus", "root", "setting"]
        
        # prvni root nema rodice
        if node == self.control.map.getRoot():
            tools.remove("root")
                             
        # prvky od prvni urovne lze smazat
        if level > 0 :
            tools.append("delete")
        
        # nastoje pro zobrazovani poznamek a nasledniku
        if hasNote or hasChildren:
            
                tools.append("separator")
                
                if hasNote :        tools.append("note")                    
                if hasChildren :    tools.append("list")
        
        # vrati nastroje        
        return tools
        
    def highlightTool(self, tool):
        
        if tool == None or tool == "" :
            self.highlighted = None
            
        else :
            self.highlighted = tool
    
    def findTool(self, editnode, point):
        
        if not editnode :
            return None
        
        (node, level) = editnode
        
        # ziskej pozici menu
        (x,y) = self.getPosition((node, level))
        
        # ziskej nastroje
        tools = self.getTools((node, level))
        
        # test na celou oblast menu
        
        tolerance = 10
        menu_x = x - tolerance
        menu_y = y - tolerance
        menu_w = 2 * tolerance + len(tools) * self.iconsize + (len(tools) - 1) * self.iconspace
        menu_h = 2 * tolerance + self.iconsize
        area = (menu_x, menu_y, menu_w, menu_h)
        
        if not lib.inArea(point, area) :
            return None
        
        # hledani konkretniho nastroje
        
        dx = 0
        
        for tool in tools :
            
            # preskocit separator
            if tool == "separator" :
                dx += self.iconsize/5 + self.iconspace
                continue
            
            # vypocet oblasti
            area = (x + dx, y, self.iconsize, self.iconsize)
            # leze bod v oblasti ikonky nastroje ?
            if lib.inArea(point, area) :
                return tool
            # posun na dalsi ikonku
            dx += self.iconsize + self.iconspace
         
        # hledani je neuspesne    
        return ""
            
        
    
    def draw(self, gcdc, (node, level), setting = None):
        
        if setting :
            self.drawSetting(gcdc, (node, level))            
        else:
            self.drawMenu(gcdc, (node, level))

            
    def drawMenu(self, gcdc, (node, level)):
        
        (x,y) = self.getPosition((node, level))
        tools = self.getTools((node, level)) 
                        
        for tool in tools :

            # nastaveni nazvu ikony a pozice
            toolname = tool
            (w,h) = (self.iconsize, self.iconsize)
            
            # uprava nazvu ikony:
            if tool == "note" and self.control.isNodeCommented(node):
                toolname = self.oppositeToolName(toolname)
                
            elif tool == "list" and self.control.isNodeExpanded(node):
                toolname = self.oppositeToolName(toolname)
                
            if tool == self.highlighted :
                toolname = self.highlightedToolName(toolname)

            # separator menu
            if tool == "separator":
                (w,h) = (self.iconsize/5, self.iconsize)     
                
            # vykresleni ikony
            img = lib.resizeImage(self.icons[toolname], w, h)  
            gcdc.DrawBitmap(img, x, y)
            
            # posunuti xove souradnice          
            x = x + w + self.iconspace
            
            
    def drawSetting(self, gcdc, (node, level)):
        
        (x,y) = self.getPosition((node, level))
        (w,h) = (self.iconsize, self.iconsize)

        (label, icon, priority, color, note) = node.getProperties()
                                  
        # vykresleni ikony
        toolname = "setting"
        img = lib.resizeImage(self.icons[toolname], w, h)  
        gcdc.DrawBitmap(img, x, y)
            
        x = x + w + self.iconspace

        # vykresleni oddelovace
        toolname = "separator"
        img = lib.resizeImage(self.icons[toolname], w/5, h)  
        gcdc.DrawBitmap(img, x, y)
            
        x = x + w/5 + self.iconspace

        
        # vykresleni ikonky pisma
        toolname = "setting"
        img = lib.resizeImage(self.icons[toolname], w, h)  
        gcdc.DrawBitmap(img, x, y)
            
        x = x + w + self.iconspace
        
        # vykresleni ikony uzlu
        icon = wx.Bitmap("neuron/img/icon.png", type = wx.BITMAP_TYPE_PNG)
        img = lib.resizeImage(icon, w, h)  
        gcdc.DrawBitmap(img, x, y)
            
        x = x + w + self.iconspace
        
        # vykresleni barvy
        gcdc.SetBrush(wx.Brush(color))
        gcdc.DrawRectangle(x, y, w, h)
                      
        x = x + w + self.iconspace
        
        # vykresleni priority
        img = lib.resizeImage(self.icons[toolname], w, h)  
        gcdc.DrawBitmap(img, x, y)
            
        x = x + w + self.iconspace
        
        
                    
