'''
Created on 24.11.2012

@author: Vendula Poncova
'''

class MindMap(object):
    '''
    The model of the mind map.
    '''
    rootNode = None
    control = None
    
    #next_id = 0

    def __init__(self, control):
        '''
        Constructor
        '''
        self.control = control
     
    def getRoot(self):
        return self.rootNode
        
    def addNode(self, parent, node):

        if parent == None :
            self.rootNode = node
        else :
            parent.addChild(node)
            
    def deleteNode(self, node):
        if node != None :
            parent = node.getParent()
            # is it root?
            if parent == None :
                self.rootNode = None
            # delete the child
            else :
                parent.deleteChild(node)

class MindNode(object):
    '''
    The model for the node of the mind map.
    '''
    # static id
    next_id = 0
    
    # params
    parent = None
    children = list()
    id = 0
    
    # properties
    label = None
    icon = None
    priority = 1
    color = None
    note = None

    def __init__(self, label = "Node", icon = None, 
                 priority = 1, color = None, note = "" ):

        # set the id
        self.id = MindNode.next_id
        MindNode.next_id += 1
        
        # set relationships
        self.parent = None
        self.children = list()
        
        # set properties
        self.setProperties(label, icon, priority, color, note)
    
    def addChild(self, child):
        self.children.append(child)
        child.setParent(self)
        
    def deleteChild(self, child):
        if self.children.count(child) > 0 :
            self.children.remove(child)
        
    def getChildren(self):
        return self.children
    
    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent
    
    def setProperties(self, label, icon, priority, color, note):
        self.label = label
        self.icon = icon
        self.priority = priority
        self.color = color
        self.note = note
        
    def getProperties(self):
        return (self.label, self.icon, self.priority, self.color, self.note)
        
    def getId(self):
        return self.id

    def getLabel(self):
        return self.label
    
    def setLabel(self, label):
        self.label = label
    
    def getPriority(self):
        return self.priority
    
    def setPriority(self, priority):
        self.priority = priority
    
    def getColor(self):
        return self.color
    
    def getIcon(self):
        return self.icon
    
    def setColor(self, color):
        self.color = color
        
    def setIcon(self, icon):
        self.icon = icon
        
    def getNote(self):
        return self.note
    
    def setNote(self, note):
        self.note = note

    
