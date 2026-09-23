from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Payment:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System - Payment")
        self.root.geometry("1295x550+230+220")
    
        # Variables
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_roomno=StringVar()
        self.var_total_amount=StringVar()
        self.var_payment_method=StringVar()
        self.var_amount_paid=StringVar()

        # Title
        lbl_title=Label(self.root,text="PAYMENT DETAILS" ,font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # Logo
        img2 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg_logo = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg_logo.place(x=5, y=2, width=100, height=40)

        # LabelFrame Left
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Payment Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)  

        # Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact: ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)  

        btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.fetch_data,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=340,y=4)  

        # Name
        lbl_name = Label(labelframeleft, text="Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_name.grid(row=1, column=0, sticky=W)
        txt_name = ttk.Entry(labelframeleft, width=22,textvariable=self.var_name,font=("arial", 13, "bold"), state="readonly")
        txt_name.grid(row=1, column=1)

        # Room No
        lbl_roomno = Label(labelframeleft, text="Room No:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_roomno.grid(row=2, column=0, sticky=W)
        txt_roomno = ttk.Entry(labelframeleft, width=22,textvariable=self.var_roomno, font=("arial", 13, "bold"), state="readonly")
        txt_roomno.grid(row=2, column=1)

        # Total Amount
        lbl_total = Label(labelframeleft, text="Total Amount:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_total.grid(row=3, column=0, sticky=W)
        txt_total = ttk.Entry(labelframeleft, width=22,textvariable=self.var_total_amount, font=("arial", 13, "bold"), state="readonly")
        txt_total.grid(row=3, column=1)

        # Payment Method
        lbl_method = Label(labelframeleft, text="Payment Method:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_method.grid(row=4, column=0, sticky=W)
        combo_method = ttk.Combobox(labelframeleft,textvariable=self.var_payment_method, font=("arial", 13, "bold"), width=20, state="readonly")
        combo_method["values"] = ("Cash", "Credit Card", "Debit Card", "UPI", "Net Banking")
        combo_method.current(0)
        combo_method.grid(row=4, column=1)

        # Amount Paid
        lbl_paid = Label(labelframeleft, text="Amount Paid:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_paid.grid(row=5, column=0, sticky=W)
        txt_paid = ttk.Entry(labelframeleft, width=22,textvariable=self.var_amount_paid,font=("arial", 13, "bold"))
        txt_paid.grid(row=5, column=1)

        # Buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnPay=Button(btn_frame,text="Pay & Save",command=self.save_payment,font=("arial",12,"bold"),bg="black",fg="gold",width=13)
        btnPay.grid(row=0,column=0,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=13)
        btnReset.grid(row=0,column=1,padx=1)

        # Table Frame
        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Payment Records",font=("arial", 12, "bold"), padx=2)
        Table_frame.place(x=435, y=50, width=860, height=490)

        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=10, width=850, height=450)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.payment_table = ttk.Treeview(details_table, columns=("contact", "name", "roomno", "total_amount", "method", "amount_paid", "date"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.payment_table.xview)
        scroll_y.config(command=self.payment_table.yview)

        self.payment_table.heading("contact", text="Contact")
        self.payment_table.heading("name", text="Name")
        self.payment_table.heading("roomno", text="Room No")
        self.payment_table.heading("total_amount", text="Total Bill")
        self.payment_table.heading("method", text="Payment Method")
        self.payment_table.heading("amount_paid", text="Amount Paid")
        self.payment_table.heading("date", text="Date")

        self.payment_table["show"]="headings"
        self.payment_table.column("contact", width=100)
        self.payment_table.column("name", width=100)
        self.payment_table.column("roomno", width=80)
        self.payment_table.column("total_amount", width=100)
        self.payment_table.column("method", width=100)
        self.payment_table.column("amount_paid", width=100)
        self.payment_table.column("date", width=100)

        self.payment_table.pack(fill=BOTH,expand=1)
        
        self.fetch_all_payments()

    def fetch_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please Enter Contact Number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
                my_cursor = conn.cursor()
                
                # Fetch Name from customer
                my_cursor.execute("SELECT Name FROM customer WHERE Mobile=%s", (self.var_contact.get(),))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Contact Number Not found in Customers!", parent=self.root)
                    return
                self.var_name.set(row[0])

                # Fetch Room Details from room
                my_cursor.execute("SELECT roomtype, roomavailable, meal, noOfdays FROM room WHERE contact=%s", (self.var_contact.get(),))
                room_row = my_cursor.fetchone()
                if room_row is None:
                    messagebox.showerror("Error", "No Room Booked for this Contact!", parent=self.root)
                    return
                
                roomtype, roomavailable, meal, days = room_row
                self.var_roomno.set(roomavailable)

                # Calculate Total Bill
                meal_prices = {"Breakfast": 300, "Lunch": 500, "Dinner": 700, "All": 1500}
                room_prices = {"Single": 2000, "Double": 3000, "Luxury": 4000}

                meal_cost = meal_prices.get(meal, 0) if meal != "All" else meal_prices["All"]
                room_cost = room_prices.get(roomtype, 0)

                total = (meal_cost + room_cost) * float(days)
                tax = total * 0.09
                final_amt = total + tax

                self.var_total_amount.set("Rs." + str("%.2f" % final_amt))
                self.var_amount_paid.set(str("%.2f" % final_amt)) # Default to full amount
                
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def save_payment(self):
        if self.var_contact.get() == "" or self.var_amount_paid.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
                my_cursor = conn.cursor()
                
                current_date = datetime.now().strftime("%d/%m/%Y")
                
                my_cursor.execute(
                    "INSERT INTO payment (contact, name, roomno, total_amount, method, amount_paid, date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_contact.get(),
                        self.var_name.get(),
                        self.var_roomno.get(),
                        self.var_total_amount.get(),
                        self.var_payment_method.get(),
                        self.var_amount_paid.get(),
                        current_date
                    )
                )
                conn.commit()
                conn.close()
                self.fetch_all_payments()
                messagebox.showinfo("Success", "Payment Has Been Saved", parent=self.root)
            except Exception as es:
                # E.g. table might not exist
                messagebox.showwarning("Warning", f"Something Went Wrong (Did you create the payment table?): {str(es)}", parent=self.root)

    def fetch_all_payments(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM payment")
            rows = my_cursor.fetchall()
            
            self.payment_table.delete(*self.payment_table.get_children())
            if len(rows) != 0:
                for row in rows:
                    self.payment_table.insert("", "end", values=row)
            conn.commit()
            conn.close()
        except:
            pass # Ignore if table doesn't exist yet

    def reset(self):
        self.var_contact.set("")
        self.var_name.set("")
        self.var_roomno.set("")
        self.var_total_amount.set("")
        self.var_payment_method.set("")
        self.var_amount_paid.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Payment(root)
    root.mainloop()
