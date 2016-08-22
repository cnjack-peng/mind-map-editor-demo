# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Neuron", pos = wx.DefaultPosition, size = wx.Size( 650,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 400,300 ), wx.DefaultSize )
		
		self.menuBar = wx.MenuBar( 0 )
		self.m_menu4 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"New Map"+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItem3 )
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Open"+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem31 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItem31 )
		
		self.m_menuItem41 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Save As"+ u"\t" + u"Shift+Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItem41 )
		
		self.m_menu4.AppendSeparator()
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Print"+ u"\t" + u"Ctrl+P", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItem5 )
		
		self.m_menu4.AppendSeparator()
		
		self.m_menuItem6 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Exit"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItem6 )
		
		self.menuBar.Append( self.m_menu4, u"File" ) 
		
		self.m_menu5 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Undo"+ u"\t" + u"Ctrl+Z", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem7 )
		
		self.m_menuItem8 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Redo"+ u"\t" + u"Ctrl+Y", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem8 )
		
		self.m_menu5.AppendSeparator()
		
		self.m_menuItem9 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Copy"+ u"\t" + u"Ctrl+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem9 )
		
		self.m_menu5.AppendSeparator()
		
		self.m_menuItem10 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Align Nodes"+ u"\t" + u"Ctrl+A", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem10 )
		
		self.m_menu5.AppendSeparator()
		
		self.m_menuItem11 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Delete All"+ u"\t" + u"Ctrl+D", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.m_menuItem11 )
		
		self.menuBar.Append( self.m_menu5, u"Edit" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem12 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem12 )
		
		self.m_menuItem13 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Higher", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem13 )
		
		self.m_menu3.AppendSeparator()
		
		self.m_menuItem14 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Zoom In"+ u"\t" + u"Ctrl++", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem14 )
		
		self.m_menuItem15 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Zoom Out"+ u"\t" + u"Ctrl+-", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem15 )
		
		self.menuBar.Append( self.m_menu3, u"View" ) 
		
		self.m_menu41 = wx.Menu()
		self.m_menuItem16 = wx.MenuItem( self.m_menu41, wx.ID_ANY, u"Help"+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu41.AppendItem( self.m_menuItem16 )
		
		self.m_menu41.AppendSeparator()
		
		self.m_menuItem17 = wx.MenuItem( self.m_menu41, wx.ID_ANY, u"About Neuron", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu41.AppendItem( self.m_menuItem17 )
		
		self.menuBar.Append( self.m_menu41, u"Help" ) 
		
		self.SetMenuBar( self.menuBar )
		
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter2.SetSashGravity( 0 )
		self.m_splitter2.SetSashSize( 1 )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		self.m_splitter2.SetMinimumPaneSize( 160 )
		
		self.m_panel3 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook2 = wx.Notebook( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.treePanel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer6 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.treeScrolledWindow = wx.ScrolledWindow( self.treePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.treeScrolledWindow.SetScrollRate( 5, 5 )
		gSizer6.Add( self.treeScrolledWindow, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.treePanel.SetSizer( gSizer6 )
		self.treePanel.Layout()
		gSizer6.Fit( self.treePanel )
		self.m_notebook2.AddPage( self.treePanel, u"Map", False )
		self.nodePanel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.m_scrolledWindow5 = wx.ScrolledWindow( self.nodePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		fgSizer7 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.nodeName = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.nodeName, 0, wx.EXPAND|wx.ALL, 5 )
		
		fgSizer7.Add( bSizer8, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer7.Add( self.m_staticline6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer3.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.colourChoice = wx.ColourPickerCtrl( self.m_scrolledWindow5, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		fgSizer3.Add( self.colourChoice, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Icon:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer3.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.iconChoice = wx.FilePickerCtrl( self.m_scrolledWindow5, wx.ID_ANY, wx.EmptyString, u"Select an icon", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fgSizer3.Add( self.iconChoice, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Priority:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer3.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		priorityChoiceChoices = []
		self.priorityChoice = wx.Choice( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, priorityChoiceChoices, 0 )
		self.priorityChoice.SetSelection( 0 )
		fgSizer3.Add( self.priorityChoice, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT, 5 )
		
		fgSizer7.Add( fgSizer3, 5, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer7.Add( self.m_staticline7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer152.SetMinSize( wx.Size( -1,180 ) ) 
		self.m_staticText12 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Note:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer152.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_scrolledWindow82 = wx.ScrolledWindow( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow82.SetScrollRate( 5, 5 )
		gSizer102 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.nodeNote = wx.richtext.RichTextCtrl( self.m_scrolledWindow82, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gSizer102.Add( self.nodeNote, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_scrolledWindow82.SetSizer( gSizer102 )
		self.m_scrolledWindow82.Layout()
		gSizer102.Fit( self.m_scrolledWindow82 )
		bSizer152.Add( self.m_scrolledWindow82, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer7.Add( bSizer152, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer7.Add( self.m_staticline3, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.applyButton = wx.Button( self.m_scrolledWindow5, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.applyButton, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.ALIGN_BOTTOM, 5 )
		
		self.m_scrolledWindow5.SetSizer( fgSizer7 )
		self.m_scrolledWindow5.Layout()
		fgSizer7.Fit( self.m_scrolledWindow5 )
		gSizer4.Add( self.m_scrolledWindow5, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.nodePanel.SetSizer( gSizer4 )
		self.nodePanel.Layout()
		gSizer4.Fit( self.nodePanel )
		self.m_notebook2.AddPage( self.nodePanel, u"Node", True )
		
		bSizer4.Add( self.m_notebook2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		self.m_panel4 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow6 = wx.ScrolledWindow( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow6.SetScrollRate( 5, 5 )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.toolBar = wx.ToolBar( self.m_scrolledWindow6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_NOICONS|wx.TB_TEXT ) 
		self.toolBar.AddLabelTool( wx.ID_ANY, u"Open", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, u"Open file", wx.EmptyString ) 
		self.toolBar.AddLabelTool( wx.ID_ANY, u"Save", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, u"Save file", wx.EmptyString ) 
		self.toolBar.AddSeparator()
		self.toolBar.AddLabelTool( wx.ID_ANY, u"Undo", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, u"Undo", wx.EmptyString ) 
		self.toolBar.AddLabelTool( wx.ID_ANY, u"Redo", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, u"Redo", wx.EmptyString ) 
		self.toolBar.AddSeparator()
		self.toolBar.AddLabelTool( wx.ID_ANY, u"Home", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, u"View Root Level", wx.EmptyString ) 
		self.toolBar.AddLabelTool( wx.ID_ANY, u"Higher", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, u"View Higher Level", wx.EmptyString ) 
		self.toolBar.AddSeparator()
		self.toolBar.AddLabelTool( wx.ID_ANY, u"+", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, u"Zoom In", wx.EmptyString ) 
		self.toolBar.AddLabelTool( wx.ID_ANY, u"-", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, u"Zoom Out", wx.EmptyString ) 
		self.toolBar.Realize()
		
		bSizer10.Add( self.toolBar, 0, wx.EXPAND, 5 )
		
		self.canvasPanel = wx.Panel( self.m_scrolledWindow6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.canvasPanel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer10.Add( self.canvasPanel, 1, wx.EXPAND, 5 )
		
		self.m_scrolledWindow6.SetSizer( bSizer10 )
		self.m_scrolledWindow6.Layout()
		bSizer10.Fit( self.m_scrolledWindow6 )
		bSizer9.Add( self.m_scrolledWindow6, 1, wx.EXPAND, 5 )
		
		self.m_panel4.SetSizer( bSizer9 )
		self.m_panel4.Layout()
		bSizer9.Fit( self.m_panel4 )
		self.m_splitter2.SplitVertically( self.m_panel3, self.m_panel4, 160 )
		bSizer3.Add( self.m_splitter2, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.applyButton.Bind( wx.EVT_BUTTON, self.changeNodeProperties )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def changeNodeProperties( self, event ):
		pass
	
	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 160 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )
	

