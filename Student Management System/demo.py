from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tmsg
import mysql

class demo:
    def __init__(self,root):
        self.root=root
        self.root.title("demo")
        self.root.geometry("980x580")
        
        Label(root,text="WELCOME",font="lucida 30 bold",bd=4,relief=SUNKEN,bg="red",fg="gold").place(x=0,y=0,width=980,height=70)    
        body=Frame(root,bg="blue")
        body.place(x=0,y=70,width=980,height=510)
        
        tname=Label(body,text="Name",font="lucida 15").place(x=40,y=30)
        name_data = Label(body, text="k", font=("lucida", 10)).place(x=40, y=60)
        
        tcourse=Label(body,text="Course",font="lucida 15").place(x=40,y=100)
        course=Label(body,text="g",font="lucida 10").place(x=40, y=130)
        
        tcourse_id=Label(body,text="Course id",font="lucida 15").place(x=40,y=170)
        course_id=Label(body,text="g",font="lucida 10").place(x=40, y=200)
        
        tedu=Label(body,text="Education",font="lucida 15").place(x=40,y=240)
        edu=Label(body,text="g",font="lucida 10").place(x=40, y=270)
        
        Mobile=Label(body,text="Mobile",font="lucida 15").place(x=300,y=30)
        mobile_data=Label(body,text="g",font="lucida 10").place(x=40, y=340)
        
        sal=Label(body,text="salary",font="lucida 15").place(x=40,y=380)
        sal_data=Label(body,text="g",font="lucida 10").place(x=40, y=410)
        
        
        # id=Label(body,text="Enter your id:",font="lucida 15",width=26,height=1)
        # id.grid(row=0,column=0)
            
        # self.var_id=StringVar()
            
        # id_entry=ttk.Entry(body,font="lucida 15",textvariable=self.var_id,width=21)
        # id_entry.grid(row=1,column=0)
        
        # def check_details():
        #     if self.var_id.get()=="":
        #         tmsg.showerror("incorrect","enter valid")
        #     else:
        #         conn=mysql.connector.connect(host="localhost",username="root",password="simran2003",database="student_management2")
        #         my_cursor=conn.cursor()
        #         query=("select * from teacher where contact=%s")
        #         value=(self.contact_var.get(),)
        #         my_cursor.execute(query,value)
        #         row=my_cursor.fetchone()
                
        #         if row==None:
        #                 tmsg.showerror("Error!","Contact number doesn't exists")
        #         else:
        #                 # ShowDetails(row)
        #                 conn.commit()
        #                 conn.close()
        
        
        # def show_detail(row):
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=demo(root)
    root.mainloop()
    