import wx

data = [[1,2],[3,4]]

class App_(wx.App):
  def OnInit(self):
    self.Frame_ = Frame_(None)
    self.SetTopWindow(self.Frame_)
    self.Frame_.Show(True)
    return True

class Frame_(wx.Frame):
  def __init__(self, parent):
    super().__init__(parent, id=-1)
    self.List_ = List_(self)
    self.timer = Timer_(self)
    self.Bind(wx.EVT_TIMER, self.redraw, self.timer)
    self.timer.Start(20)

  def redraw(self, event):
    data[0][0] = data[0][0] + 1
    wx.ListCtrl.Refresh(self.List_)

class List_(wx.ListCtrl):
  def __init__(self, parent):
    super().__init__(parent, id=-1, style=wx.LC_REPORT|wx.LC_VIRTUAL)
    self.items = data
    self.SetBackgroundColour("#c8c8c8")
    self.InsertColumn(0, 'time')
    self.InsertColumn(1, 'id')
    self.SetItemCount(len(data))

  def OnGetItemText(self, item, column):
    items = (self.items[item][column])
    return str(items)

class Timer_(wx.Timer):
  def __init__(self, parent):
    super().__init__(parent, id=-1)    

def main():
  app = App_(False)
  app.MainLoop()

if __name__=="__main__":
  main()
