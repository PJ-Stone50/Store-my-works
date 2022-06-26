import tkinter as tk
from tkinter import messagebox

def show_frame(frame):
  frame.tkraise()

def sayhi():
  messagebox.showinfo("Easter Egg1", "mypassword: Ok")

def addpage():
  messagebox.showinfo("Easter Egg1", "mypassword: Ok")

def deletepage():
  messagebox.showinfo("Easter Egg1", "mypassword: Ok")


window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

container_home = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

container_home.rowconfigure((0,4), weight=2)
container_home.rowconfigure((1,2,3), weight=1)
container_home.columnconfigure((0,1), weight=1)


for frame in (container_home, frame2, frame3):
  frame.grid(row=0, column=0, sticky='news')


# Homepage

# Left
template_btn = tk.Button(container_home,bg="lightgrey",text="Template",command=lambda:sayhi(),width=30,height=4)
template_btn.grid(row=1,column=0)

add_btn = tk.Button(container_home,bg="lightgrey",text="Add",width=30,height=4)
add_btn.grid(row=2,column=0)

delete_btn = tk.Button(container_home,bg="lightgrey",text="Delete",width=30,height=4)
delete_btn.grid(row=3,column=0)


# Right
searchbar = tk.Entry(container_home, text="frame1", bg="red")
searchbar.grid(row=0, column=1)

frame1_btn = tk.Button(container_home, text="Enter",command=lambda:show_frame(frame2),bg="red")
frame1_btn.grid(row=11, column=1, sticky='news')

















# Frame2
frame2_title = tk.Label(frame2, text="frame2", bg="orange")
frame2_title.pack(fill='x')

frame2_btn = tk.Button(frame2, text="Enter",command=lambda:show_frame(frame3),bg="red")
frame2_btn.pack()

# Frame3
frame3_title = tk.Label(frame3, text="frame3", bg="green")
frame3_title.pack(fill='x')

frame3_btn = tk.Button(frame3, text="Enter",command=lambda:show_frame(container_home),bg="red")
frame3_btn.pack()

show_frame(container_home)

window.mainloop()