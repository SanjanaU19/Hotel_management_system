from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from hotel import HotelManagementSystem
from customer import Cust_Win
from room import Roombooking
from details import RoomDetails

# ========================= Main =========================
def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

# ========================= Login Window =========================
class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.var_email = StringVar()
        self.var_pass = StringVar()

        # ================= Background Image =================
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # ================= Frame =================
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # ================= Icon Image =================
        img1 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # ================= Username =================
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=185, width=270)

        # ================= Password =================
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # ================= Login Button =================
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # ================= Register Button =================
        registerbtn = Button(frame, text="New User Register", command=self.register_window, borderwidth=0,
                             font=("times new roman", 10, "bold"), fg="white", bg="black", activeforeground="white",
                             activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # ================= Forgot Password Button =================
        forgotpasswordbtn = Button(frame, text="Forgot Password", command=self.forgot_passward_window, borderwidth=0,
                                   font=("times new roman", 10, "bold"), fg="white", bg="black", activeforeground="white",
                                   activebackground="black")
        forgotpasswordbtn.place(x=10, y=370, width=160)

    # ================= Register Window =================
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    # ================= Login Function =================
    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        # ----- Hardcoded Admin Login -----
        if username == "kapu" and password == "ashu":
            messagebox.showinfo("Success", "Welcome Admin!")
            self.new_window = Toplevel(self.root)
            self.app = HotelManagementSystem(self.new_window)
            return

        # ----- Database Login -----
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
            my_cursor = conn.cursor()

            query = "SELECT * FROM register WHERE email=%s AND password=%s"
            my_cursor.execute(query, (username, password))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                messagebox.showinfo("Success", "Login Successful!")
                self.new_window = Toplevel(self.root)
                self.app = HotelManagementSystem(self.new_window)

            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    # ================= Forgot Password =================
    def forgot_passward_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the Email address to reset password")
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            my_cursor.execute(query, (self.txtuser.get(),))
            row = my_cursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Error", "Invalid user")
            else:
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white").place(x=0, y=10, relwidth=1)

                Label(self.root2, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="red").place(x=50, y=80)
                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth place", "Your Birth Date", "Your Best Friend Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="red").place(x=50, y=160)
                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=190, width=250)

                Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="red").place(x=50, y=240)
                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=270, width=250)

                Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"), fg="white", bg="black").place(x=100, y=330)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    # ================= Reset Password =================
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the security question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the Answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the password", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                my_cursor.execute(query, (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get()))
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Incorrect security answer", parent=self.root2)
                else:
                    my_cursor.execute("UPDATE register SET password=%s WHERE email=%s", (self.txt_newpass.get(), self.txtuser.get()))
                    conn.commit()
                    messagebox.showinfo("Success", "Password reset successfully", parent=self.root2)

                conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

        self.root2.destroy()


# ================= Register Window =================
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # ================= Variables =================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Left side image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\thought-good-morning-messages-LoveSove.jpg")
        Label(self.root, image=self.bg1).place(x=50, y=100, width=470, height=550)

        # Main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white").place(x=20, y=20)

        # First Name
        Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=100)
        ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold")).place(x=50, y=130, width=250)

        # Last Name
        Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=100)
        ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15)).place(x=370, y=130, width=250)

        # Contact
        Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=170)
        ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15)).place(x=50, y=200, width=250)

        # Email
        Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=170)
        ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15)).place(x=370, y=200, width=250)

        # Security Q
        Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth place", "Your Birth Date", "Your Best Friend Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        # Security A
        Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=240)
        ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15)).place(x=370, y=270, width=250)

        # Password
        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=310)
        ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15)).place(x=50, y=340, width=250)

        # Confirm Password
        Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=310)
        ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15)).place(x=370, y=340, width=250)

        # Terms Checkbox
        self.var_check = IntVar()
        Checkbutton(frame, text="I Agree Terms & Condition", variable=self.var_check, font=("times new roman", 12, "bold"), onvalue=1, offvalue=0).place(x=50, y=400)

        # Register Button
        img = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\register-now-button1.jpg").resize((200, 50), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2").place(x=40, y=450, width=200)

        # Return to Login
        img1 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\loginpng.png").resize((200, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        Button(frame, image=self.photoimage1, command=self.return_login, borderwidth=0, cursor="hand2").place(x=330, y=450, width=200)

    # ================= Register Data =================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be Same")
            return
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to Terms & Condition")
            return
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s", (self.var_email.get(),))
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists!")
            else:
                my_cursor.execute("INSERT INTO register VALUES(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                messagebox.showinfo("Success", "Registered Successfully!!", parent=self.root)
            conn.close()

    def return_login(self):
        self.root.destroy()


# ================= Run Main =================
if __name__ == "__main__":
    main()
