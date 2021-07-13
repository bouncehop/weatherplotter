# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrmMain
###########################################################################

class FrmMain ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Weather Plotter", pos = wx.DefaultPosition, size = wx.Size( 284,439 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizerFrameMain = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel4 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        m_choiceChoices = [ u"Update", u"Download All" ]
        self.m_choice = wx.Choice( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceChoices, 0 )
        self.m_choice.SetSelection( 0 )
        bSizer2.Add( self.m_choice, 0, wx.ALL, 5 )

        self.btn_dl = wx.Button( self.m_panel4, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btn_dl, 0, wx.ALL, 5 )


        self.m_panel4.SetSizer( bSizer2 )
        self.m_panel4.Layout()
        bSizer2.Fit( self.m_panel4 )
        self.m_notebook3.AddPage( self.m_panel4, u"Data", True )
        self.m_panel5 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Yearly Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Start Year (YYYY):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.txt_startyear = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.txt_startyear, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"End Year (YYYY):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.txt_endyear = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.txt_endyear, 0, wx.ALL, 5 )

        self.btn_yearly = wx.Button( self.m_panel5, wx.ID_ANY, u"Plot Yearly Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btn_yearly, 0, wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText7 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Daily Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer6.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Year (YYYY):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.txt_year = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txt_year, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Month (MM):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer6.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.txt_month = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txt_month, 0, wx.ALL, 5 )

        self.btn_daily = wx.Button( self.m_panel5, wx.ID_ANY, u"Plot Daily Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn_daily, 0, wx.ALL, 5 )


        bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )


        self.m_panel5.SetSizer( bSizer5 )
        self.m_panel5.Layout()
        bSizer5.Fit( self.m_panel5 )
        self.m_notebook3.AddPage( self.m_panel5, u"Graph", False )

        bSizerFrameMain.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizerFrameMain )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btn_dl.Bind( wx.EVT_BUTTON, self.onStartClick )
        self.btn_yearly.Bind( wx.EVT_BUTTON, self.onYearlyClick )
        self.btn_daily.Bind( wx.EVT_BUTTON, self.onDailyClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onStartClick( self, event ):
        event.Skip()

    def onYearlyClick( self, event ):
        event.Skip()

    def onDailyClick( self, event ):
        event.Skip()


