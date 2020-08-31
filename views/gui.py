# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jul 26 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from wx.lib.intctrl import IntCtrl
import wx.html

ID_KELUAR = 1000

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer3 = wx.FlexGridSizer( 6, 1, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.AddGrowableRow( 0 )
		fgSizer3.AddGrowableRow( 1 )
		fgSizer3.AddGrowableRow( 2 )
		fgSizer3.AddGrowableRow( 3 )
		fgSizer3.AddGrowableRow( 4 )
		fgSizer3.AddGrowableRow( 5 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,300 ), 0 )
		self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn4 = self.m_dataViewListCtrl1.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		fgSizer3.Add( self.m_dataViewListCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button3, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button4 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button4, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button5, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button6, 1, wx.ALL|wx.EXPAND, 5 )


		fgSizer3.Add( gSizer1, 3, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_intctrl=IntCtrl(self.m_panel1, wx.ID_ANY,0 )
		self.m_intctrl.SetFont( wx.Font( 26, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer3.Add( self.m_intctrl, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		gSizer2 = wx.GridSizer( 4, 3, 0, 0 )

		self.m_button7 = wx.Button( self.m_panel1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button7.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button7, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button8 = wx.Button( self.m_panel1, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button8.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button8, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button9 = wx.Button( self.m_panel1, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button9.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button9, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button10 = wx.Button( self.m_panel1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button10.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button10, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self.m_panel1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button11.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button11, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button12 = wx.Button( self.m_panel1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button12.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button12, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self.m_panel1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button13.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button13, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button14 = wx.Button( self.m_panel1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button14.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button14, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button15 = wx.Button( self.m_panel1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button15.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button15, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button16 = wx.Button( self.m_panel1, wx.ID_ANY, u"00", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button16.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button16, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button17 = wx.Button( self.m_panel1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button17.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button17, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self.m_panel1, wx.ID_ANY, u"000", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button18.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		gSizer2.Add( self.m_button18, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer41.Add( gSizer2, 3, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 5, 0, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.AddGrowableRow( 1 )
		fgSizer4.AddGrowableRow( 2 )
		fgSizer4.AddGrowableRow( 3 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button19 = wx.Button( self.m_panel1, wx.ID_ANY, u"x", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_button19.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.m_button19, 3, wx.ALL|wx.EXPAND, 5 )

		self.m_button21 = wx.Button( self.m_panel1, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_button21.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.m_button21, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button22 = wx.Button( self.m_panel1, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_button22.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.m_button22, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button20 = wx.Button( self.m_panel1, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_button20.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.m_button20, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button23 = wx.Button( self.m_panel1, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		self.m_button23.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.m_button23, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer41.Add( fgSizer4, 1, wx.EXPAND, 5 )


		fgSizer3.Add( bSizer41, 1, wx.EXPAND, 5 )


		bSizer4.Add( fgSizer3, 3, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_searchCtrl1 = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer5.Add( self.m_searchCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_dataViewCtrl1 = wx.dataview.DataViewCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewColumn1 = self.m_dataViewCtrl1.AppendTextColumn( u"Name", 0, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewColumn2 = self.m_dataViewCtrl1.AppendTextColumn( u"Name", 0, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewColumn3 = self.m_dataViewCtrl1.AppendTextColumn( u"Name", 0, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer5.Add( self.m_dataViewCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_dataViewListCtrl2 = wx.dataview.DataViewListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn5 = self.m_dataViewListCtrl2.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn6 = self.m_dataViewListCtrl2.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn7 = self.m_dataViewListCtrl2.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer5.Add( self.m_dataViewListCtrl2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_htmlWin1 = wx.html.HtmlWindow( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
		bSizer5.Add( self.m_htmlWin1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer5, 5, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer2.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.berkas = wx.Menu()
		self.keluar = wx.MenuItem( self.berkas, ID_KELUAR, u"Keluar", wx.EmptyString, wx.ITEM_NORMAL )
		self.berkas.Append( self.keluar )

		self.m_menubar1.Append( self.berkas, u"Berkas" )

		self.pengaturan = wx.Menu()
		self.m_menubar1.Append( self.pengaturan, u"Pengaturan" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button17.Bind( wx.EVT_KEY_DOWN, self.tekan0 )
		self.Bind( wx.EVT_MENU, self.Keluar, id = self.keluar.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tekan0( self, event ):
		event.Skip()

	def Keluar( self, event ):
		event.Skip()


