import wx
import os
class MainWindow():


    def __init__(self,parent):
        self.parent = parent
        self.parent.thumbnail.ShowDir("/home/pmc/Projects/POSPython/testing/")
        self.parent.thumbnail.ShowFileNames(False)



class AddText(wx.Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.data = os.listdir(os.getcwd())

        location = "/home/pmc/Projects/POSPython/testing/download.jpeg"

        bitmap = wx.Bitmap(location)
        dc = wx.MemoryDC(bitmap)
        text = 'whatever'
        w, h = dc.GetSize()
        tw, th = dc.GetTextExtent(text)
        dc.DrawText(text, (w - tw)/2, (h - th)) #display text in center
        print (w,h)
        print(tw,th)
        del dc

        control = wx.StaticBitmap(self, -1, bitmap)

if __name__=="__main__":
    run = wx.App()
    go = AddText(None)
    go.Show()
    run.MainLoop()