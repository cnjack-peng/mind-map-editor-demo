'''
Created on 24.11.2012

@author: Vendula Poncova
'''

from neuron import lib
import wx

class MapDrawer ():
    '''
    Drawer of the mind map.
    '''
    control = None   
    
    def __init__(self, control):
        '''
        Constructor
        '''      
        self.control = control

########################################################################## drawing map

    def draw (self, gcdc):
                
        # priprava
        nodesList = list()
        nodesList.append((self.control.getRoot(), 0))
        
        # vykresleni vsech uzlu
        while nodesList :
            (node, level) = nodesList.pop()
            
            if node != None:
                
                # pokud ma byt uzel expandoan, vykresli potomky
                if self.control.isNodeExpanded(node):
                
                    for child in node.getChildren() :
                        # pridej naslednika
                        nodesList.append((child, level + 1))
                        # vykresli hranu
                        if child != None :
                            self.drawEdge(gcdc, node, child, level)
                
                # vykresleni uzlu        
                self.drawNode(gcdc, node, level)
                self.drawNote(gcdc, node, level)
                
                # vykresleni priznaku poznamka a naslednici
                if (node, level) != self.control.getEditNode() :
                    self.drawIcons(gcdc, node, level)
                  

    def drawNode (self, gcdc, node, level = -1) :
        
        gc = gcdc.GetGraphicsContext()
        
        # parametry pro vykresleni
        (x, y, w, h) = self.control.getNodeBoundary(node)
        (label, icon, priority, color, note) = node.getProperties()
        
        grey = wx.Color(200, 200, 200)
        shadow = wx.Color(0, 0, 0, 50)

        # nastaveni pera a stetce
        gc.SetPen(gc.CreatePen(wx.TRANSPARENT_PEN))
        gcdc.SetTextForeground('BLACK')        
        
        # nastaveni fontu
        lib.setFont(gcdc, level, priority)
        
        # icon
        icon = wx.Bitmap("./neuron/img/icon.png", type = wx.BITMAP_TYPE_PNG)
            
        # vykresleni podle typu uzlu
        if level == 0 :
            # nakresli stin
            gcdc.SetBrush(wx.Brush(shadow))
            gcdc.DrawEllipse(x + 3, y + 3, w, h)
            
            # elipsa
            if color : gcdc.SetBrush(wx.Brush(color))
            gcdc.DrawEllipse(x, y, w, h)

            # ikonka
            image = lib.resizeImage(icon, w * 0.3, w * 0.3)     
            gcdc.DrawBitmap(image, x + w * 0.35, y + 10)
             
            # napis
            lib.setFont(gcdc, level, priority)
            gcdc.DrawLabel(label, (x, y + 10, w, h), wx.ALIGN_CENTER)
            
        elif level == 1 :
            # nakresli stin
            gcdc.SetBrush(wx.Brush(shadow))
            gcdc.DrawRoundedRectangle(x + 6, y + 3, w - 3, h, 5)
            
            # obdelnik
            if color : gcdc.SetBrush(wx.Brush(color))
            gcdc.DrawRoundedRectangle(x, y, w, h, 5)
            
            # ikonka
            image = lib.resizeImage(icon, h * 0.8, h * 0.8)     
            gcdc.DrawBitmap(image, x + 8, y + h * 0.1)

            # napis 
            gcdc.DrawLabel(label, (x + h + 10, y, w - h, h), 
                           wx.ALIGN_LEFT or wx.ALIGN_CENTRE_VERTICAL)
            
        else :
            # ikonka
            image = lib.resizeImage(icon, h * 0.5, h * 0.5)     
            gcdc.DrawBitmap(image, x, y + h * 0.25)
            
            gcdc.DrawLabel(label, (x + h * 0.7, y, w - h, h), 
                           wx.ALIGN_LEFT or wx.ALIGN_CENTRE_VERTICAL)               
    
    
    def drawNote(self, gcdc, node, level = 1):
        
            # nakresli poznamku ?
            if not node.getNote() or not self.control.isNodeCommented(node):
                return
            
            # ohraniceni
            (x, y, w, h) = self.control.getNodeBoundary(node)
                
            note, (note_w, note_h, note_dw, note_dh) = self.control.getNoteView(node)
            
            # nastaveni
            color = wx.Color(200, 200, 200)
            textcolor = wx.Color(150, 150, 150)
            
            lib.setFont(gcdc, -1)
            
            if level == 0 or level == 1 :
                
                # kresleni trojuhelniku
                pt1 = (x + w/2, y + h + 5)
                pt2 = (x + w/2 - 7, y + h + 10)
                pt3 = (x + w/2 + 7, y + h + 10)
                
                # kresleni obdelniku
                gcdc.SetBrush(wx.Brush(color))
                gcdc.DrawPolygon((pt1, pt2, pt3))
                gcdc.DrawRoundedRectangle(x, y + h + 10, note_w, note_h + note_dh, 10)
                
                gcdc.SetBrush(wx.Brush('WHITE'))
                d = 2
                gcdc.DrawRoundedRectangle(x + d, y + h + 10 + d, note_w -2*d, note_h + note_dh -2*d, 10)
                
                # kresleni textu
                gcdc.SetTextForeground(textcolor)
                gcdc.DrawLabel(note, wx.Rect(x  + note_dw/2, y + h + 10 + note_dh/2, 0, 0)) 
 
            else:
                
                # kresleni trojuhelniku
                pt1 = (x + 40, y + h - 5)
                pt2 = (x + 40 - 7, y + h)
                pt3 = (x + 40 + 7, y + h)
                
                # kresleni obdelniku
                gcdc.SetBrush(wx.Brush(color))
                gcdc.DrawPolygon((pt1, pt2, pt3))
                gcdc.DrawRoundedRectangle(x + 20, y + h, note_w + note_dw, note_h + note_dh/2, 10)
                
                gcdc.SetBrush(wx.Brush('WHITE'))
                d = 2
                gcdc.DrawRoundedRectangle(x + 20 + d, y + h + d, note_w + note_dw -2*d, note_h + note_dh/2 -2*d, 10)
                
                # kresleni textu
                gcdc.SetTextForeground(textcolor)
                gcdc.DrawLabel(note, wx.Rect(x + 20 + note_dw/2, y + h + note_dh/4, 0, 0)) 
     
    def drawEdge (self, gcdc, parent, child, level) :
         
        A = parent
        B = child 
         
        if level in (0,1) :
            (xA, yA, wA, hA) = self.control.getNodeBoundary(A)
            (xB, yB, wB, hB) = self.control.getNodeBoundary(B)
            
            # nastaveni pera a stetce
            grey = wx.Color(200, 200, 200)
            gcdc.SetPen(wx.Pen(grey, width = 2))        
            gcdc.SetBrush(wx.Brush(grey))
            
            # vykresleni podle typu uzlu
            gcdc.DrawLine(xA + wA/2, yA + hA/2, xB + wB/2, yB + hB/2)        
        
    
    def drawIcons(self, gcdc, node, level):
                
        (x, y, w, h) = self.control.getNodeBoundary(node)
        (posx, posy) = lib.NodeIcons.getPosition(level, (x,y,w,h))
        
        iconsize = lib.NodeIcons.getSize()
        iconspace = lib.NodeIcons.getSpace()
        icons = lib.NodeIcons.getIcons()
               
        hiddenNote = node.getNote() and not self.control.isNodeCommented(node)
        hiddenList = node.getChildren() and not self.control.isNodeExpanded(node)
        
        
        if hiddenList:
            img = lib.resizeImage(icons["list"], iconsize, iconsize)  
            
            if level == 1 :
                gcdc.DrawBitmap(img, posx + w - iconsize, posy)
                posx = posx - iconsize - iconspace
            else :
                gcdc.DrawBitmap(img, posx, posy)
                posx = posx + iconsize + iconspace

            
        if hiddenNote:
            img = lib.resizeImage(icons["note"], iconsize, iconsize)             

            if level == 1 :
                gcdc.DrawBitmap(img, posx + w - iconsize, posy)
                posx = posx - iconsize - iconspace
            else :
                gcdc.DrawBitmap(img, posx, posy)
                posx = posx + iconsize + iconspace            
                 
########################################################################## end
