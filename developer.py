from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import tkinter as tk


class Developer:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\biga.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\bg4.png")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer Panel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)


        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\ELEXIS.jpg")
        std_img_btn=std_img_btn.resize((170,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,text="F.FALCESO",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=250,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\LEANNE.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,text="L.LOYOLA",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=480,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\EDNIE.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,text="E.GARCIA",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=710,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\Leanne France Loyola\Desktop\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\JOSH.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,text="J.GUESE",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=940,y=380,width=180,height=45)

        return_button = tk.Button(self.root, text="Return to MainApp", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
        return_button.grid(row=0,column=1,padx=15,pady=710,sticky=W)


    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

def main():
    root = tk.Tk()
    app = Developer(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()