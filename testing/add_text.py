
import wx


class MyFrame(wx.Frame):


    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        location = "/home/pmc/Projects/POSPython/testing/download.jpeg"
        bitmap = wx.Bitmap(location)
        dc = wx.MemoryDC(bitmap)
        text = 'whatever'
        w, h = dc.GetSize()
        tw, th = dc.GetTextExtent(text)
        dc.DrawText(text, (w - tw)/2, (h - th)) #displ
        ay text in center
        print (w,h)
        print(tw,th)
        del dc

        control = wx.StaticBitmap(self, -1, bitmap)



if __name__=="__main__":
    run = wx.App()
    go = MyFrame(None).Show()
    run.MainLoop()