from tkinter import *
from tkinter import messagebox as tmsg
from tkinter import ttk
from PIL import Image,ImageTk
from admin import adminpage
import mysql

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management system")
        self.root.geometry("980x580+200+150")
        head=Frame(root)
        head.place(x=0,y=0,width=980,height=70)
        
        Label(head,text="WELCOME",font="lucida 30 bold",bd=4,relief=SUNKEN,bg="red",fg="gold").place(x=0,y=0,width=980,height=70)
        
        body=Frame(root,bg="blue")
        body.place(x=0,y=70,width=980,height=510)
        
        ph=Frame(body,bg="blue").place(x=0,y=70,width=680,height=510)
        img=Image.open(r"C:\Users\simra\Downloads\john-schnobrich-2FPjlAyMQTA-unsplash.jpg")
        img=img.resize((680,510),Image.FILTERED)
        self.photoimage=ImageTk.PhotoImage(img)
        labl=Label(ph,image=self.photoimage)
        labl.place(x=0,y=70,width=680,height=510)
        
        txt=Frame(body,bd=4,relief=GROOVE)
        txt.place(x=680,y=0,width=300,height=520)
        def main_page():
            
            id=Label(txt,text="Enter your identity:",font="lucida 15",width=26,height=1)
            id.grid(row=0,column=0)
            
            self.var_identity=StringVar()
            ent=ttk.Combobox(txt,textvariable=self.var_identity,state="readonly",width=20,height=1,font="lucida 16")
            ent["value"]=("Admin","Teacher","student")
            ent.grid(row=1,column=0)
            
            self.var_id=StringVar()
            self.var_psd=StringVar()
        main_page()
         
            
        
        
        def next_page():
            clear_screen()
            
            id=Label(txt,text="Enter your id:",font="lucida 15",width=26,height=1)
            id.grid(row=0,column=0)
            id_entry=ttk.Entry(txt,font="lucida 15",textvariable=self.var_id,width=21)
            id_entry.grid(row=1,column=0)
            
            password=Label(txt,text="Enter Password:",font="lucida 15",width=26,height=1)
            password.grid(row=2,column=0)
            password_entry=ttk.Entry(txt,font="lucida 15",textvariable=self.var_psd,width=21,show="*")
            password_entry.grid(row=3,column=0)
            
            def submit_page():
                
                if self.var_id.get()=="Admin" and self.var_psd.get()=="admin123":
                    
                    admin_page()
                  
                    
                elif self.var_psd.get()=="student":
                    student_detail()
                    
                elif self.var_psd.get()=="teacher":
                    checkout_deatil()
                    
                else:
                        tmsg.showerror("Warning","invalid username or password")
                    
                    
            btn=Button(txt,text="Submit",command=submit_page,font="lucida 12 bold",cursor="hand2")
            btn.grid(row=4,column=0,pady=15)
                
        next_btn=Button(txt,text="next",command=next_page,font="lucida 13",cursor="hand2",width=15)
        next_btn.grid(row=2,column=0,pady=10)        
        
        def clear_screen():
            for widget in txt.winfo_children():
                widget.destroy()
                
        def clear_body():
            labl.place_forget()
            
        def checkout_deatil():
            if self.var_id.get()=="":
                tmsg.showerror("Error","Enter id")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="simran2003",database="student_management")
                my_cursor=conn.cursor()
                query=("select * from teacher where T_Id=%s")
                value=(self.var_id.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                if row==None:
                        tmsg.showerror("Error!","id number doesn't exists")
                else:
                        ShowDetails(row)
                        conn.commit()
                        conn.close()
        
        def ShowDetails(row):
            clear_body()
            tname=Label(body,text="Name",font="lucida 15").place(x=40,y=30)
            name_data = Label(body, text=row[1], font=("lucida", 10)).place(x=40, y=60)
            
            tcourse=Label(body,text="Course",font="lucida 15").place(x=40,y=100)
            course=Label(body,text=row[2],font="lucida 10").place(x=40, y=130)
            
            tcourse_id=Label(body,text="Course id",font="lucida 15").place(x=40,y=170)
            course_id=Label(body,text=row[3],font="lucida 10").place(x=40, y=200)
            
            tedu=Label(body,text="Education",font="lucida 15").place(x=40,y=240)
            edu=Label(body,text=row[4],font="lucida 10").place(x=40, y=270)
            
            Mobile=Label(body,text="Mobile",font="lucida 15").place(x=40,y=310)
            mobile_data=Label(body,text=row[5],font="lucida 10").place(x=40, y=340)
            
            sal=Label(body,text="salary",font="lucida 15").place(x=40,y=380)
            sal_data=Label(body,text=row[6],font="lucida 10").place(x=40, y=410)
                
        def student_detail():
            if self.var_id.get()=="":
                tmsg.showerror("Error","ALL Field required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="simran2003",database="student_management")
                my_cursor=conn.cursor()
                query=("select * from student where S_Id=%s")
                value=(self.var_id.get(),)
                my_cursor.execute(query,value)
                row1=my_cursor.fetchone()
                
                if row1==None:
                        tmsg.showerror("Error!","id number doesn't exists")
                else:
                        ShowStudentDetails(row1)
                        conn.commit()
                        conn.close()
                        
        def ShowStudentDetails(row1):
            clear_body()
            fname=Label(body,text="First Name",font="lucida 15").place(x=40,y=30)
            fname_data = Label(body, text=row1[1], font=("lucida", 10)).place(x=40, y=60)
            
            fname=Label(body,text="Last Name",font="lucida 15").place(x=40,y=100)
            lname_data = Label(body, text=row1[2], font=("lucida", 10)).place(x=40, y=130)
            
            tcourse=Label(body,text="Course",font="lucida 15").place(x=40,y=170)
            course=Label(body,text=row1[3],font="lucida 10").place(x=40, y=200)
            
            subject=Label(body,text="Subject",font="lucida 15").place(x=40,y=240)
            sub=Label(body,text=row1[4],font="lucida 10").place(x=40, y=270)
            
            fee=Label(body,text="fees",font="lucida 15").place(x=40,y=310)
            fees=Label(body,text=row1[5],font="lucida 10").place(x=40, y=340)
            
            age=Label(body,text="Age",font="lucida 15").place(x=300,y=30)
            mobile_data=Label(body,text=row1[6],font="lucida 10").place(x=300, y=60)
            
            gender=Label(body,text="Gender",font="lucida 15").place(x=300,y=100)
            sal_data=Label(body,text=row1[7],font="lucida 10").place(x=300, y=130)
            
            contact=Label(body,text="Contact",font="lucida 15").place(x=300,y=170)
            con_data=Label(body,text=row1[8],font="lucida 10").place(x=300, y=200)
            
            email=Label(body,text="Email",font="lucida 15").place(x=300,y=240)
            email_data=Label(body,text=row1[9],font="lucida 10").place(x=300, y=270)
                
        def admin_page():
            new_win = Toplevel(self.root)
            self.app = adminpage(new_win)  
        
        # def clear_screen():
            
            
           
        def clear_text():
            self.var_id.set("")
            self.var_psd.set("")
            
            
        
       
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()