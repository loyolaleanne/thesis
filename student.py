from tkinter import* 
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkcalendar import *
from tkinter import ttk
from tkinter import Tk
# from main2 import Face_Recognition_System1


# Testing Connection 
"""
conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Student:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")

        # self.root.state('zoomed')
        # self.root.attributes('-fullscreen',True)



        #-----------Variables-------------------
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_std_mname=StringVar()
        self.var_std_lname=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        def pick_date(event):
            global cal, delete_window
            
            date_window = Toplevel()
            date_window.grab_set()
            date_window.title('Choose Date of Birth')
            date_window.geometry('250x220+590+370')
            cal = Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")
            cal.place(x=0, y=0)

            submit_btn = Button(date_window, text="Submit", command=grab_date)
            submit_btn.place(x=80, y=190)

        def grab_date():
            student_dob_entry.delete(0, END)
            student_dob_entry.insert(0, cal.get_date())
            delete_window.destroy()
            

    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\biga.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

         # backgorund image 
        bg1=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Student Panel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)


        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1400,height=510)

        self.return_button = tk.Button(self.root, text="Return to MainApp", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
        self.return_button.grid(row=0,column=1,padx=15,pady=710,sticky=W)
        # self.return_button.pack()

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        #Class Student Information
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",12,"bold"),fg="navyblue")
        class_Student_frame.place(x=10,y=10,width=635,height=370)

        #Student id
        studentId_label = Label(class_Student_frame,text="Student ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #Student first name
        student_name_label = Label(class_Student_frame,text="First Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        #Middle Name
        student_mname_label = Label(class_Student_frame,text="Middle Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_mname_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)

        student_mname_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_mname,width=15,font=("verdana",12,"bold"))
        student_mname_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        #Last Name
        student_lname_label = Label(class_Student_frame,text="Last Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_lname_label.grid(row=3,column=0,padx=5,pady=10,sticky=W)

        student_lname_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_lname,width=15,font=("verdana",12,"bold"))
        student_lname_entry.grid(row=3,column=1,padx=5,pady=10,sticky=W)

        #Class Didvision
        student_div_label = Label(class_Student_frame,text="Schedule:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_div_label.grid(row=3,column=2,padx=5,pady=10,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=13,font=("verdana",12,"bold"),state="readonly")
        div_combo["values"]=("Morning","Afternoon")
        div_combo.current(0)
        div_combo.grid(row=3,column=3,padx=5,pady=5,sticky=W)
        
        #Roll No
        student_roll_label = Label(class_Student_frame,text="LRN:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=4,column=2,padx=5,pady=10,sticky=W)
        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=4,column=3,padx=5,pady=10,sticky=W)
        
        # Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_gender_label.grid(row=1,column=2,padx=5,pady=10,sticky=W)

        # combo box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)


        #Date of Birth
        student_dob_label = Label(class_Student_frame,text="Birthday:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_dob_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        student_dob_entry = Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("verdana",12,"bold"))
        student_dob_entry.insert(0,"mm/dd/yyyy")
        student_dob_entry.bind("<1>", pick_date)
        student_dob_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)


        #Email
        student_email_label = Label(class_Student_frame,text="Grade/Sec:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=4,column=0,padx=5,pady=10,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        student_email_entry.grid(row=4,column=1,padx=5,pady=10,sticky=W)


        #Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_address_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        student_address_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)

        #Teacher Name
        student_tutor_label = Label(class_Student_frame,text="Adviser:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_tutor_label.grid(row=5,column=2,padx=5,pady=10,sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("verdana",12,"bold"))
        student_tutor_entry.grid(row=5,column=3,padx=5,pady=10,sticky=W)
        

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=7,column=0,padx=5,pady=10,sticky=W)

        radiobtn1=ttk.Radiobutton(class_Student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn1.grid(row=7,column=1,padx=5,pady=10,sticky=W)

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        #update photo button
        update_photo_btn=Button(btn_frame,text="Update Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)
        
        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Records",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=480)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=635,height=80)

        #Search
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","LRN")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("ID","Name","mName","lName","Div","Gender","DOB","Address","Roll-No","Email","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="First Name")
        self.student_table.heading("mName",text="Middle Name")
        self.student_table.heading("lName",text="Last Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="Birthday")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Roll-No",text="LRN")
        self.student_table.heading("Email",text="Grade & Section")
        self.student_table.heading("Teacher",text="Adviser")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"


        # Set Width of Colums 
        self.student_table.column("ID",width=60)
        self.student_table.column("Name",width=90)
        self.student_table.column("mName",width=90)
        self.student_table.column("lName",width=90)
        self.student_table.column("Div",width=90)
        self.student_table.column("Gender",width=90)
        self.student_table.column("DOB",width=120)
        self.student_table.column("Address",width=90)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Email",width=90)
        self.student_table.column("Teacher",width=90)
        self.student_table.column("Photo",width=90)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


   

# ==================Function Decleration==============================
    
    def return_to_main_app(self):
        self.root.withdraw()
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()
        

    def add_data(self):
        if self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_std_mname.get()=="" or self.var_std_lname.get()=="" or self.var_div.get()=="" or self.var_gender.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_std_mname.get(),
                self.var_std_lname.get(),
                self.var_div.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_std_mname.set(data[2]),
        self.var_std_lname.set(data[3]),
        self.var_div.set(data[4]),
        self.var_gender.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_address.set(data[7]),
        self.var_roll.set(data[8]),
        self.var_email.set(data[9]),
        self.var_teacher.set(data[10]),
        self.var_radio1.set(data[11])
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_std_mname.get()=="" or self.var_std_lname.get()=="" or   self.var_div.get()=="" or self.var_gender.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Name=%s,mName=%s,lName=%s,Division=%s,Gender=%s,DOB=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_std_mname.get(),
                    self.var_std_lname.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_std_mname.set(""),
        self.var_std_lname.set(""),
        self.var_div.set("Morning"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    
    # ===========================Search Data===================


    def search_data(self):
        if self.var_search.get() == "" or self.var_searchTX.get() == "Select":
            messagebox.showerror("Error", "Select Combo option and enter entry box", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
                my_cursor = conn.cursor()

                sql = "SELECT Student_ID, Name, mName, lName, Division, Gender, DOB, Address, Roll_No, Email, Teacher_Name, PhotoSample FROM student WHERE Roll_No = %s"
                params = (str(self.var_search.get()),)
                my_cursor.execute(sql, params)

                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                else:
                    messagebox.showerror("Error", "Data Not Found", parent=self.root)

                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_roll.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Name=%s,mName=%s,lName=%s,Division=%s,Gender=%s,DOB=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_std_mname.get(),
                    self.var_std_lname.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data_img/stdudent."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


def main():
    root = tk.Tk()
    app = Student(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()