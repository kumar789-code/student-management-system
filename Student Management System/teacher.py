from tkinter import *
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox as tmsg


class teacher_win:
    def __init__(self,root):
        self.root=root
        self.root.title("teacher")
        self.root.geometry("1530x530+0+300")
        num=1
        if num==1:
            
            x=random.randint(1000,10000)
            
            
            self.var_tid=StringVar()
            self.var_tid.set(x)
            self.tname=StringVar()
            self.course=StringVar()
            self.Education=StringVar()
            self.mobile=StringVar()
            self.cid=StringVar()
            
            
            
          
            detail=Frame(root,bg="sky blue",bd=2,relief=SUNKEN)
            detail.place(x=0,y=0,height=530,width=1530)
            
            
            Label(detail,text="TEACHER DETAILS",fg="green",bg="aqua",font="lucida 20").place(x=0,y=0,height=50,width=1530)
        #        #===========================================================================Frame============================================================================== 
            labl=LabelFrame(detail,text="Add Teacher Details",font="lucida 16 bold",bd=2,relief=RIDGE,padx=2)
            labl.place(x=0,y=50,height=500,width=420)
                
        #         #========================================INPUTS===========================================================================================================
            T_id=Label(labl,text="Teacher Id",font="lucida 15 bold",padx=2,pady=4)
            T_id.grid(row=0,column=0,sticky=W)

        #     # ===========================================================================================================================
            id_entry=ttk.Entry(labl,textvariable=self.var_tid,font="lucida 16 bold",width=18)
            id_entry.grid(row=0,column=1)
             
            T_name=Label(labl,text="Teacher Name",font="lucida 15 bold",padx=2,pady=4)
            T_name.grid(row=1,column=0,sticky=W)
            
            name_entry=ttk.Entry(labl,textvariable=self.tname,font="lucida 16 bold",width=18)
            name_entry.grid(row=1,column=1)
        #    # ===================================================================================================
        
            course_name=Label(labl,text="Course",font="lucida 15 bold",padx=2,pady=4)
            course_name.grid(row=2,column=0,sticky=W)
            
            c_entry=ttk.Entry(labl,textvariable=self.course,font="lucida 16 bold",width=18)
            c_entry.grid(row=2,column=1)
            
            cid=Label(labl,text="course Id",font="lucida 15 bold",padx=2,pady=4)
            cid.grid(row=3,column=0,sticky=W)
            
            cid_entry=ttk.Entry(labl,textvariable=self.cid,font="lucida 16 bold",width=18)
            cid_entry.grid(row=3,column=1)
            
            edu=Label(labl,text="Education",font="lucida 15 bold",padx=2,pady=4)
            edu.grid(row=4,column=0,sticky=W)
            
            m_entry=ttk.Entry(labl,textvariable=self.Education,font="lucida 16 bold",width=18)
            m_entry.grid(row=4,column=1)
            
            
            mob=Label(labl,text="Mobile no.",font="lucida 15 bold",padx=2,pady=4)
            mob.grid(row=5,column=0,sticky=W)
            
            m_entry=ttk.Entry(labl,textvariable=self.mobile,font="lucida 16 bold",width=18)
            m_entry.grid(row=5,column=1)
            
            
            sal=Label(labl,text="Salary",font="lucida 15 bold",padx=2,pady=4)
            sal.grid(row=6,column=0,sticky=W)
            self.var_sal=StringVar()
            
            sal_entry=ttk.Entry(labl,textvariable=self.var_sal,font="lucida 16 bold",width=18)
            sal_entry.grid(row=6,column=1)
            
            
        #     # =====================================================================BUTTONS============================================================
            
            btn_frame2=Frame(labl,bd=2,relief=SUNKEN,bg="red")
            btn_frame2.place(x=0,y=270,width=410,height=40)
            
        #     # ====================================================ADD BUTTON=========================================================
            def add_techer():
                if self.var_tid.get()=="" and self.tname.get()=="":
                    tmsg.showerror("Error","All field are required")
                    
                else:
                    try:
                        conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into teacher values(%s,%s,%s,%s,%s,%s,%s)",(
                                                    self.var_tid.get(),
                                                    self.tname.get(),
                                                    self.course.get(),
                                                    self.cid.get(),
                                                    self.Education.get(),
                                                    self.mobile.get(),
                                                    self.var_sal.get(),
                                                    
                                                                                    ))
                
                        conn.commit()
                        fetch_data()
                        conn.close()
                        tmsg.showinfo("Success","Added Successfully")
                        reset()
                    except Exception as e:
                        tmsg.showerror("Warning",f"{str(e)}",parent=self.root)
                        
                        
            def fetch_data():
                conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from teacher")
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
                
                self.var_tid.set(row[0])
                self.tname.set(row[1])
                self.course.set(row[2])
                self.cid.set(row[3])
                self.Education.set(row[4])
                self.mobile.set(row[5])
                self.var_sal.set(row[6])
            
            addbtn=Button(btn_frame2,text="ADD",command=add_techer,font="lucida 10",width=10,cursor="hand2")
            addbtn.grid(row=0,column=0,padx=6,pady=4)
        #     # =====================================================update button =====================================================================
            def update():
                if self.tname.get()=="" or self.mobile.get()=="":
                    tmsg.showerror("Warning","'ALL field are required")
                    
                else:
                    conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update teacher set T_Name=%s,Course=%s,C_Id=%s,Education=%s,Mobile=%s ,salary=%s where T_Id=%s",( 
                                                                                self.tname.get(),
                                                                                self.course.get(),
                                                                                self.cid.get(),
                                                                                self.Education.get(),
                                                                                self.mobile.get(),
                                                                                self.var_sal.get(),
                                                                                self.var_tid.get()
                                                                                
                    ))
                    
                    conn.commit()
                    fetch_data()
                    conn.close()
                    tmsg.showinfo("Success","Updated Successfully") 
                    reset()
                
            updatebtn=Button(btn_frame2,text="UPDATE",command=update,font="lucida 10",width=10,cursor="hand2")
            updatebtn.grid(row=0,column=1,padx=6,pady=4)
            
        #     # ==========================================================Delete button===============================================================
            def delete():
                if self.tname.get()=="":
                    tmsg.showerror("Error","Invalid action")
                    
                else:
                    dele=tmsg.askyesno("Teacher Detail",f"Are you want to delete {self.tname.get()}",parent=self.root)
                    if dele>0:
                        conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("delete from teacher where T_Id=%s",(self.var_tid.get(),))
                        conn.commit()
                        fetch_data()
                        conn.close()
                        reset()
                        tmsg.showinfo("success","Deleted Successfully")
                        
                    else:
                        return
        
        
            delbtn=Button(btn_frame2,text="DELETE",command=delete,font="lucida 10",width=10,cursor="hand2")
            delbtn.grid(row=0,column=2,padx=6,pady=4)
            
        #     # =================================================RESET================================================
            def reset():
                # self.var_tid.set(x)
                self.tname.set("")
                self.course.set("")
                self.cid.set("")
                self.Education.set("")
                self.mobile.set("")
                self.var_sal.set("")
                
            resbtn=Button(btn_frame2,text="RESET",command=reset,font="lucida 10",width=10,cursor="hand2")
            resbtn.grid(row=0,column=3,padx=6,pady=4)
            
            
            
            
        #     # =====================================================DETAIL FRAME=====================================================
            table_frame=LabelFrame(detail,text="View Details and Search System",font="lucida 16 bold",bd=2,relief=RIDGE,padx=2)
            table_frame.place(x=430,y=50,height=500,width=830)
            
            
            srh_btn=Label(table_frame,text="Search By",width=10,bg="red",font="arial 14",fg="white")
            srh_btn.grid(row=0,column=0,sticky=W,padx=2)
            
            self.search_var=StringVar()
            
            sel_combo=ttk.Combobox(table_frame,width=14,textvariable=self.search_var,font="lucida 15",state="readonly")
            sel_combo["value"]=("Teacher id","mobile number")
            sel_combo.current(0)
            sel_combo.grid(row=0,column=1,padx=2)
            
            text_search=StringVar()
            entry=ttk.Entry(table_frame,textvariable=text_search,width=16,font="arial 15")
            entry.grid(row=0,column=2,padx=2)
            
            def search_teacher():
                search_term=text_search.get()
                search_by=self.search_var.get()
                
                if search_by=="Teacher id":
                    query=("select * from teacher where T_Id=%s")
                else:
                    query=("select * from teacher where Mobile=%s")
                
                conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                my_cursor=conn.cursor()
                my_cursor.execute(query,(search_term,)) 
                rows=my_cursor.fetchall()
                
                if len(rows)!=0:
                    self.admin_view.delete(*self.admin_view.get_children())
                    for row in rows:
                        self.admin_view.insert("", END, values=row)
                    
                conn.close()
                          
                    
            
            
            srh_btn=Button(table_frame,text="SEARCH",cursor="hand2",command=search_teacher,width=15,bg="green",font="lucida 11",fg="white")
            srh_btn.grid(row=0,column=3,padx=2)
            
            
            detail_frame=Frame(table_frame,bd=2,relief=RIDGE)
            detail_frame.place(x=0,y=50,width=800,height=350)
            
            
            scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
            
            
            
            self.admin_view=ttk.Treeview(detail_frame,columns=("T_Id","T_Name","Course","C_Id","Education","Mobile","salary"))
            
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            
            scroll_x.config(command=self.admin_view.xview)
            scroll_y.config(command=self.admin_view.yview)
            
            self.admin_view.heading("T_Id",text="Teacher Id")
            self.admin_view.heading("T_Name",text="Teacher Name")
            self.admin_view.heading("Course",text="Course")
            self.admin_view.heading("C_Id",text="course Id")
            self.admin_view.heading("Education",text="Education")
            self.admin_view.heading("Mobile",text="Mobile No")
            self.admin_view.heading("salary",text="Salary")
            
            self.admin_view["show"]="headings"
            
            
            self.admin_view.column("T_Id",width=100)
            self.admin_view.column("T_Name",width=100)
            self.admin_view.column("Course",width=100)
            self.admin_view.column("C_Id",width=100)
            self.admin_view.column("Education",width=100)
            self.admin_view.column("Mobile",width=100)
            self.admin_view.column("salary",width=100)
            
            
            
            self.admin_view.pack(fill=BOTH,expand=1)
            self.admin_view.bind("<ButtonRelease-1>",get_cursor)
            fetch_data()
            
            
if __name__=="__main__":
    root=Tk()
    obj=teacher_win(root)
    root.mainloop()