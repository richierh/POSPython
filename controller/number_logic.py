import wx

class Number():

    def __init__(self,parent):
        self.parent = parent

        self.parent.m_button7.Bind(wx.EVT_BUTTON,self.number7click)
        self.parent.m_button8.Bind(wx.EVT_BUTTON,self.number8click)
        self.parent.m_button9.Bind(wx.EVT_BUTTON,self.number9click)
        self.parent.m_button10.Bind(wx.EVT_BUTTON,self.number4click)
        self.parent.m_button11.Bind(wx.EVT_BUTTON,self.number5click)
        self.parent.m_button12.Bind(wx.EVT_BUTTON,self.number6click)
        self.parent.m_button13.Bind(wx.EVT_BUTTON,self.number1click)
        self.parent.m_button14.Bind(wx.EVT_BUTTON,self.number2click)
        self.parent.m_button15.Bind(wx.EVT_BUTTON,self.number3click)
        self.parent.m_button16.Bind(wx.EVT_BUTTON,self.number00click)
        self.parent.m_button17.Bind(wx.EVT_BUTTON,self.number0click)
        self.parent.m_button18.Bind(wx.EVT_BUTTON,self.number000click)
    
    
    def number0click(self,event):
        print ("number 0")
    
    def number00click(self,event):
        print ("number 00")

    def number000click(self,event):
        print ("number 000")

    def number7click(self,event):
        print ("okay")

    def number8click(self,event):
        print ("number8")
    
    def number9click(self,event):
        print("number 9")

    def number1click(self,event):
        print("number1")
    
    def number2click(self,event):
        print("number 2")
    
    def number3click(self,event):
        print("number 3")
        
    def number4click(self,event):
        print("number 4")

    def number5click(self,event):
        print("number 5")
        
    def number6click(self,event):
        print ("number 6")
        
    def number7click(self,event):
        print ("number 7")