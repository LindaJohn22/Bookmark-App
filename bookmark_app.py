import tkinter as tk
import webbrowser

def fb(event):
  webbrowser.open_new_tab('https://www.facebook.com/linda.john.526')
def quora(event):
  webbrowser.open_new_tab('https://www.quora.com/')
def insta(event):
  webbrowser.open_new_tab('https://www.instagram.com/')
def reddit(event):
  webbrowser.open_new_tab('https://www.reddit.com/')
def yt(event):
  webbrowser.open_new_tab('https://www.youtube.com/')
window=tk.Tk()
window.geometry("700x700")
window.title("Social Media Bookmark App")
label1=tk.Label(text="My Social Media",font=("Times new roman",20))
label1.grid(column=1,row=0)

canvas=tk.Canvas(window,width=650,height=470)
canvas.grid(column=1,row=1)
photo=tk.PhotoImage(file='D:\\Users\\jinojohn\\Desktop\\folder\\practice\\python\\bk\\sample.gif')
canvas.create_image(80,0,anchor='nw',image=photo)

label1=tk.Label(text="Click the buttons below to access the bookmarked social media pages")
label1.grid(column=1,row=2)


button1=tk.Button(window,text="Quora",bg="orange")
button1.grid(column=1,row=3)
button2=tk.Button(window,text="Facebook",bg="light blue")
button2.grid(column=1,row=7)
button3=tk.Button(window,text="Reddit",bg="light green")
button3.grid(column=1,row=4)
button4=tk.Button(window,text="Instagram",bg="pink")
button4.grid(column=1,row=6)
button5=tk.Button(window,text="Youtube",bg="red")
button5.grid(column=1,row=5)
button1.bind("<Button-1>",quora)
button2.bind("<Button-1>",fb)
button3.bind("<Button-1>",reddit)
button4.bind("<Button-1>",insta)
button5.bind("<Button-1>",yt)

window.mainloop()

