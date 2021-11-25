from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Login Page")
#root.iconbitmap('')
root.geometry("1920x1080")
root.iconbitmap('C:/Users/Srikar Reddy/Desktop/mainproject/3f9470b34a8e3f526dbdb022f9f19cf7.ico')
#define image
bg = PhotoImage(file="C:/Users/Srikar Reddy/Desktop/mainproject/unnamed.png")

#define canvas
my_canvas = Canvas(root, width=1920, height=1800, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

#put the image on the canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

img = PhotoImage(file="C:/Users/Srikar Reddy/Desktop/mainproject/logo1.png")      
my_canvas.create_image(730,300, anchor=NW, image=img)

#Create welcome screen
def welcome():

    uname = un_entry.get()
    password = pw_entry.get()
 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
 
    elif(uname == "Admin" and password == "123"):
        un_entry.destroy()
        pw_entry.destroy()
        login_btn.destroy()
 
        messagebox.showinfo("","Login Success")
        root.destroy()
        import project
        exec('project')
       
 
    else :
        messagebox.showinfo("","Incorrent Username and Password")

    #add a welcome message
    #my_canvas.create_text(160,450, text="Welcome", font=("Helvatica, 40"), fill="white")

#define entry boxes
un_entry = Entry(root, font=("Helvetica", 24), width=15, fg="#336d92", bd=0)
pw_entry = Entry(root, font=("Helvetica", 24), width=15, fg="#336d92", bd=0)

un_entry.insert(0, "Username")
pw_entry.insert(0, "Password")

#add the entry boxes to the canvas
un_window = my_canvas.create_window(640,400, anchor="nw", window=un_entry)
pw_window = my_canvas.create_window(640,450, anchor="nw", window=pw_entry)

#define button
login_btn = Button(root, text="Login", font=("Helvetica", 20), width=6, fg="#336d92", command=welcome)
login_btn_window = my_canvas.create_window(720,500, anchor="nw", window=login_btn)


#Define entry_clear function
def entry_clear(e):
    if un_entry.get() == 'Username' or pw_entry.get() == 'Password':
        un_entry.delete(0,END)
        pw_entry.delete(0,END)
        #change text to stars
        pw_entry.config(show="*")


#bind the entry boxes
un_entry.bind("<Button-1>", entry_clear)
pw_entry.bind("<Button-1>", entry_clear)

root.mainloop()