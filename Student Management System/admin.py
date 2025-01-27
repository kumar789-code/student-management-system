from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox as tmsg
from teacher import teacher_win
from student import student_page
from course import course_window


class adminpage:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin page")
        self.root.geometry("1530x830")
        
        frame1=Frame(root,bd=4,relief=RIDGE)
        frame1.place(x=0,y=0,width=1530,height=150)
        
        Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font="lucida 40 bold",bd=4,relief=RIDGE,bg="red").place(x=0,y=0,width=1535,height=120)
        body=Frame(root)
        body.place(x=0,y=120,width=1530,height=680)
        Label(root,text="ADMIN PAGE",font="lucida 20 bold",bd=4,relief=RIDGE,bg="blue",fg="white").place(x=0,y=120,width=1530,height=50)
        
        btn_frame=Frame(body,bd=2,bg="yellow",relief=SUNKEN)
        btn_frame.place(x=0,y=50,height=100,width=1530)
#   =================================================================================ADMIN DETAILS===========================================      
        detail=Frame(body,bg="sky blue",bd=2,relief=SUNKEN)
        detail.place(x=0,y=150,height=530,width=1530)
        
        def admin_details():
            
            self.var_ad_id=StringVar()
            x=random.randint(1000,10000)
            self.var_ad_id.set(x)
        
            
            self.var_name=StringVar()
            self.var_lname=StringVar()
            self.var_pas=StringVar()
            self.var_mobile=StringVar()
            
            
            
            Label(detail,text="ADD ADMIN DETAIL",fg="green",bg="aqua",font="lucida 20").place(x=0,y=0,height=50,width=1530)
            #===========================================================================Frame============================================================================== 
            labl=LabelFrame(detail,text="Add New Admin",font="lucida 16 bold",bd=2,relief=RIDGE,padx=4)
            labl.place(x=0,y=50,height=500,width=420)
                
                #========================================ADMIN ID===========================================================================================================
            ad_id=Label(labl,text="Admin Id",font="lucida 15 bold",padx=2,pady=4)
            ad_id.grid(row=0,column=0,sticky=W)
            
            
            
            # ===========================================================================================================================
            id_entry=ttk.Entry(labl,textvariable=self.var_ad_id,font="lucida 16 bold",width=18)
            id_entry.grid(row=0,column=1)
            
            
            
            
            name=Label(labl,text="Name",font="lucida 15 bold",padx=2,pady=4)
            name.grid(row=1,column=0,sticky=W)
            
            name_entry=ttk.Entry(labl,textvariable=self.var_name,font="lucida 16 bold",width=18)
            name_entry.grid(row=1,column=1)
        # ======================================LOGIN NAME=============================================================
        
            login_name=Label(labl,text="Login Name",font="lucida 15 bold",padx=2,pady=4)
            login_name.grid(row=2,column=0,sticky=W)
            
            name_entry=ttk.Entry(labl,textvariable=self.var_lname,font="lucida 16 bold",width=18)
            name_entry.grid(row=2,column=1)
            
            passw=Label(labl,text="Password",font="lucida 15 bold",padx=2,pady=4)
            passw.grid(row=3,column=0,sticky=W)
            
            pas_entry=ttk.Entry(labl,textvariable=self.var_pas,font="lucida 16 bold",width=18)
            pas_entry.grid(row=3,column=1)
                
            mob=Label(labl,text="Mobile No.",font="lucida 15 bold",padx=2,pady=4)
            mob.grid(row=4,column=0,sticky=W)
                
            mob_entry=ttk.Entry(labl,textvariable=self.var_mobile,font="lucida 16 bold",width=18)
            mob_entry.grid(row=4,column=1)
            
            
            # =====================================================================BUTTONS============================================================
            
            btn_frame2=Frame(labl,bd=2,relief=SUNKEN,bg="red")
            btn_frame2.place(x=0,y=200,width=410,height=40)
            
            # ====================================================ADD BUTTON=========================================================
                
            def add_admin():
                    if self.var_lname==" " or self.var_pas==" " or self.var_mobile==" ":
                        tmsg.showerror("Warning","All field are required",parent=self.root)
                                
                    else:
                        try:
                                    
                            conn=mysql.connector.connect(host="localhost",username="root",password="simran2003",database="student_management")
                            my_cursor=conn.cursor()
                            my_cursor.execute("insert into admin values(%s,%s,%s,%s,%s)",(
                                                                            self.var_ad_id.get(),
                                                                            self.var_name.get(),
                                                                            self.var_lname.get(),
                                                                            self.var_pas.get(),
                                                                            self.var_mobile.get(),
                        
                            ))
                            conn.commit()
                            fetch_data()
                            conn.close()
                            tmsg.showinfo("Success","Data added successfully")
                            reset()
                            self.var_ad_id.set(x) 
                        except Exception as es:
                            tmsg.showwarning("Warning",f"{str(es)}",parent=self.root)
            
            def fetch_data():
                            
                    conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from admin")
                    row=my_cursor.fetchall()
                                
                    if len(row)!=0:
                        self.admin_view.delete(*self.admin_view.get_children())
                        for i in row:
                            self.admin_view.insert("",END,values=i)
                                        
                    conn.commit()
                    conn.close()     
            
            
            addbtn=Button(btn_frame2,text="ADD",command=add_admin,font="lucida 10",width=10,cursor="hand2")
            addbtn.grid(row=0,column=0,padx=6,pady=4)
            # =====================================================update button =====================================================================
            
                    
                    
                    
            def get_cursor(event=""):
                    cursor_row = self.admin_view.focus()
                    content = self.admin_view.item(cursor_row)
                    row = content["values"]
                    
                    self.var_ad_id.set(row[0])
                    self.var_name.set(row[1])
                    self.var_lname.set(row[2])
                    self.var_pas.set(row[3])
                    self.var_mobile.set(row[4])
                    
            def update():
                    if self.var_mobile==" ":
                        tmsg.showerror("Error","All field are required",parent=self.root)
                    else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="simran2003",database="student_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update admin set Name=%s,Login_Name=%s,Password=%s,Mobile=%s where Admin_Id=%s",(
                                                                                        
                                                                            self.var_name.get(),
                                                                            self.var_lname.get(),
                                                                            self.var_pas.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_ad_id.get()
                        
                        ))
                    conn.commit()
                    fetch_data()
                    conn.close()
                    tmsg.showinfo("success","Updated succesfully",parent=self.root)
                    reset()
                    
                
                
                
            updatebtn=Button(btn_frame2,text="UPDATE",command=update,font="lucida 10",width=10,cursor="hand2")
            updatebtn.grid(row=0,column=1,padx=6,pady=4)
            
            # ==========================================================Delete button===============================================================
            
            def delete():
                if self.var_name.get()=="":
                    tmsg.showerror("Error","fill the form")
                else:
                    
                    delete=tmsg.askyesno("student Management system",f"Do You want delete this Admin name={self.var_name.get()}",parent=self.root)
                    
                    if delete>0:
                    
                        conn=mysql.connector.connect(host="localhost",username="root",password="simran2003",database="student_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("delete from admin where Admin_Id=%s",(
                            self.var_ad_id.get(),
                        ))
                        reset()
                        
                    else:
                        if not delete:
                            return
                        
                    conn.commit()
                    fetch_data()
                    conn.close()

            
            
            
            delbtn=Button(btn_frame2,text="DELETE",command=delete,font="lucida 10",width=10,cursor="hand2")
            delbtn.grid(row=0,column=2,padx=6,pady=4)
            
            # =================================================RESET================================================
            
            def reset():
               
                self.var_name.set("")
                self.var_lname.set("")
                self.var_pas.set("")
                self.var_mobile.set("")
                x=random.randint(1000,10000)
                self.var_ad_id.set(x)
                
            
            
            resbtn=Button(btn_frame2,text="RESET",command=reset,font="lucida 10",width=10,cursor="hand2")
            resbtn.grid(row=0,column=3,padx=6,pady=4)
                
                
                # =====================================================DETAIL FRAME=====================================================
            table_frame=LabelFrame(detail,text="View Details and Search System",font="lucida 16 bold",bd=2,relief=RIDGE,padx=2)
            table_frame.place(x=430,y=50,height=500,width=830)
                
                
            srh_btn=Label(table_frame,text="Search By",width=10,bg="red",font="arial 14",fg="white")
            srh_btn.grid(row=0,column=0,sticky=W,padx=2)
                
            self.search_var=StringVar()
                
            sel_combo=ttk.Combobox(table_frame,width=14,textvariable=self.search_var,font="lucida 15",state="readonly")
            sel_combo["value"]=("Admin id","mobile number")
            sel_combo.current(0)
            sel_combo.grid(row=0,column=1,padx=2)
                
            text_search=StringVar()
            entry=ttk.Entry(table_frame,textvariable=text_search,width=16,font="arial 15")
            entry.grid(row=0,column=2,padx=2)
            
            def search_admin():
                search_term = text_search.get().strip()
                search_by = self.search_var.get()

                if search_by == "Admin id":
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
            
            srh_btn=Button(table_frame,text="SEARCH",command=search_admin,cursor="hand2",width=15,bg="green",font="lucida 11",fg="white")
            srh_btn.grid(row=0,column=3,padx=2)
            
            
            detail_frame=Frame(table_frame,bd=2,relief=RIDGE)
            detail_frame.place(x=0,y=50,width=800,height=350)
            
            
            scroll_x=ttk.Scrollbar(detail_frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(detail_frame,orient=VERTICAL)
            
            
            
            self.admin_view=ttk.Treeview(detail_frame,columns=("Admin_Id","Name","Login_Name","Password","Mobile"))
            
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            
            scroll_x.config(command=self.admin_view.xview)
            scroll_y.config(command=self.admin_view.yview)
            
            self.admin_view.heading("Admin_Id",text="Admin Id")
            self.admin_view.heading("Name",text="Name")
            self.admin_view.heading("Login_Name",text="Login Name")
            self.admin_view.heading("Password",text="Password")
            self.admin_view.heading("Mobile",text="Mobile No")
            
            self.admin_view["show"]="headings"
            
            
            self.admin_view.column("Admin_Id",width=100)
            self.admin_view.column("Name",width=100)
            self.admin_view.column("Login_Name",width=100)
            self.admin_view.column("Password",width=100)
            self.admin_view.column("Mobile",width=100)
            
            
            self.admin_view.pack(fill=BOTH,expand=1)
            self.admin_view.bind("<ButtonRelease-1>",get_cursor)
            fetch_data()
            
        
        btn1=Button(btn_frame,text="ADMIN DETAILS",cursor="hand2",command=admin_details,font="lucida 16 bold",bg="black",fg="gold",width=20)
        btn1.grid(row=0,column=1,padx=54,pady=25)
#    =================================================================COURSE DETAILS==============================================  
# ==========================================================================================================================================================================   
        # def ClearScreen():
        #     for widget in detail.winfo_children():
        #         widget.destroy()
        
        def course_win():
            new_window=Toplevel(root)
            self.app=course_window(new_window)
        
        btn2=Button(btn_frame,text="COURSE DETAILS",command=course_win,cursor="hand2",font="lucida 16 bold",bg="black",fg="gold",width=20)
        btn2.grid(row=0,column=2,padx=54,pady=25)
# =================================================================Teacher details============================================================================================
        def teacher_site():
            new_window=Toplevel(root)
            self.app=teacher_win(new_window)
        btn3=Button(btn_frame,text="TEACHER DETAILS",command=teacher_site,cursor="hand2",font="lucida 16 bold",bg="black",fg="gold",width=20)
        btn3.grid(row=0,column=3,padx=54,pady=25)
# =======================================================================================STUDENT DETAIL=====================================================================
        def student_site():
            new_window=Toplevel(root)
            self.app=student_page(new_window)
        btn4=Button(btn_frame,text="STUDENT DETAILS",command=student_site,cursor="hand2",font="lucida 16 bold",bg="black",fg="gold",width=20)
        btn4.grid(row=0,column=4,padx=54,pady=25)
               
        
if __name__=="__main__":
    root=Tk()
    obj=adminpage(root)
    root.mainloop()