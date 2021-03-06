#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Dmitriy Bryndin
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.4 on Mon Jan 30 15:48:02 2006

import wx

class InsertRowsDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: InsertRowsDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.Rows = wx.StaticText(self, -1, "Rows:")
        self.spin_ctrl_Rows = wx.SpinCtrl(self, -1, "1", min=0, max=100)
        self.radio_box_where = wx.RadioBox(self, -1, "", choices=["Above", "Below"], majorDimension=2, style=wx.RA_SPECIFY_ROWS)
        self.button_OK = wx.Button(self, wx.ID_OK, "OK")
        self.button_Cancel = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: InsertRowsDialog.__set_properties
        self.SetTitle("InsertRows")
        self.radio_box_where.SetSelection(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: InsertRowsDialog.__do_layout
        sizer_horiz = wx.BoxSizer(wx.HORIZONTAL)
        sizer_right_vert = wx.BoxSizer(wx.VERTICAL)
        sizer_left_vert = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.Rows, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.spin_ctrl_Rows, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_left_vert.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_left_vert.Add(self.radio_box_where, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        sizer_horiz.Add(sizer_left_vert, 0, wx.EXPAND, 0)
        sizer_right_vert.Add(self.button_OK, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_right_vert.Add(self.button_Cancel, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_horiz.Add(sizer_right_vert, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_horiz)
        sizer_horiz.Fit(self)
        sizer_horiz.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class InsertRowsDialog
