'''
Created on 30.11.2012

@author: Vendula Poncova
'''

from neuron.lib.colors import MapColor
from neuron.mindmap.controler import MapControler
from neuron.mindmap.model import MindNode
import wx

def test5(canvas):        
    mmap = MapControler(canvas)
           
    n1 = MindNode(label = "My Live", color = MapColor.random())
    n2 = MindNode(label = "Family", color = MapColor.random())
    n3 = MindNode(label = "Hobbies", color = MapColor.random())
    n4 = MindNode(label = "Holiday", color = MapColor.random())
    n5 = MindNode(label = "USA", color =MapColor.random())
    n6 = MindNode(label = "Starbucks", color = MapColor.random())

    
    mmap.addNode(None, n1)
    mmap.addNode(n1, n2)
    mmap.addNode(n1, n3)
    mmap.addNode(n1, n4)
    mmap.addNode(n1, n5)
    mmap.addNode(n1, n6)
    
    mmap.showView(n1)       
    return mmap

def test4(canvas):        
    mmap = MapControler(canvas)
           
    n1 = MindNode(label = "My Live", color = wx.Colour(153, 102, 153, 255), priority = 2)
    n2 = MindNode(label = "Family", color = wx.Colour(51, 128, 204, 255))
    n3 = MindNode(label = "Hobbies", color = wx.Colour(255, 209, 71, 255))
    n4 = MindNode(label = "Holiday", color = wx.Colour(255, 0, 71, 255), priority = 0)
    n5 = MindNode(label = "USA", color = wx.Colour(0, 123, 123, 255), priority = 2)
    n6 = MindNode(label = "Silene dlouhy krutoprisny nazev", color = wx.Colour(0, 123, 0, 255))

    
    mmap.addNode(None, n1)
    mmap.addNode(n1, n2)
    mmap.addNode(n2, n3)
    mmap.addNode(n3, n4)
    mmap.addNode(n3, n5)
    mmap.addNode(n2, n6)
    
    n2.setNote("Tato poznamka je na druhou stranu mnohem zajimavejsi, nebot nevypovida vubec o nicem. Tohle tvrzeni zakladam an domenkach, ze:\n\n1.nic jste se nedozvedeli\n2.nebylo ucelem vam neco sdelit")
    n3.setNote("Tohle je nejaka velmi zajimava a uzitecna poznamka o nesmrtelnosti brouka. Kdyz se tak zamyslime, brouk prece nemuze byt nesmrtelny, to je pekna blbost.")
    
    mmap.showView(n2)
    return mmap

def test3(canvas):        
    mmap = MapControler(canvas)
           
    n1 = MindNode(label = "My Live", color = wx.Colour(153, 102, 153, 255), priority = 2)
    n2 = MindNode(label = "Family", color = wx.Colour(51, 128, 204, 255))
    n3 = MindNode(label = "Hobbies", color = wx.Colour(255, 209, 71, 255))
    n4 = MindNode(label = "Holiday", color = wx.Colour(255, 0, 71, 255), priority = 0)
    n5 = MindNode(label = "USA", color = wx.Colour(0, 123, 123, 255), priority = 2)
    n6 = MindNode(label = "Silene dlouhy krutoprisny nazev", color = wx.Colour(0, 123, 0, 255))

    
    mmap.addNode(None, n1)
    mmap.addNode(n1, n2)
    mmap.addNode(n2, n3)
    mmap.addNode(n3, n4)
    mmap.addNode(n3, n5)
    mmap.addNode(n2, n6)
    
    mmap.showView(n2)
    return mmap

def test2(canvas):        
    mmap = MapControler(canvas)
           
    n1 = MindNode(label = "My Live", color = wx.Colour(153, 102, 153, 255))
    n2 = MindNode(label = "Family", color = wx.Colour(51, 128, 204, 255))
    n3 = MindNode(label = "Hobbies", color = wx.Colour(255, 209, 71, 255))
    n4 = MindNode(label = "Holiday", color = wx.Colour(255, 0, 71, 255))
    n5 = MindNode(label = "USA", color = wx.Colour(0, 123, 123, 255))
    n6 = MindNode(label = "Starbucks", color = wx.Colour(0, 123, 0, 255))

    
    mmap.addNode(None, n1)
    mmap.addNode(n1, n2)
    mmap.addNode(n2, n3)
    mmap.addNode(n3, n4)
    mmap.addNode(n3, n5)
    mmap.addNode(n2, n6)
    
    mmap.showView(n1)
    return mmap

    
def test1(canvas):        
    mmap = MapControler(canvas)
           
    n1 = MindNode(label = "My Live", color = wx.Colour(153, 102, 153, 255))
    n2 = MindNode(label = "Family", color = wx.Colour(51, 128, 204, 255))
    n3 = MindNode(label = "Hobbies", color = wx.Colour(255, 209, 71, 255))
    n4 = MindNode(label = "Holiday", color = wx.Colour(255, 0, 71, 255))
    n5 = MindNode(label = "USA", color = wx.Colour(0, 123, 123, 255))
    n6 = MindNode(label = "Starbucks", color = wx.Colour(0, 123, 0, 255))

    
    mmap.addNode(None, n1)
    mmap.addNode(n1, n2)
    mmap.addNode(n1, n3)
    mmap.addNode(n1, n4)
    mmap.addNode(n1, n5)
    mmap.addNode(n1, n6)
    
    mmap.showView(n1)       
    return mmap

def test0(canvas):        
    mmap = MapControler(canvas)
           
    n1 = MindNode(label = "My Live", color = wx.Colour(153, 102, 153, 255))       
    mmap.addNode(None, n1)
    
    mmap.showView(n1)
    return mmap
