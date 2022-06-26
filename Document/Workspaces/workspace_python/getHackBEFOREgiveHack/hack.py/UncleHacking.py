from tkinter import *

# data members
font18 = ('Sprite Coder', 18, 'bold')
font24 = ('Sprite Coder', 24, 'bold')
font48 = ('Sprite Coder', 48, 'bold')
fontx = ('Public Sans', 10, 'bold')
fontcl = 'white'
width_cv = 400
height_cv = 300

fg='green'
bg='#191919'
WW = 1920
HH = 1080

def MainProgram():
    root = Tk()
    w = 1000
    h = 600

    
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2- h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#191919')
    #root.config(bg='#4a3933')
    root.title("Login/Register Application: ")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,1,2),weight=1)
    root.columnconfigure((0,1,2),weight=1)
    # Set FullScreen
    # root.state('zoomed')
    root.title("UncleHacking#")

    # root.attributes('-alpha',0.2)

    menubar = Menu(root)
    # menubar.add_command(label="Logout",command=logoutClick)
    # menubar.add_command(label="Exit",command=root.quit)
    
    return root

def Index():
    global font18,fontcl,canvas
    font188 = ('Sprite Coder', 24, 'bold')
    fontcl = 'white'

    homeframe = Frame(root,bg='#191919')
    homeframe.grid(row=1,column=1,sticky='news')
    homeframe.rowconfigure((0,1,2),weight=1)
    homeframe.columnconfigure((0,1,2),weight=1)

    Label(homeframe,text="Hello Tkinter hope to you again soon..",font=font188,fg='white',bg='#191919').grid(row=1,column=1)
    exit_button = Button(homeframe, text="Exit", command=root.destroy)
    exit_button.grid(row=2,column=2)

    #Canvas ลองใช้ canvas ทำเป็น frame เหมือนเกมงู
    

    canvas = Canvas(root,width=WW,height=HH,bd=1,relief='ridge',highlightthickness=0,bg=bg)
    canvas.place(x=0,y=0)

 
#Methods
def Fullscreen(event):
    root.attributes('-fullscreen',True)

def ExitFullscreen(event):
    root.attributes('-exitfullscreen',True)

def Disappear(event):
    root.attributes('-alpha',0)

def Jookroo(event):
    root.attributes('-alpha',1)

def CloseWindow(event):
    root.destroy()



def MyFrame(x,y,width=300,height=100):
    frame1 = canvas.create_rectangle(0,0,width,height, fill=bg,outline=fg, width=2)
    canvas.move(frame1,x,y)

def HeadFrame(x,y,width=300,height=100):
    frame1 = canvas.create_rectangle(0,0,width,height, fill='green',outline=fg, width=2)
    canvas.move(frame1,x,y)

def FixedLabel(text="This is text",x=50, y=50, font='font18', color=fontcl):
    L1 = Label(root, text=text, font=font, bg='green', fg='white')
    L1.place(x=x, y=y)

def FleLabixed(text="This is text",x=50, y=50, font='font18', color=fontcl):
    L1 = Label(root, text=text, font=font, bg='#191919', fg='white')
    L1.place(x=x, y=y)


def FixedLabelCloseWin(text="This is text",x=50, y=50, font='font18', color=fontcl):
    L1 = Label(root, text=text, font=font, bg='green', fg='black')
    L1.place(x=x, y=y)




root = MainProgram()
Index()

root.bind('<F11>',Fullscreen,False)
root.bind('<F12>',ExitFullscreen)
root.bind('<F10>',Disappear)
root.bind('<F9>',Jookroo)
root.bind('<Escape>',CloseWindow)
# root.bind('<F6>', Lambda event: root.attributes('-fullscreen',False))


# Check Stock

MyFrame(20, 20, 400, 300)
FixedLabel('THAI STOCK', 40, 40,font=font18)
FixedLabelCloseWin('X',410,40,font=fontx)

v_stockname = StringVar() #StringVar ตัวแปรสำหรับใช้กับ GUI

E1 = Entry(root,width=10,textvariable=v_stockname,font=font18,bg=bg,fg=fg)
E1.configure(insertbackground=fg)
E1.configure(highlightthickness=1)
E1.place(x=60,y=90)

v_result = StringVar()
LResult = Label(root, textvariable=v_result, font=font18, bg=bg, fg=fg, justify=LEFT)
LResult.place(x=60,y=140)

MyFrame(25, 25, 400, 300)
MyFrame(30, 30, 400, 300)
HeadFrame(35, 35, 400, 300)
MyFrame(35, 70, 400, 265)




# Stock Market
MyFrame(500,20,400,300)
FixedLabel('STOCK MARKET',520,40,font=font18)
MyFrame(1000,180,900,150)

FleLabixed('BTC :       +11.28%',540,80,font=font18)
FleLabixed('ADA :       -32.41%',540,120,font=font18)
FleLabixed('DOGE :     +66.88%',540,160,font=font18)
FleLabixed('BNB :       -55.55%',540,200,font=font18)
FleLabixed('ETH :       +0.00%',540,240,font=font18)



# # Remote1
# MyFrame(20,400,900,450)
# img1 = PhotoImage(file="C://Users//Admin//Desktop//workspace_python//getHackBEFOREgiveHack//hack.py//3.png")      
# canvas.create_image(20,400, anchor=NW, image=img1)   


# # Remote2
# MyFrame(1000,400,900,450)
# MyFrame(505,25,400,300)
# MyFrame(510,30,400,300)
# img2 = PhotoImage(file="C://Users//Admin//Desktop//workspace_python//getHackBEFOREgiveHack//hack.py//4.png")      
# canvas.create_image(1000,400, anchor=NW, image=img2) 

MyFrame(20,400,500,215)
img1 = PhotoImage(file="C://Users//Admin//Desktop//workspace_python//getHackBEFOREgiveHack//hack.py//5.png")  
canvas.create_image(20,400, anchor=NW, image=img1)  

MyFrame(600,400,500,310)
img2 = PhotoImage(file="C://Users//Admin//Desktop//workspace_python//getHackBEFOREgiveHack//hack.py//6.png")  
canvas.create_image(600,400, anchor=NW, image=img2)  

Label(root,text="My Program",font=font48,bg='#191919',fg='white').place(x=1200,y=20)



from uncleengineer import thaistock
## Get and print value into console
def CheckStockPrice(event):
    stockname = v_stockname.get()
    print(stockname)
    result = thaistock(stockname)
    text = 'STOCK: {}\nPRICE: {}'.format(result[0],result[1])
    v_result.set(text)

E1.bind('<Return>',CheckStockPrice)

root.mainloop()