import wx

data = [[1,2],[3,4]]

class App_(wx.App):
  def OnInit(self):
    self.Frame_ = Frame_(None, id=-1)
    self.SetTopWindow(self.Frame_)
    self.Frame_.Show(True)
    self.Frame_.Timer_.Start(milliseconds=50)
    return True

class Frame_(wx.Frame):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)
    self.List_ = List_(self, id=-1, style=wx.LC_REPORT|wx.LC_VIRTUAL)
    self.Timer_ = Timer_(self, id=-1)
  
  def re(self):
    self.List_.SetItemCount(len(data))

class List_(wx.ListCtrl):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)
    self.items = data
    self.SetBackgroundColour("#c8c8c8")
    self.InsertColumn(0, 'time')
    self.InsertColumn(1, 'id')
    self.SetItemCount(len(data))

  def OnGetItemText(self, item, column):
    items = (self.items[item][column])
    return str(items)
  
class Timer_(wx.Timer):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)
  
  def Notify(self):
    data[0][0] = data[0][0] + 1

def main():
  app = App_(False)
  app.MainLoop()

if __name__=="__main__":
  main()
