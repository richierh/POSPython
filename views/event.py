from views.gui import MyFrame1
import wx
from controller.number_logic import Number

class OpenWindows(MyFrame1):


    def __init__(self,parent,*args,**kwds):
        super().__init__(parent,*args,**kwds)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        # event for click button
        self.number = Number(self)

    def OnCloseWindow(self,event):

        if event.CanVeto() :#and self.fileNotSaved:

            if wx.MessageBox("Pastikan data sudah disimpan.... atau tetap tutup aplikasi? ","Please confirm",wx.ICON_QUESTION | wx.YES_NO) != wx.YES:

                event.Veto()
                return

        self.Destroy()  # you may also do:  event.Skip()
                        # since the default event handler does call Destroy(), too



    def tekan0(self,event):
        keycode = event.GetKeyCode()
        if keycode == ord('0'):
            print(keycode)
            self.number = 0

class RunApp(wx.App):
    def OnInit(self):
        self.Frame = OpenWindows(parent=None)
        self.Frame.Show()
        self.__properties()
        return True

    def __properties(self):
        self.Frame.Maximize()
        self.Frame.SetTitle("Point Of Sales Using Python")
        self.Frame.SetSize(800,600)
        self.SetTopWindow(self.Frame)
        self.Frame.Centre()
        self.Frame.Layout()
