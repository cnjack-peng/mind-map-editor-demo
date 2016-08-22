'''
Created on 29.11.2012

@author: Vendula Poncova
'''

from neuron import lib
import math

########################################################################## NodeView

class NodeView(object):
    '''
    The view at the node.
    '''
    
    def __init__(self, position = (0,0), size = (0,0), commented = True, expanded = True):

        self.position = position
        self.size = size
        self.expanded = expanded 
        self.commented = commented
        self.note_view = "", (0,0,0,0)

    def getNodePosition(self):
        return self.position
    
    def setNodePosition(self, position):
        self.position = position
        
    def getNodeSize(self):
        return self.size
    
    def setNodeSize(self, size):
        self.size = size
        
    def getNodeExpanded(self):
        return self.expanded
    
    def changeNodeExpanded(self):
        self.expanded = not self.expanded
        
    def getNodeCommented(self):
        return self.commented
    
    def changeNodeCommented(self):
        self.commented = not self.commented
        
    def getNoteView(self):
        return self.note_view
        
    def setNoteView(self, note, size):
        self.note_view = note, size

########################################################################## MapView

class MapView(object):
    '''
    The view at the mind map.
    '''
    
    control = None
    
    root_view = None
    views = None
    
    def __init__(self, control):
        self.control = control       
        self.views = {}
        
        # default settings for the root
        self.root_view = NodeView(position = (200,150), size = (100,100), expanded = True)
        

########################################################################## add

    def addMapView(self, root, mapview):
        self.views[root.getId()] = mapview

    def addNodeView(self, root, node, nodeview):
        mapview = self.getMapView(root)
        mapview[node.getId()] = nodeview        

########################################################################## get 

    def getViews(self):
        return self.views
    
    def getMapView(self, root):
        
        if root  and  (root.getId() in self.views) :
            return self.views[root.getId()]
        else :
            return None

    def getNodeView(self, root, node):

        # if it is a root, return the view on the root
        if node and root == node :
            return self.root_view
        
        # get the mapview and check its existence
        mapview = self.getMapView(root)
        if not mapview : 
            return None
        
        # if the node has a view, return this view
        elif node and (node.getId() in mapview) :
            return mapview[node.getId()]
        
        # error
        else :
            return None
    
    def getNodePosition(self, root, node):
        nodeview = self.getNodeView(root, node)
        return nodeview.getNodePosition()
    
    def getNodeSize(self, root, node):
        nodeview = self.getNodeView(root, node)
        return nodeview.getNodeSize()
    
    def getNodeBoundary(self, root, node):
        (x,y) = self.getNodePosition(root, node)
        (w,h) = self.getNodeSize(root, node)
        return (x,y,w,h)
    
    def getNodeCommented(self, root, node):
        nodeview = self.getNodeView(root, node)
        return nodeview.getNodeCommented()
    
    def getNodeExpanded(self, root, node):
        nodeview = self.getNodeView(root, node)
        return nodeview.getNodeExpanded()
    
    def getNoteView(self, root, node):
        nodeview = self.getNodeView(root, node)
        return nodeview.getNoteView()


########################################################################## set  
    
    def setNodeBoundary(self, root, node, (x,y,w,h)):
        self.setNodePosition(root, node, (x,y))
        self.setNodeSize(root, node, (x,y))
        
    def setNodePosition(self, root, node, position):
        nodeview = self.getNodeView(root, node)
        nodeview.setNodePosition(position)
        
    def setNodeSize(self, root, node, size):
        nodeview = self.getNodeView(root, node)
        nodeview.setNodeSize(size)
        
    def changeNodeExpanded(self, root, node):
        nodeview = self.getNodeView(root, node)
        nodeview.changeNodeExpanded()    
        
    def changeNodeCommented(self, root, node):
        nodeview = self.getNodeView(root, node)
        nodeview.changeNodeCommented()
        
    def setNoteView(self, root, node, note, size):
        nodeview = self.getNodeView(root, node)
        nodeview.setNoteView(note, size)
        
########################################################################## delete

    def deleteNodeView(self, node):
        
        # for all roots
        for rootid in list(self.views) :
            
            # delete the mapview
            if rootid == node.getId() :
                del self.views[rootid]
                break
            
            # for all nodes
            for nodeid in list(self.views[rootid]) :
                
                # delete the node
                if nodeid == node.getId() :
                    del self.views[rootid][nodeid] 

        
########################################################################## calculateSize

    def calculateNodeSize(self, node, level):     
    
        # get the dimensions of the title
        font =  lib.getFont(level, node.getPriority)
        (w,h) = lib.getTextSize(self.control, node.getLabel(), font)
        #(note_w, note_h) = self.calculateNoteSize(node)

        # set the minimum and check
        if level == 1 : 
            w = max(w + 60, 100)
            h = max(h, 25)
        
        else :
            w = max(w + 40, 100)
            h = max(h, 25)
        
        # return the dimensions of the node
        return (w,h) 
    
    def calculateNoteView(self, root, node, level = 1):
        
        if node and node.getNote() and self.getNodeCommented(root, node):
            
            (width, height) = self.getNodeSize(root, node)
                   
            if level > 1:
                (dw, dh) = (10, 30)
                width = max(width, 200)
            else:
                (dw, dh) = (14, 30) 
        
            lines, (w,h) = lib.getMultilineText(self.control, node.getNote(), width - dw/4)    
            
            return lines, (max(w,width), h, dw, dh)
        
        else:
            return None, (0,0,0,0)
            

########################################################################## actualize

    #===========================================================================
    # actualize
    # Aktualizuje hodnoty datove struktury pro mapview daneho roota.
    # 1. Pokud nodeview neexistuje, vytvor jej
    # 2. Prepocitej velikosti vsech uzlu
    # 3. Prepocitej rozmisteni dalsich levelu
    #===========================================================================
    def actualize(self, root):
        # error
        if root == None:
            return
        
        # check the existence of the mapview
        isNew = False
        mapview = self.getMapView(root)
        
        if mapview == None :
            self.addMapView(root, {})
            isNew = True
                 
        # create the nodeviews and set the sizes
        nodesList = list()
        nodesList.append((root, 0))
        
        # search the nodes
        while nodesList :
            (node, level) = nodesList.pop()
            
            if node != None :
                
                # skip the root
                if level > 0 :
                    
                    # get the view
                    nodeview = self.getNodeView(root, node)
                    
                    # does it exist?
                    if nodeview == None:
                        # create new one
                        nodeview = NodeView()
                        self.addNodeView(root, node, nodeview)
                        
                        # set the position
                        (x,y) = self.getNodePosition(root, root)
                        nodeview.setNodePosition((x + 100, y - 100))
                        
                    # set the size of the node
                    size = self.calculateNodeSize(node, level)
                    nodeview.setNodeSize(size)
                    
                # set the size of the note
                note, note_size = self.calculateNoteView(root, node, level)
                self.setNoteView(root, node, note, note_size)
                                
                # add children
                for child in node.getChildren() :
                    nodesList.append((child, level + 1))
        
        
        # if the view is new, deploy the first level of nodes
        if isNew : self.deployFirstLevel(root)
        
        # deploy next level nodes
        self.deployNextLevels(root)
        


########################################################################## deploy

    #===============================================================================
    # deployFirstLevel
    # Nastavi pozici prvni urovni uzlu a rozestavi je rovnomerne kolem roota.
    #===============================================================================
    def deployFirstLevel(self, root = None):
        
        # default
        if root == None :
            root = self.control.getRoot()
            
        # error
        if root == None or len(root.getChildren()) == 0:
            return
               
        # the root is in the middle
        (x,y,w,h) = self.getNodeBoundary(root, root)
        
        (center_x, center_y) = (x + w / 2, y + h / 2)
        
        r = 100
        delta = 2.0 * math.pi / len(root.getChildren())
        
        # korekce
        #alpha = 7.0 / 4.0 * math.pi
        alpha = 5.0 / 4.0 * math.pi
        
        delta_max = 1.0 / 2.0 * math.pi
        if delta > delta_max : delta = delta_max
        
        # first level
        for child in root.getChildren() :
            
            # get the size of the node
            (w,h) = self.getNodeSize(root, child)

            # calculate the position
            x = math.cos(alpha) * (r + w/2)
            y = math.sin(alpha) * (r + 50)
            alpha -= delta
            
            new_x = center_x + x - w / 2
            new_y = center_y + y - h / 2
            
            # set the position
            self.setNodePosition(root, child, (new_x, new_y))
               

    #===========================================================================
    # deployNextLevels
    # Nastavi pozici dalsim levelum, rozmisti je do seznamu.
    #===========================================================================
    def deployNextLevels(self, root = None, level = 0):

        # default
        if root == None :
            root = self.control.getRoot()
            level = 0
            
        # error
        if root == None or len(root.getChildren()) == 0:
            return
            
        # first level
        nodesList = list()
        nodesList.append((root, level, (0,0)))
        
        # for all nodes
        while nodesList :
            (node, level, (nx, ny)) = nodesList.pop()
            
            if node != None : 
                       
                # level zero and one
                if level == 0 or level == 1 :
                    (x,y,w,h) = self.getNodeBoundary(root, node)
                    (note_w, note_h, note_dw, note_dh) = (0,0,0,0)
                    
                    x += w + 10     # position of the list
                    y -= h          # position of the list
                    
                # other levels
                if level > 1 :
                    (w,h) = self.getNodeSize(root, node)
                    
                    x = nx + 40     # horizontal position
                    y += 0.7 * h    # vertical position
                    
                    # set the position
                    self.setNodePosition(root, node, (nx, y))
                    
                    # add the size of the note
                    note,(note_w, note_h, note_dw, note_dh) = self.getNoteView(root, node)
                    y += note_h + note_dh 
                    
                # if expanded, add children
                if self.getNodeExpanded(root, node):
                                   
                    childlist = list(node.getChildren())
                    childlist.reverse()
                
                    for child in childlist :
                        nodesList.append((child, level + 1, (x , y))) 

        

        
