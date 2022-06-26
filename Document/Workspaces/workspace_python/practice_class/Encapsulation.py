from tkinter import*
from tkinter import messagebox


class OT:
  __rate = 300.0

  def getrate(self):
    return self.__rate

  def changerate(self, r):
    self.__rate = r

  def cal_ot(self,hour):
    return hour * self.__rate


class OTform:
  @staticmethod

  def myotform():
    root = Tk()
    root.title("Rate Overtime")
    root.geometry("300x200")

    app = Frame(root)
    app.grid()

    blanklabel1 = Label(app, font=("tahoma",'11'), width=35)
    blanklabel1.grid(col=0,row=0,columnspan=2)

    hrlabel = Label(app, font=('tahoma','11'),text="Hour", width=10, anchor=W)
    hrlabel.grid(col=0,row=1)
    hrtext = StringVar()
    hrentry = Entry(app, font=('tahoma',11),textvariable=hrtext,bd=2,width=15)
    hrentry.grid(col=1,row=1)


  def hentry_keypress(event):
    w = event.widget # ไม่เข้าใจ 1
    if float(w.get()) < 40:
      rateentry.configure(state=NORMAL)
      ratetext.set("")
      anslabel['text'] = ""
      rateentry.focus_set()

    else:
      rateentry.configure(state=DISABLED)
      ratetext.set('0.0')
      calbutton.focus_set()

    hrentry.bind('<Return>', hrentry_keypress)

    ratelabel = Label(app, font=("tahoma",'11'), text="ค่าแรงใหม่",width=10, anchor=W)
    ratelabel.grid(column=0,row=2)
    ratetext = StringVar()

    rateentry = Entry(app,font=("tahoma",'11'),textvariable=ratetext, state=DISABLED, bd=2 ,width=15)
    ratetext.set('0.0')
    rateentry.grid(column=1,row=2)

    def rateentry_keypress(event):
      w = event.widget # ไม่เข้าใจ 2

      if w.get() == "":
        messasgebox.showinfo("เกิดข้อผิดพลาด!",'ป้อนข้อมูลใหม่อีกครั้ง')
        w.focus_set()

      calbutton.focus_set()

      rateentry.bind("<Return>",rateentry_keypress)

      blanklabel3 = Label(app, width=35)
      blanklabel3.grid(column=0,row=3,columnspan=2)

      calbutton = Button(app,font=("tahoma",'11'),text="คำนวณ", width=10, command=lambda: setlogindata(loginbutton))
      calbutton.grid(column=0,row=4)

      def calbutton_keypress(event):
        
       









root.mainloop()

ot_f = OTform()
ot_f.myotform()