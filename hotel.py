from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from customer import Cust_Win
from room import Roombooking
from details import RoomDetails


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
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
