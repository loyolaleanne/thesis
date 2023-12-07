import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from helpsupport import Helpsupport
from school_info import Schoolinfo


class MainApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1366x768+0+0")

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
        title_lb1 = Label(bg_img,text="ATTENDANCE USING FACIAL RECOGNITION",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)


       # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student
        std_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\stdpanel1.jpg")
        std_img_btn=std_img_btn.resize((170,170),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.open_window1,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=100,width=180,height=180)

        std_b1 = tk.Button(self.root, text="Student Panel", command=self.open_window1,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1.place(x=252,y=412,width=180,height=45)



        # Face Recog
        det_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\stdfacerecog.png")
        det_img_btn=det_img_btn.resize((160,160),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.open_window2,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=100,width=180,height=180)
        det_b1 = tk.Button(self.root, text="Face Detector", command=self.open_window2,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1.place(x=482,y=412,width=180,height=45)


        # Data Train
        trai_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\tra1.jpg")
        trai_img_btn=trai_img_btn.resize((180,180),Image.LANCZOS)
        self.trai_img1=ImageTk.PhotoImage(trai_img_btn)

        trai_b1 = Button(bg_img,command=self.open_window3,image=self.trai_img1,cursor="hand2",)
        trai_b1.place(x=710,y=100,width=180,height=180)
        
        trai_b1 = tk.Button(self.root, text="Data Train", command=self.open_window3,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        trai_b1.place(x=712,y=412,width=180,height=45)

         # Attendance
        att_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\stdattendance.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.open_window4,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=250,y=330,width=180,height=180)

        att_b1 = tk.Button(self.root, text="Attendance", command=self.open_window4, cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1.place(x=252,y=643,width=180,height=45)


        # Help Support
        hlp_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\hlp.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.open_window5,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=100,width=180,height=180)

        hlp_b1_1 = tk.Button(self.root, text="Help Support", command=self.open_window5,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=942,y=412,width=180,height=45)

        # School Info


        pho_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\schoolinfo.png")
        pho_img_btn=pho_img_btn.resize((140,140),Image.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_window6,image=self.pho_img1,cursor="hand2")
        pho_b1.place(x=480,y=330,width=180,height=180)
        pho_b1_1 = tk.Button(self.root, text="School Info", command=self.open_window6,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=482,y=643,width=180,height=45)

        # Developer
        dev_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\dev.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.LANCZOS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.open_window7,image=self.dev_img1,cursor="hand2")
        dev_b1.place(x=710,y=330,width=180,height=180)

        dev_b1 = tk.Button(self.root, text="Developers", command=self.open_window7,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        dev_b1.place(x=712,y=643,width=180,height=45)

        # Exit
        exi_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.open_window8,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=940,y=330,width=180,height=180)


        exi_b1_1 = tk.Button(self.root, text="Exit", command=self.open_window8,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=942,y=643,width=180,height=45)
    
    def open_window1(self):
        self.root.withdraw()
        self.window1 = tk.Toplevel(self.root)
        self.disable_close_button(self.window1)
        self.app1 = Student(self.window1, self.show_main_app)

    def open_window2(self):
        self.root.withdraw()
        self.window2 = tk.Toplevel(self.root)
        self.disable_close_button(self.window2)
        self.app2 = Face_Recognition(self.window2, self.show_main_app)
    
    def open_window3(self):
        self.root.withdraw()
        self.window3 = tk.Toplevel(self.root)
        self.disable_close_button(self.window3)
        self.app3 = Train(self.window3, self.show_main_app)

    def open_window4(self):
        self.root.withdraw()
        self.window4 = tk.Toplevel(self.root)
        self.disable_close_button(self.window4)
        self.app4 = Attendance(self.window4, self.show_main_app)
    
    def open_window5(self):
        self.root.withdraw()
        self.window5 = tk.Toplevel(self.root)
        self.disable_close_button(self.window5)
        self.app5 = Helpsupport(self.window5, self.show_main_app)
    
    def open_window6(self):
        self.root.withdraw()
        self.window6 = tk.Toplevel(self.root)
        self.disable_close_button(self.window6)
        self.app6 = Schoolinfo(self.window6, self.show_main_app)
    
    def open_window7(self):
        self.root.withdraw()
        self.window7 = tk.Toplevel(self.root)
        self.disable_close_button(self.window7)
        self.app7 = Developer(self.window7, self.show_main_app)

    def open_window8(self):
        self.root.withdraw()
        self.window8 = tk.Toplevel(self.root)
        self.disable_close_button(self.window8)
        self.app8 = Developer(self.window8, self.show_main_app)
        self.root.destroy()

    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked

    def show_main_app(self):
        self.root.deiconify()  # Show the main window
        # Destroy child windows when returning to MainApp
        if hasattr(self, 'window1'):
            self.window1.destroy()
        if hasattr(self, 'window2'):
            self.window2.destroy()
        if hasattr(self, 'window3'):
            self.window3.destroy()
        if hasattr(self, 'window4'):
            self.window4.destroy()
        if hasattr(self, 'window5'):
            self.window5.destroy()
        if hasattr(self, 'window6'):
            self.window6.destroy()
        if hasattr(self, 'window7'):
            self.window7.destroy()
        if hasattr(self, 'window8'):
            self.window8.destroy()
    

    









def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

