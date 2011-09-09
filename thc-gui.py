#!/usr/bin/python

# panels.py

import wx


class Panels(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
		
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        splitter = wx.SplitterWindow(self, -1)
        hashtag = '#wineparty'

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        panel1 = wx.Panel(splitter, -1)
        panel11 = wx.Panel(panel1, -1, size=(-1, 40))
        panel11.SetBackgroundColour('#53728c')
        st1 = wx.StaticText(panel11, -1, hashtag, (5, 5))
        st1.SetForegroundColour('WHITE')

        panel12 = wx.Panel(panel1, -1, style=wx.BORDER_SUNKEN)
        panel12.SetBackgroundColour('WHITE')

        vbox1.Add(panel11, 0, wx.EXPAND)
        vbox1.Add(panel12, 1, wx.EXPAND)

        panel1.SetSizer(vbox1)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        panel2 = wx.Panel(splitter, -1)
        panel21 = wx.Panel(panel2, -1, size=(-1, 40), style=wx.NO_BORDER)
        st2 = wx.StaticText(panel21, -1, 'Users in Chat', (5, 5))
        st2.SetForegroundColour('WHITE')

        panel21.SetBackgroundColour('#53728c')
        panel22 = wx.Panel(panel2, -1, style=wx.BORDER_RAISED)

        panel22.SetBackgroundColour('WHITE')
        vbox2.Add(panel21, 0, wx.EXPAND)
        vbox2.Add(panel22, 1, wx.EXPAND)

        panel2.SetSizer(vbox2)

        menubar = wx.MenuBar()
        settings = wx.Menu()
        settings.Append(-1, '&Hashtag')
        settings.AppendSeparator()
        settings.Append(-1, '&Update interval')
        settings.Append(-1, '&Keep history for...')
        settings.Append(-1, '&Define "in chat" timer')
        settings.AppendSeparator()
        settings.Append(-1, '&Clear history')
        menubar.Append(settings, '&Settings')
        self.SetMenuBar(menubar)

        hbox.Add(splitter, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        self.SetSizer(hbox)
        self.CreateStatusBar()
        splitter.SplitVertically(panel1, panel2)
        self.Centre()
        self.Show(True)


    def ExitApp(self, event):
        self.Close()


app = wx.App(redirect=True,filename="mylogfile.txt")
Panels(None, -1, 'Twitter Hashtag Chat')
app.MainLoop()