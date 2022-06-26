import sqlite3
from tkinter import messagebox
from tkinter import *

def mainwindow() :
    global menubar
    root = Tk()
    w = 1000
    h = 600
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#28527a')
    #root.config(bg='#4a3933')
    root.title("Login/Register Application: ")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,1,2),weight=1)
    root.columnconfigure((0,1,2),weight=1)
    menubar = Menu(root)
    menubar.add_command(label="Logout",command=logoutClick)
    menubar.add_command(label="Exit",command=root.quit)
    return root

# C:\\Users\\Admin\\Desktop\\Lab8_A.moo_week10\\week10_1630708350.db
def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('C:\\Users\\Admin\\Desktop\\Lab8_A.moo_week10\\DB\\week10_1630708350.db')
    cursor = conn.cursor()

def loginlayout() :
    global userentry
    global pwdentry
    global loginframe
    
    loginframe = Frame(root,bg='#709fb0')
    loginframe.grid(row=1,column=1,sticky='news')
    loginframe.rowconfigure((0,1,2),weight=1)
    loginframe.columnconfigure((0,1,2),weight=1)
    root.title("Login")
    emptyMenu = Menu(root) #create empty menu
    root.config(bg='lightblue',menu=emptyMenu) #change root menu to  empty menu   
    
    Label(loginframe,text="Login/Register Application",font="Calibri 26 bold",image=img1,compound=LEFT,bg='#709fb0',fg='#e4fbff').grid(row=0,columnspan=2)
    Label(loginframe,text="User name : ",bg='#709fb0',fg='#e4fbff',padx=20).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e4fbff',width=20,textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e4fbff',width=20,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='#709fb0',fg='#e4fbff').grid(row=2,column=0,padx=20,sticky='e')
    # ปุ่ม Login
    Button(loginframe,text="Login",width=10,command=loginclick).grid(row=3,column=0,columnspan=2)
    #Button(loginframe,text="Register",width=10).grid(row=3,column=1,pady=20,ipady=15,sticky='w',padx=20)

def loginclick() :
    #profilewindow('temp value')
    #print("Hello from loginclick")
    if userinfo.get() == "" :
        messagebox.showwarning("Admin : ","Enter Username and try again")
        userentry.focus_force()
    elif pwdinfo.get() == "" :
        messagebox.showwarning("Admin : ","Enter Password and try again")
        userentry.focus_force()
    else :
        sql = "SELECT * FROM student WHERE USERNAME=?"
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            # Check Password
            sql = "SELECT * FROM student WHERE USERNAME=? AND PASSWORD=?"
            cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
            result = cursor.fetchall()
            if result :
                messagebox.showinfo("Admin : ","Login Successfully")
                profilewindow(userinfo.get())
            else :
                messagebox.showwarning("Admin : ","Incorrect username or password")
                pwdentry.select_range(0,END)
                pwdentry.focus_force()

def profilewindow(user) :
    global profileframe  
    loginframe.destroy()
    
    root.title("Welcome : "+user)
    root.config(bg='lightblue',menu=menubar) #Add menubar to root menu 
    profileframe = Frame(root, bg='skyblue')
    profileframe.grid(row=0,column=0,columnspan=3,rowspan=3,sticky='news')
    profileframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    profileframe.columnconfigure((0,1,2),weight=1)
   # profileframe.option_add('*bg','lightblue')
  #  profileframe.columnconfigure(1,weight=0)

    # db field user | pwd | fname | lname
    sql_student = "SELECT * FROM student WHERE USERNAME=?"
    cursor.execute(sql_student,[user])
    result_stu = cursor.fetchone()

    Label(profileframe,image=img1,bg='skyblue').grid(row=0,column=1)
    Label(profileframe,text="Student ID         "+ str(result_stu[0]),bg='skyblue').grid(row=1,column=1,padx=5,pady=5)
    Label(profileframe,text="Name         "+ str(result_stu[4]),bg='skyblue').grid(row=2,column=1)
    Label(profileframe,text="Score         "+ str(result_stu[3]),bg='skyblue').grid(row=3,column=1)
    

    if result_stu[3] >= 80 :
        Label(profileframe,text="Grade         "+ 'A',bg='skyblue').grid(row=4,column=1)
    elif result_stu[3] >= 70 :
        Label(profileframe,text="Grade         "+ 'B',bg='skyblue').grid(row=4,column=1)
    elif result_stu[3] >= 60 :
        Label(profileframe,text="Grade         "+ 'C',bg='skyblue').grid(row=4,column=1)
    elif result_stu[3] >= 50 :
        Label(profileframe,text="Grade         "+ 'D',bg='skyblue').grid(row=4,column=1)
    elif result_stu[3] < 50 :
        Label(profileframe,text="Grade         "+ 'F',bg='skyblue').grid(row=4,column=1)
    else :
        print("ERROR")

    # Add picture into profilewindow()
    

    Button(profileframe,text="Logout",command=logoutClick).grid(row=6,column=1)        # Button Logout
    
    #profileframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    

def logoutClick() :
    profileframe.destroy()
    loginlayout() #Show login


createconnection()
root = mainwindow()

userinfo = StringVar()
pwdinfo = StringVar()

img1 = PhotoImage(file='images/profile.png').subsample(2,2)
loginlayout()
newuserinfo = StringVar()
newpwdinfo = StringVar()
cfinfo = StringVar()
fname = StringVar()
lname = StringVar()

root.mainloop()
#cursor.close()
#conn.close()

