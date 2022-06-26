from tkinter import*

def main():
  root = Tk()
  window1 = Window(root, "Class", '400x500', "Hi user, this is my first time I'm playing with class in here!")
  return None

def window2():
  root = Tk()
  window2 = Window(root, "Class", '400x600', "Window2")
  Label(root,text="เดี๋ยวกลับมาฝึกต่อนะ ตอนนี้ class คือไรยังงงอยู๋").pack()
  return None

class Window:
  n = 0

  def __init__(self,root,title,geometry,message):
    self.root = root
    self.root.title(title)
    self.root.geometry(geometry)
    Label(self.root, text=message).pack()
    button1 = Button(self.root, text="Increment", command=self.increment)
    button1.pack()
    self.root.mainloop()
    pass

  def increment(self):

    window2()
    return None

  pass

main()
