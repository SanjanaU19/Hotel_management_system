from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
from time import strftime
from datetime import datetime
import mysql.connector
from hotel import HotelManagementSystem
from customer import Cust_Win
from room import Roombooking
from details import RoomDetails

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.var_email = StringVar()
        self.var_pass = StringVar()

#============================ Images ===================================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new romn",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # lable

        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=185,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

    # ========================== Icon images =========================================
        img2=Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=394,width=25,height=25)

    # login btn
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

    # register btn
        registerbtn=Button(frame,text="New User Register",command=self.register_window,borderwidth=0,font=("times new roman",10,"bold"),relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        # forgot password btn
        forgotpasswordbtn=Button(frame,text="Forgot Password",command=self.forgot_passward_window,borderwidth=0,font=("times new roman",10,"bold"),relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpasswordbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

    # Hardcoded admin login for testing
        if username == "kapu" and password == "ashu":
            messagebox.showinfo("Success", "Welcome!!")
            return

    # Database login
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_mana_system")
            my_cursor = conn.cursor()

            query = "SELECT * FROM register WHERE email=%s AND password=%s"
            my_cursor.execute(query, (username, password))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only Admin")
                if open_main:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

 # ====================================== reset password ===========================================

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the security question",parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the Answer",parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the password",parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_mana_system")
                my_cursor = conn.cursor()

                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                values = (self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
                my_cursor.execute(query, values)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Please enter the correct Answer",parent=self.root2)
                else:
                    update_query = "UPDATE register SET password=%s WHERE email=%s"
                    update_values = (self.txt_newpass.get(), self.txtuser.get())
                    my_cursor.execute(update_query, update_values)

                    conn.commit()
                    messagebox.showinfo( "Info", "Your password has been reset successfully! Please login with your new password.",parent=self.root2)
                conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
        self.root2.destroy()

    def forgot_passward_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password") 
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_mana_system")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)    

            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")      
            else:  
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="red")
                security_Q.place(x=50,y=80)
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth place","Your Birth Date","Your Best Friend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="red")
                security_A.place(x=50,y=160)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=190,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="red")
                new_password.place(x=50,y=240)
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=270,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass ,font=("times new roman",15,"bold"),fg="white",bg="black")
                btn.place(x=100,y=330)
            
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # ================= varibles =============================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #background image 
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # left side image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl = Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
    #======================main frame ========================================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        #register label
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

    #================== label entry ==============================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        # Row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

       # Row - 3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth place","Your Birth Date","Your Best Friend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        # row - 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        cpswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        cpswd.place(x=370,y=310)
        self.txt_cpswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_cpswd.place(x=370,y=340,width=250)

        # ====================== Check btn ===================================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,text="I Agree Terms & Condition",variable=self.var_check,font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=400)

        #=========================== btn ==============================================
        img=Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\register-now-button1.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=40,y=450,width=200)

        img1=Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\loginpng.png")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=450,width=200)

    #============================== fuction declartion ======================================\
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our Terms & Condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_mana_system")
            my_cursor=conn.cursor()
            query=("Select*from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist please try another email!")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully!!",parent=self.root)
    def return_login(self):
        self.root.destroy()
        

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ================= Top Banner Image ===================
        img1 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\top1.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ================== Logo ==================
        img2 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\logohotel.png")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg_logo = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg_logo.place(x=0, y=0, width=230, height=140)

        # ================= Title ==================
        lbl_title = Label(self.root, text="Tara Hotel", font=("Times New Roman", 40, "bold"),bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ================= Main Frame ==================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ================= Menu Label ==================
        lbl_menu = Label(main_frame, text="MENU", font=("Times New Roman", 20, "bold"),bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ================= Button Frame ==================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details,width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.room_booking_details, width=22, font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22,command=self.details_room, font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22,font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22,font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # ================ Right Side Image =================
        img3 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\san.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=230, y=0, width=1310, height=590)

        # ================ Bottom Images =================
        img4 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\myh.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\khana.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg3 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg3.place(x=0, y=420, width=230, height=190)

    # ================ Customer Window ================
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def room_booking_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomDetails(self.new_window)
      


if __name__ == "__main__":
    main()
    
