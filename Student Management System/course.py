from tkinter import *
import mysql.connector
from tkinter import ttk
import random
from tkinter import messagebox as tmsg


class course_window:
    def __init__(self,root):
        self.root=root
        self.root.title("COURSE DETAILS")
        self.root.geometry("1530x530+0+300")
        
        
        detail=Frame(root,bg="sky blue",bd=2,relief=SUNKEN)
        detail.place(x=0,y=0,height=530,width=1530)
        
        
          
        self.var_cid=StringVar()
        x=random.randint(1,100)
        y="S"+str(x)
        self.var_cid.set(y)
        self.var_cname=StringVar()
        self.var_sub=StringVar()
        self.var_fees=StringVar()
        self.var_duration=StringVar()
        
            
        Label(detail,text="ADD COURSE DETAILS",fg="green",bg="aqua",font="lucida 20").place(x=0,y=0,height=50,width=1530)
    #        #===========================================================================Frame============================================================================== 
        labl=LabelFrame(detail,text="Add Course",font="lucida 16 bold",bd=2,relief=RIDGE,padx=2)
        labl.place(x=0,y=50,height=500,width=420)
                
        #         #========================================ADMIN ID===========================================================================================================
        C_id=Label(labl,text="Course Id",font="lucida 15 bold",padx=2,pady=4)
        C_id.grid(row=0,column=0,sticky=W)
            
            
            
        #     # ===========================================================================================================================
        id_entry=ttk.Entry(labl,textvariable=self.var_cid,font="lucida 16 bold",width=18)
        id_entry.grid(row=0,column=1)
            
            
            
            
        C_name=Label(labl,text="Course Name",font="lucida 15 bold",padx=2,pady=4)
        C_name.grid(row=1,column=0,sticky=W)
            
        name_entry=ttk.Entry(labl,textvariable=self.var_cname,font="lucida 16 bold",width=18)
        name_entry.grid(row=1,column=1)
        
        C_name=Label(labl,text="subject",font="lucida 15 bold",padx=2,pady=4)
        C_name.grid(row=2,column=0,sticky=W)
            
        name_entry=ttk.Entry(labl,textvariable=self.var_sub,font="lucida 16 bold",width=18)
        name_entry.grid(row=2,column=1)
        
        
        login_name=Label(labl,text="Fees",font="lucida 15 bold",padx=2,pady=4)
        login_name.grid(row=3,column=0,sticky=W)
            
        name_entry=ttk.Entry(labl,textvariable=self.var_fees,font="lucida 16 bold",width=18)
        name_entry.grid(row=3,column=1)
            
        fees=Label(labl,text="Duration",font="lucida 15 bold",padx=2,pady=4)
        fees.grid(row=4,column=0,sticky=W)
            
        pas_entry=ttk.Entry(labl,textvariable=self.var_duration,font="lucida 16 bold",width=18)
        pas_entry.grid(row=4,column=1)
            
           
        #     # =====================================================================BUTTONS============================================================
            
        btn_frame2=Frame(labl,bd=2,relief=SUNKEN,bg="red")
        btn_frame2.place(x=0,y=190,width=410,height=40)
            
        #     # ====================================================ADD BUTTON=========================================================
        
        def add_course():
            if self.var_cname.get()=="" and self.var_duration.get()=="":
                tmsg.showerror("'Warning","All field are required")
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into course values(%s,%s,%s,%s,%s)",(
                        self.var_cid.get(),
                        self.var_cname.get(),
                        self.var_fees.get(),
                        self.var_duration.get(),
                        self.var_sub.get(),
                        
                    ))
                    conn.commit()
                    fetch_data()
                    conn.close()
                    tmsg.showinfo("Successfull","data added successfully")
                except Exception as e:
                    tmsg.showwarning("Warning",f"{str(e)}",parent=self.root)
        
        def fetch_data():
                    conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from course")
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
            
            self.var_cid.set(row[0])
            self.var_cname.set(row[1])
            self.var_fees.set(row[2])
            self.var_duration.set(row[3])
            self.var_sub.set(row[4])
            
        addbtn=Button(btn_frame2,text="ADD",command=add_course,font="lucida 10",width=10,cursor="hand2")
        addbtn.grid(row=0,column=0,padx=6,pady=4)
        #     # =====================================================update button =====================================================================
        
        def update_data():
            if self.var_sub.get()=="":
                tmsg.showerror("Error","All Field are Required",parent=self.root)
                
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                my_cursor=conn.cursor()
                my_cursor.execute("update course set CName=%s,Fees=%s,Duration=%s,subject=%s where C_Id=%s",( 
                                                                                                             
                    self.var_cname.get(),
                    self.var_fees.get(),
                    self.var_duration.get(),
                    self.var_sub.get(),
                    self.var_cid.get(),
                ))
                conn.commit()
                fetch_data()
                conn.close()
                tmsg.showinfo("Success","Updated Successfully",parent=self.root)
                
                
        updatebtn=Button(btn_frame2,text="UPDATE",command=update_data,font="lucida 10",width=10,cursor="hand2")
        updatebtn.grid(row=0,column=1,padx=6,pady=4)
            
        #     # ==========================================================Delete button===============================================================
        def delete_data():
            
            delete=tmsg.askyesno("Course",f"Do you want to delete {self.var_cname.get()}",parent=self.root)
            
            
            if delete>0:
                conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                my_cursor=conn.cursor()
                my_cursor.execute("delete from course where C_Id=%s",(self.var_cid.get(),))
                conn.commit()
                fetch_data()
                conn.close()
                tmsg.showinfo("Success","Deleted Successfully",parent=self.root)
                reset()
            else:
                return
            
            
        delbtn=Button(btn_frame2,text="DELETE",command=delete_data,font="lucida 10",width=10,cursor="hand2")
        delbtn.grid(row=0,column=2,padx=6,pady=4)
            
        #     # =================================================RESET================================================
        def reset():
            self.var_cname.set("")
            self.var_duration.set("")
            self.var_fees.set("")
            self.var_sub.set("")
        resbtn=Button(btn_frame2,text="RESET",command=reset,font="lucida 10",width=10,cursor="hand2")
        resbtn.grid(row=0,column=3,padx=6,pady=4)
            
            
            
            
        #     # =====================================================DETAIL FRAME=====================================================
        table_frame=LabelFrame(detail,text="View Details and Search System",font="lucida 16 bold",bd=2,relief=RIDGE,padx=2)
        table_frame.place(x=430,y=50,height=500,width=830)
            
            
        srh_btn=Label(table_frame,text="Search By",width=10,bg="red",font="arial 14",fg="white")
        srh_btn.grid(row=0,column=0,sticky=W,padx=2)
            
        self.search_var=StringVar()
            
        sel_combo=ttk.Combobox(table_frame,width=14,textvariable=self.search_var,font="lucida 15",state="readonly")
        sel_combo["value"]=("course id","Course Name")
        sel_combo.current(0)
        sel_combo.grid(row=0,column=1,padx=2)
            
        text_search=StringVar()
        entry=ttk.Entry(table_frame,textvariable=text_search,width=16,font="arial 15")
        entry.grid(row=0,column=2,padx=2)
            
        def search_course():
                search_term = text_search.get().strip()
                search_by = self.search_var.get()

                if search_by == "course id":
                    query = "SELECT * FROM admin WHERE Admin_Id = %s"
                else:
                    query = "SELECT * FROM admin WHERE Mobile = %s"
                
                conn = mysql.connector.connect(host="localhost", user="root", password="simran2003", database="student_management")
                my_cursor = conn.cursor()
                my_cursor.execute(query, (search_term,))
                rows = my_cursor.fetchall()
                
                if len(rows) != 0:
                    self.admin_view.delete(*self.admin_view.get_children())
                    for row in rows:
                        self.admin_view.insert("", END, values=row)
                
                conn.close()

            
        srh_btn=Button(table_frame,text="SEARCH",command=search_course,cursor="hand2",width=15,bg="green",font="lucida 11",fg="white")
        srh_btn.grid(row=0,column=3,padx=2)
            
            
        detail_frame=Frame(table_frame,bd=2,relief=RIDGE)
        detail_frame.place(x=0,y=50,width=800,height=350)
            
            
        scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
            
            
            
        self.admin_view=ttk.Treeview(detail_frame,columns=("C_Id","CName","Fees","Duration","subject"))
            
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
            
        scroll_x.config(command=self.admin_view.xview)
        scroll_y.config(command=self.admin_view.yview)
            
        self.admin_view.heading("C_Id",text="Course Id")
        self.admin_view.heading("CName",text="Course Name")
        self.admin_view.heading("Fees",text="Fees")
        self.admin_view.heading("Duration",text="Duration")
        self.admin_view.heading("subject",text="Subject")
          
            
        self.admin_view["show"]="headings"
            
            
        self.admin_view.column("C_Id",width=100)
        self.admin_view.column("CName",width=100)
        self.admin_view.column("Fees",width=100)
        self.admin_view.column("Duration",width=100)
        self.admin_view.column("subject",width=100)
            
            
            
        self.admin_view.pack(fill=BOTH,expand=1)    
        self.admin_view.bind("<ButtonRelease-1>",get_cursor)
        fetch_data()    
        
        
if __name__=="__main__":
    root=Tk()
    obj=course_window(root)
    root.mainloop()