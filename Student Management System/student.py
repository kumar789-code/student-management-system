from tkinter import *
from tkinter import ttk 
import random
import mysql.connector
from tkinter import messagebox as tmsg

class student_page:
    def __init__(self,root):
        self.root=root
        self.root.title("Student details")
        self.root.geometry("1530x530+0+300")
        
        
        num=1
        if num==1:
            
            detail=Frame(root,bg="sky blue",bd=2,relief=SUNKEN)
            detail.place(x=0,y=0,height=530,width=1530)
        
            Label(detail,text="STUDENT DETAILS",fg="green",bg="aqua",font="lucida 20").place(x=0,y=0,height=50,width=1530)
        #        #===========================================================================Frame============================================================================== 
            labl=LabelFrame(detail,text="Add Student Details",font="lucida 16 bold",bd=2,relief=RIDGE,padx=2)
            labl.place(x=0,y=50,height=500,width=420)
                
        #========================================ID===========================================================================================================
            id=Label(labl,text="Student Id",font="lucida 15 bold",padx=2,pady=4)
            id.grid(row=0,column=0,sticky=W)
            self.s_id=StringVar()
            x=random.randint(100,10000)
            self.s_id.set(x)
            
            
        
            id_entry=ttk.Entry(labl,textvariable=self.s_id,font="lucida 16 bold",width=18)
            id_entry.grid(row=0,column=1)
            # ============================================================================================name======================================================   
            f_name=Label(labl,text="First Name",font="lucida 15 bold",padx=2,pady=4)
            f_name.grid(row=1,column=0,sticky=W)
            
            self.fname=StringVar()
            
            fname_entry=ttk.Entry(labl,textvariable=self.fname,font="lucida 16 bold",width=18)
            fname_entry.grid(row=1,column=1)
            # ===================================================Lname===================================================
            l_name=Label(labl,text="Last Name",font="lucida 15 bold",padx=2,pady=4)
            l_name.grid(row=2,column=0,sticky=W)
            
            self.lname=StringVar()
            
            lname_entry=ttk.Entry(labl,textvariable=self.lname,font="lucida 16 bold",width=18)
            lname_entry.grid(row=2,column=1)
        #    # ======================================course=============================================================
        
            login_name=Label(labl,text="Course",font="lucida 15 bold",padx=2,pady=4)
            login_name.grid(row=3,column=0,sticky=W)
            self.course=StringVar()
            
            course_entry=ttk.Entry(labl,textvariable=self.course,font="lucida 16 bold",width=18)
            course_entry.grid(row=3,column=1)
            # ========================================Subject====================================================================
            sub=Label(labl,text="subject",font="lucida 15 bold",padx=2,pady=4)
            sub.grid(row=4,column=0,sticky=W)
            self.sub=StringVar()
            
            sub_entry=ttk.Entry(labl,textvariable=self.sub,font="lucida 16 bold",width=18)
            sub_entry.grid(row=4,column=1)
            # =================================================fees==============================================================
            fees=Label(labl,text="Fees",font="lucida 15 bold",padx=2,pady=4)
            fees.grid(row=5,column=0,sticky=W)
            self.fee=StringVar()
            
            fee_entry=ttk.Entry(labl,textvariable=self.fee,font="lucida 16 bold",width=18)
            fee_entry.grid(row=5,column=1)
            
            # ============================================Age====================================
            
            age=Label(labl,text="Age",font="lucida 15 bold",padx=2,pady=4)
            age.grid(row=6,column=0,sticky=W)
            self.age=StringVar()
            
            age_entry=ttk.Entry(labl,textvariable=self.age,font="lucida 16 bold",width=18)
            age_entry.grid(row=6,column=1)
            
            # =======================================================Gender=========================
            
            gender=Label(labl,text="Gender",font="lucida 15 bold",padx=2,pady=4)
            gender.grid(row=7,column=0,sticky=W)
            self.gender=StringVar()
            
            gender_entry=ttk.Combobox(labl,textvariable=self.gender,font="lucida 16 bold",width=18)
            gender_entry["value"]=["Male","Female","other"]
            gender_entry.current(0)
            gender_entry.grid(row=7,column=1)
            
            # ==============================================contact==================================
            
            contact=Label(labl,text="Contact",font="lucida 15 bold",padx=2,pady=4)
            contact.grid(row=8,column=0,sticky=W)
            self.contact=StringVar()
            
            pas_entry=ttk.Entry(labl,textvariable=self.contact,font="lucida 16 bold",width=18)
            pas_entry.grid(row=8,column=1)
            # =========================================Email======================================
            Email=Label(labl,text="Email",font="lucida 15 bold",padx=2,pady=4)
            Email.grid(row=9,column=0,sticky=W)
            
            self.email=StringVar()
            
            m_entry=ttk.Entry(labl,textvariable=self.email,font="lucida 16 bold",width=18)
            m_entry.grid(row=9,column=1)
            
        #     # =====================================================================BUTTONS============================================================
            
            btn_frame2=Frame(labl,bd=2,relief=SUNKEN,bg="red")
            btn_frame2.place(x=0,y=365,width=410,height=40)
            
        #     # ====================================================ADD BUTTON=========================================================
            def add():
                if self.fname.get()=="" or self.contact.get()=="":
                    tmsg.showerror("Alert","All Field required")
                else:
                    conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")    
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.s_id.get(),
                        self.fname.get(),
                        self.lname.get(),
                        self.course.get(),
                        self.sub.get(),
                        self.fee.get(),
                        self.age.get(),
                        self.gender.get(),
                        self.contact.get(),
                        self.email.get()
                    ))
                    conn.commit()
                    fetch_data()
                    conn.close()
                    tmsg.showinfo("student","Added Successfully")
                    reset()
            
            def fetch_data():
                conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                row=my_cursor.fetchall()
                if len(row)!=0:
                    self.admin_view.delete(*self.admin_view.get_children())
                    for i in row:
                        self.admin_view.insert("",END,values=i)
                conn.commit()
                conn.close()
                
                
            def get_cursor(event=""):
                cursor_row=self.admin_view.focus()
                content=self.admin_view.item(cursor_row)
                row=content["values"]
                
                self.s_id.set(row[0])
                self.fname.set(row[1])
                self.lname.set(row[2])
                self.course.set(row[3])
                self.sub.set(row[4])
                self.fee.set(row[5])
                self.age.set(row[6])
                self.gender.set(row[7])
                self.contact.set(row[8])
                self.email.set(row[9])
                view_fee()
                                
            def view_fee():
                conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from fees where student_id=%s",(self.s_id.get(),))
                row=my_cursor.fetchone()
                if row==None:
                        tmsg.showerror("Error!","student id doesn't exists")
                else:
                        ShowDetails(row)
                        conn.commit()
                        conn.close()
            
            def ShowDetails(row):
                self.adm.set(row[1])
                self.tut.set(row[2])
                self.ses.set(row[3])
                self.lib.set(row[4])
                self.exm.set(row[5])
                
                
                
            addbtn=Button(btn_frame2,text="ADD",font="lucida 10",command=add,width=10,cursor="hand2")
            addbtn.grid(row=0,column=0,padx=6,pady=4)
        #     # =====================================================update button =====================================================================
            def update():
                if self.fname.get()=="" or self.fee.get()=="" or self.contact.get()=="":
                    tmsg.showerror("Error","Invalid Action")
                    
                else:
                    conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set F_Name=%s,L_Name=%s,Course=%s,Subject=%s,Fees=%s,Age=%s,Gender=%s,Contact=%s,Email=%s where S_Id=%s",(
                                                                self.fname.get(),
                                                                self.lname.get(),
                                                                self.course.get(),
                                                                self.sub.get(),
                                                                self.fee.get(),
                                                                self.age.get(),
                                                                self.gender.get(),
                                                                self.contact.get(),
                                                                self.email.get(),
                                                                self.s_id.get()
                    ))
                    conn.commit()
                    fetch_data()
                    conn.close()
                    tmsg.showinfo("Success","Updated successfully")
                    reset()
            updatebtn=Button(btn_frame2,text="UPDATE",command=update,font="lucida 10",width=10,cursor="hand2")
            updatebtn.grid(row=0,column=1,padx=6,pady=4)
            
        #     # ==========================================================Delete button===============================================================
            def delete_student():
                if self.course.get()=="" or self.contact.get()=="":
                    tmsg.showerror("ERROR","Invalid action")
                else:
                    delete=tmsg.askyesno("STUDENT DETAIL",f"Do you want to delete ({self.fname.get()})")
                    if delete>0:
                        conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("delete from student where S_Id=%s",(self.s_id.get(),))
                        conn.commit()
                        fetch_data()
                        conn.close()
                        tmsg.showinfo("Success","Deleted successfully")
                        reset()
                    else:
                        return
        
        
            delbtn=Button(btn_frame2,text="DELETE",command=delete_student,font="lucida 10",width=10,cursor="hand2")
            delbtn.grid(row=0,column=2,padx=6,pady=4)
            
        #     # =================================================RESET================================================
            def reset():
                self.fname.set("")
                self.lname.set("")
                self.course.set("")
                self.sub.set("")
                self.fee.set("")
                self.age.set("")
                # self.gender.set("")
                self.contact.set("")
                self.email.set("")
                x=random.randint(100,10000)
                self.s_id.set(x)
            resbtn=Button(btn_frame2,command=reset,text="RESET",font="lucida 10",width=10,cursor="hand2")
            resbtn.grid(row=0,column=3,padx=6,pady=4)

#================================================================= fees structure=================================================================================
            fee_frame=LabelFrame(self.root,text="Fees Structure",font="lucida 15",bd=2,relief=RIDGE,padx=2)
            fee_frame.place(x=430,y=50,height=300,width=270)
        #    ===================================================student detail=============================================================================================
            adm_id=Label(fee_frame,text="student id",font="lucida 10",padx=2,pady=4)
            adm_id.grid(row=0,column=0,sticky=W)
            
            
            adm_identry=ttk.Entry(fee_frame,textvariable=self.s_id,font="lucida 10",width=18)
            adm_identry.grid(row=0,column=1)

            # ======================================Admission fee======================
            adm=Label(fee_frame,text="Admission Fees",font="lucida 10",padx=2,pady=4)
            adm.grid(row=1,column=0,sticky=W)
            self.adm=StringVar()
            
            adm_entry=ttk.Entry(fee_frame,textvariable=self.adm,font="lucida 10",width=18)
            adm_entry.grid(row=1,column=1)
            # ====================================================tution fees=============================
            tut=Label(fee_frame,text="Tution Fees",font="lucida 10",padx=2,pady=4)
            tut.grid(row=2,column=0,sticky=W)
            self.tut=StringVar()
            
            tut_entry=ttk.Entry(fee_frame,textvariable=self.tut,font="lucida 10",width=18)
            tut_entry.grid(row=2,column=1)
            # ==========================================Session charge==============================
            ses=Label(fee_frame,text="Session charge",font="lucida 10",padx=2,pady=4)
            ses.grid(row=3,column=0,sticky=W)
            self.ses=StringVar()
            
            ses_entry=ttk.Entry(fee_frame,textvariable=self.ses,font="lucida 10",width=18)
            ses_entry.grid(row=3,column=1)
            
            # =====================================library fees===================================
            lib=Label(fee_frame,text="Library Charge",font="lucida 10",padx=2,pady=4)
            lib.grid(row=4,column=0,sticky=W)
            self.lib=StringVar()
            
            lib_entry=ttk.Entry(fee_frame,textvariable=self.lib,font="lucida 10",width=18)
            lib_entry.grid(row=4,column=1)
            
            # ================================Examination charge=========================
            
            exm=Label(fee_frame,text="Examination Fees",font="lucida 10",padx=2,pady=4)
            exm.grid(row=5,column=0,sticky=W)
            self.exm=StringVar()
            
            exm_entry=ttk.Entry(fee_frame,textvariable=self.exm,font="lucida 10",width=18)
            exm_entry.grid(row=5,column=1)
            
            
            # =================================================TOTAL==================================
            
            total=Label(fee_frame,text="Total",font="lucida 15",padx=2,pady=4,fg="red")
            total.grid(row=6,column=0,sticky=W)
            self.total=StringVar()
            
            total_entry=ttk.Entry(fee_frame,textvariable=self.fee,font="lucida 10",width=18,foreground="red")
            total_entry.grid(row=6,column=1)
            
            def sum():
                try:
                    total=float(self.adm.get())+float(self.tut.get())+float(self.ses.get())+float(self.lib.get())+float(self.exm.get())
                    self.fee.set(str(total))
                    add_detail()
                except ValueError:
                    # self.fee.set("")
                    tmsg.showerror("Error","inavlid input")
            
            generate=Button(fee_frame,text="Generate Fees",command=sum,font="lucida 10",fg="green",cursor="hand2").grid(row=7,column=0)
            
            # =======================================================adding============================================================
            def add_detail():
                if self.fee.get()=="":
                    tmsg.showerror("Student management system","All field are Required")
                else:
                    conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into fees values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.s_id.get(),
                        self.adm.get(),
                        self.tut.get(),
                        self.ses.get(),
                        self.lib.get(),
                        self.exm.get(),
                        self.fee.get()
                    ))
                    conn.commit()
                    conn.close()
                    tmsg.showinfo(f"{self.s_id.get()}",f"total fees is {self.fee.get()}")

        #     # =====================================================DETAIL FRAME=====================================================
            table_frame=LabelFrame(self.root,text="View Details and Search System",font="lucida 16 bold",bd=2,relief=RIDGE,padx=2)
            table_frame.place(x=710,y=50,height=500,width=810)
            
            
            srh_btn=Label(table_frame,text="Search By",width=10,bg="red",font="arial 14",fg="white")
            srh_btn.grid(row=0,column=0,sticky=W,padx=2)
            
            self.search_var=StringVar()
            
            sel_combo=ttk.Combobox(table_frame,width=14,textvariable=self.search_var,font="lucida 15",state="readonly")
            sel_combo["value"]=("Student id","Contact")
            sel_combo.current(0)
            sel_combo.grid(row=0,column=1,padx=2)
            
            text_search=StringVar()
            entry=ttk.Entry(table_frame,textvariable=text_search,width=16,font="arial 15")
            entry.grid(row=0,column=2,padx=2)
            
            def search_student():
                search_term=text_search.get()
                search_by=self.search_var.get()
                
                if search_by=="Student id":
                    query=("select * from student where S_Id=%s")
                else:
                    query=("select * from student where contact=%s")
                conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                my_cursor=conn.cursor()
                my_cursor.execute(query,(search_term,))
                rows=my_cursor.fetchall()
                
                if len(rows)!=0:
                    self.admin_view.delete(*self.admin_view.get_children())
                    for row in rows:
                        self.admin_view.insert("",END,values=row)
                conn.close()
            
            srh_btn=Button(table_frame,text="SEARCH",command=search_student,cursor="hand2",width=15,bg="green",font="lucida 11",fg="white")
            srh_btn.grid(row=0,column=3,padx=2)
            
            
            detail_frame=Frame(table_frame,bd=2,relief=RIDGE)
            detail_frame.place(x=0,y=50,width=810,height=350)
            
            
            scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
            
            
            self.admin_view=ttk.Treeview(detail_frame,columns=("S_Id","F_Name","L_Name","Course","Subject","Fees","Age","Gender","Contact","Email"))
            
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            
            scroll_x.config(command=self.admin_view.xview)
            scroll_y.config(command=self.admin_view.yview)
            
            self.admin_view.heading("S_Id",text="Student Id")
            self.admin_view.heading("F_Name",text="F Name")
            self.admin_view.heading("L_Name",text="L Name")
            self.admin_view.heading("Course",text="Course")
            self.admin_view.heading("Subject",text="subject")
            self.admin_view.heading("Fees",text="fees")
            self.admin_view.heading("Age",text="Age")
            self.admin_view.heading("Gender",text="Gender")
            self.admin_view.heading("Contact",text="Contact")
            self.admin_view.heading("Email",text="Email")
            
            
            self.admin_view["show"]="headings"
            
            
            self.admin_view.column("S_Id",width=80)
            self.admin_view.column("F_Name",width=80)
            self.admin_view.column("L_Name",width=80)
            self.admin_view.column("Course",width=80)
            self.admin_view.column("Subject",width=80)
            self.admin_view.column("Fees",width=80)
            self.admin_view.column("Age",width=80)
            self.admin_view.column("Gender",width=80)
            self.admin_view.column("Contact",width=80)
            self.admin_view.column("Email",width=80)
        
            self.admin_view.pack(fill=BOTH,expand=1)
            self.admin_view.bind("<ButtonRelease-1>",get_cursor)
            fetch_data()



if __name__=="__main__":
    root=Tk()
    obj=student_page(root)
    root.mainloop()