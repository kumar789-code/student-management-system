from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tmsg
from PIL import Image,ImageTk

class teacher_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Teacher page")
        self.root.geometry("980x580+0+0")
        
        Label(root,text="WELCOME",font="lucida 30 bold",bd=4,relief=SUNKEN,bg="red",fg="gold").place(x=0,y=0,width=980,height=70)
        
        ph=Frame(root,bg="blue").place(x=0,y=70,width=680,height=510)
        
        
        img=Image.open(r"C:\Users\simra\Downloads\john-schnobrich-2FPjlAyMQTA-unsplash.jpg")
        img=img.resize((680,510),Image.FILTERED)
        self.photoimage=ImageTk.PhotoImage(img)
        labl=Label(ph,image=self.photoimage)
        labl.place(x=0,y=70,width=680,height=510)
        
        Label(ph,text="student management system",font="lucida 30 bold",relief=RIDGE,bd=3).place(x=30,y=250,width=580,height=60)
        
        txt=Frame(root,bd=4,relief=GROOVE)
        txt.place(x=680,y=70,width=300,height=500)
        
        id=Label(txt,text="Enter your identity:",font="lucida 15",width=26,height=1)
        id.grid(row=0,column=0)
        
        self.var_identity=StringVar()
        ent=ttk.Combobox(txt,textvariable=self.var_identity,state="readonly",width=20,height=1,font="lucida 16")
        ent["value"]=("Admin","Teacher","student")
        ent.grid(row=1,column=0)
        
        id=Label(txt,text="Enter your id:",font="lucida 15",width=26,height=1)
        id.grid(row=2,column=0)
        
        self.var_id=StringVar()
        
        id_entry=ttk.Entry(txt,font="lucida 15",textvariable=self.var_id,width=21)
        id_entry.grid(row=3,column=0)
        
        password=Label(txt,text="Enter Password:",font="lucida 15",width=26,height=1)
        password.grid(row=4,column=0)
        
        self.var_psd=StringVar()
        
        password_entry=ttk.Entry(txt,font="lucida 15",textvariable=self.var_psd,width=21)
        password_entry.grid(row=5,column=0)
        
        btn=Button(txt,text="submit",font="lucida 13",cursor="hand2")
        btn.grid(row=6,column=0,pady=5)
        
if __name__=="__main__":
    root=Tk()
    obj=teacher_page(root)
    root.mainloop()