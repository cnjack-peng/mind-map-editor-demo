'''
Created on 25.11.2012

@author: Vendula Poncova
'''

# vlastni import
from neuron import lib
from neuron.gui.nodemenu import NodeMenu
from neuron.gui.tooltip import ToolTip
from neuron.mindmap.drawer import MapDrawer
from neuron.mindmap.model import MindMap, MindNode
from neuron.mindmap.positioner import MapView

# gui knihovna
import wx


class MapControler(wx.PyControl):
    '''
    Application controler.
    '''
    
    frame = None
    map = None
    
    viewer = None
    views = None
    root = None
    
    toolbar = None
    edit_node = None
    edit_setting = False
    edit_lable = False
    
    dragged = None
    dragged_delta = (0,0)
    dragged_is_moved = False 

########################################################################## init()  
        
    def __init__(self, frame):
        super(MapControler, self).__init__(frame.getCanvas(), style = wx.NO_BORDER )

        # init

        self.frame = frame
        
        # set the mind map
        self.map = MindMap(self)
        self.root = self.map.getRoot()

        # views              
        self.views = MapView(self)
        self.viewer = MapDrawer(self)
             
        # the node menu
        self.toolbar = NodeMenu(self)
        self.edit_node = (self.map.getRoot(), 0)
        
        # the node
        self.tooltip = ToolTip(self)
        
        # set the background to white
        self.SetBackgroundColour(wx.Color(255, 255, 255, 255))
        self.SetSize(frame.getCanvas().GetSize())

        # action binding
        self.Bind(wx.EVT_PAINT,         self.onPaint, self) 
        self.Bind(wx.EVT_LEFT_DOWN,     self.onLeftDown, self)
        self.Bind(wx.EVT_LEFT_UP,       self.onLeftUp, self)
        self.Bind(wx.EVT_LEFT_DCLICK,   self.onLeftDouble, self)
        self.Bind(wx.EVT_RIGHT_UP,      self.onRightClick, self)
        self.Bind(wx.EVT_RIGHT_DCLICK,  self.onRightDouble, self)
        self.Bind(wx.EVT_MOTION,        self.onMotion, self)

        # change the size      
        frame.Bind(wx.EVT_SIZE,          self.onSize, frame)
 
########################################################################## get, set
    
    def getFrame(self):
        return self.frame
        
    def getMap(self):
        return self.map
    
    def getViewer(self):
        return self.viewer
    
    def getRoot(self):
        return self.root
    
    def getEditNode(self):
        return self.edit_node
 
########################################################################## node
    
    def addNode(self, parent, node):
        self.map.addNode(parent, node)
            
    def addNewNode(self, (parent, level)):

        # update the map
        node = MindNode(label = "New Node", color = lib.MapColor.random(), priority = 1)
        self.addNode(parent, node)
               
        # expand the parent
        if not self.isNodeExpanded(parent) :
            self.changeNodeExpanded(parent)
            
        # write info
        self.frame.setEditNode(node)
        
        # repaint
        self.repaint()

    def deleteNode(self, node):
        self.map.deleteNode(node)
        self.views.deleteNodeView(node)
        self.frame.deleteEditNode()

        if self.dragged and self.dragged[0] == node:
            self.dragged = None
            
        if self.edit_node and self.edit_node[0] == node:
            self.edit_node = None
            
        self.repaint()

    def changeParent(self, parent, node):
        
        # change the parent
        self.map.deleteNode(node)
        self.addNode(parent, node)
        
        # expand the parent
        if not self.isNodeExpanded(parent) :
            self.changeNodeExpanded(parent)
            
        # repaint
        self.repaint()
        
########################################################################## nodeView

    def getNodeView(self, node):
        return self.views.getNodeView(self.root, node)

    def getNodeBoundary(self, node):
        return self.views.getNodeBoundary(self.root, node)
    
    def setNodeBoundary(self, node, boundary):
        self.views.setNodeBoundary(self.root, node, boundary)
        
    def setNodeSize(self, node, size):
        self.views.setNodeSize(self.root, node, size)
        
    def setNodePosition(self, node, position):
        self.views.setNodePosition(self.root, node, position)
    
    def isNodeExpanded(self, node):
        return self.views.getNodeExpanded(self.root, node)
    
    def isNodeCommented(self, node):
        return self.views.getNodeCommented(self.root, node)
    
    def changeNodeExpanded(self, node):
        self.views.changeNodeExpanded(self.root, node)
        self.repaint()
    
    def changeNodeCommented(self, node):
        self.views.changeNodeCommented(self.root, node)
        self.repaint()
        
    def getNoteView(self, node):
        return self.views.getNoteView(self.root, node)
    
########################################################################## views

    #===========================================================================
    # showView
    # Show the mind map from a given root node.
    # Update the view and repaint.
    #===========================================================================
    def showView(self, root):
        # set the root node
        self.root = root

        # clean some of the settings
        self.dragged = None
        self.edit_node = None
        
        # repaint
        self.repaint()
         
    def changeView(self, (node, level)):
        if level == 0 and node.getParent() != None :
            node = node.getParent()
        
        self.showView(node)
        
    def prettyView(self):
        self.views.deployFirstLevel(self.root)
        self.repaint()

########################################################################## findNodes
        
    def findNodes(self, point):
            
        # init
        result = list()
        nodesList = list()
        nodesList.append((self.root, 0))
        
        # search the nodes
        while nodesList :
            (node, level) = nodesList.pop()
            
            if node != None :
                # check the area
                boundaries = self.getNodeBoundary(node)
                if lib.inArea(point, boundaries):
                    result.append((node, level))
                                
                # add the children
                if self.isNodeExpanded(node):
                    
                    for child in node.getChildren() :
                        nodesList.append((child, level + 1))
                     
        return result     

########################################################################## onSize

    def onSize(self, event):
        event.Skip()
        
        old_size = self.GetSize()
        new_size = self.frame.getCanvas().GetSize()
        
        # set the size of the canvas
        self.SetSize(new_size)
        
        # calculate the position of the node
        (new_w,new_h) = new_size.Get()
        (old_w,old_h) = old_size.Get()
        
        (x,y,w,h) = self.getNodeBoundary(self.root)
        dx = x * (1.0 * new_w / old_w) - x
        dy = y * (1.0 * new_h / old_h) - y
                
        # move the node
        self.moveNodes((self.root, 0), dx, dy)
        self.Refresh()
    
########################################################################## repaint,onPaint
        
    def repaint(self):
        
        self.views.actualize(self.root)
        self.frame.getTreeList().actualize()
        self.Refresh()
    
    def onPaint(self, event):
        event.Skip()

        # init
        dc = wx.PaintDC(self)
        gcdc = wx.GCDC(dc)

        # draw the map
        self.viewer.draw(gcdc)
        
        # draw node toolbar
        if self.edit_node and self.edit_node[0] != None :
            self.toolbar.draw(gcdc, self.edit_node, self.edit_setting)
            
        # test of colours
        # MapColor.draw(gcdc)
        
########################################################################## onLeftDown()
        
    def onLeftDown(self, event):
        event.Skip()

        # find the node in the area
        self.dragged = None
        nodeslist = self.findNodes(event.GetPosition())
        
        if nodeslist :
            # set the node that was clicked on
            self.dragged = nodeslist.pop()
            
            # params
            (node, level) = self.dragged
            (x, y, w, h) = self.getNodeBoundary(node)
            (ex, ey) = event.GetPosition()
            self.dragged_delta = (ex - x, ey - y)
            
            # reset the menu of the node
            self.frame.setEditNode(node)
            

########################################################################## onLeftUp()
    
    def onLeftUp(self, event):
        event.Skip()
        
        # expand the node
        if self.dragged and not self.dragged_is_moved :           
            self.changeNodeExpanded(self.dragged[0])

        # change the parents
        elif self.dragged and self.dragged_is_moved :
            
            # skip the root
            (node, level) = self.dragged
            if node != self.root:
            
                # get the list of nodes
                nodelist = self.findNodes(event.GetPosition())
                # add the default parent
                nodelist.insert(0, (self.root, 0))
            
                if len(nodelist) >= 2 :
                    # get node and a new parent
                    parent = None
                    node = self.dragged[0]
                     
                    while nodelist: 
                        (parent, level) = nodelist.pop()
                        if parent != node: break
                    
                    # change the parent of the node
                    if parent != node.getParent() :
                        self.changeParent(parent, node)
                
                # repaint
                self.repaint()
            
        elif self.edit_node :
            # clicked on the toolbar?
            tool = self.toolbar.findTool(self.edit_node, event.GetPosition())
                
            # clicked on a tool, do something
            if tool != None :
                (node, level) = self.edit_node
                
                if   tool == "list" :   self.changeNodeExpanded(node)
                elif tool == "note" :   self.changeNodeCommented(node)
                elif tool == "delete" : self.deleteNode(node)
                elif tool == "plus" :   self.addNewNode((node, level))
                elif tool == "root" :   self.changeView((node, level))
                elif tool == "setting": self.edit_setting = True

        # init
        self.dragged = None
        self.dragged_is_moved = False
        self.dragged_delta = (0,0)

########################################################################## onLeftDouble()

    def onLeftDouble(self, event):
        event.Skip()
        
        nodeslist = self.findNodes(event.GetPosition())
        if nodeslist :
            # which node was clicked on?
            (node, level) = nodeslist.pop()
            # start to edit the note of the node
            
 
########################################################################## onMotion()

    def moveNodes(self, (root, level), dx, dy):
            
        # init
        nodesList = list()
        nodesList.append((root, level))
        
        # search the nodes
        while nodesList :

            # get a node and the level
            (node, level) = nodesList.pop()

            if node != None :

                # set the position
                (x, y, w, h) = self.getNodeBoundary(node)
                self.setNodePosition(node, (x + dx, y + dy))

                # add chidren
                for child in node.getChildren() :
                        nodesList.append((child, level + 1))
                        
                              
    def onMotion(self, event):
        event.Skip()
        
        self.toolbar.highlightTool(None)
        
        if self.dragged != None:
            
            # hide the menu
            self.edit_node = None
            
            # dragged node is moving
            self.dragged_is_moved = True
            
            # init
            (node, level) = self.dragged
            (dx, dy) = self.dragged_delta
            
            (x, y, w, h) = self.getNodeBoundary(node)
            (ex,ey) = event.GetPosition()
            
            # skip the root
            #if level != 0 :
            
            # set the position
            self.moveNodes(self.dragged, ex - dx - x, ey - dy - y)
            # repaint
            self.Refresh()
            
        else:
            # movement at the toolbar?
            tool = self.toolbar.findTool(self.edit_node, event.GetPosition())
            self.toolbar.highlightTool(tool)
                
            # otherwise
            if tool == None :
                
                nodeslist = self.findNodes(event.GetPosition())
                if nodeslist :
                    self.edit_node = nodeslist.pop()
                else:
                    self.edit_node = None
                    self.edit_setting = None
                
            # repaint
            self.Refresh()

########################################################################## onRightClick, onRightDouble

    def onRightClick(self, event):
        event.Skip()
 
    def onRightDouble(self, event):
        event.Skip()

        # get the node
        nodelist = self.findNodes(event.GetPosition())
        
        # create new view
        if nodelist :                 
            self.changeView(nodelist.pop())
        

        
            
