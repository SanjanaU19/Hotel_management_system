from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
    
# ============================================Variable ===============================================
        self.var_contact=StringVar()
        self.var_check_in_date=StringVar()
        self.var_check_out_date=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal = StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()    
        self.var_actualamount=StringVar()      
        self.var_total=StringVar()     

#===========================TITLE===========================================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS" ,font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)

# ============================ Logo =================================
        img2 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg_logo = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg_logo.place(x=5, y=2, width=100, height=40)

#=========================================Lable frame =========================================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Deatails",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)  

#=====================================labels and entry =========================================
      #cust ref
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact: ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)  

   #================================ Fetch Data Button =============================================
        btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=340,y=4)  

    # Check-in Date
        check_in_date = Label(labelframeleft, text="Check-in Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txt_check_in_date = ttk.Entry(labelframeleft, width=22,textvariable=self.var_check_in_date,font=("arial", 13, "bold"))
        txt_check_in_date.grid(row=1, column=1)

       # Check-out Date
        check_out_date = Label(labelframeleft, text="Check-out Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        txt_check_out_date = ttk.Entry(labelframeleft, width=22,textvariable=self.var_check_out_date, font=("arial", 13, "bold"))
        txt_check_out_date.grid(row=2, column=1)

     # Room Type
        lbl_room_type = Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect( host="localhost",username="root",password="root",database="hotel_mana_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_room_type = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial", 13, "bold"), width=20, state="readonly")
        combo_room_type["values"] = ide
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)

    # Available Room
        lbl_room_available = Label(labelframeleft, text="Available Room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_available.grid(row=4, column=0, sticky=W)
        # txt_room_available = ttk.Entry(labelframeleft, width=22,textvariable=self.var_roomavailable, font=("arial", 13, "bold"))
        # txt_room_available.grid(row=4, column=1)
        
        conn = mysql.connector.connect( host="localhost",username="root",password="root",database="hotel_mana_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=20, state="readonly")
        combo_RoomNo["values"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

    # Meal
        lbl_meal = Label(labelframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)
        txt_meal = ttk.Entry(labelframeleft, width=22,textvariable=self.var_meal, font=("arial", 13, "bold"))
        txt_meal.grid(row=5, column=1)

      # No of Days
        lbl_days = Label(labelframeleft, text="No of Days:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_days.grid(row=6, column=0, sticky=W)
        txt_days = ttk.Entry(labelframeleft, width=22,textvariable=self.var_noofdays, font=("arial", 13, "bold"))
        txt_days.grid(row=6, column=1)

         # Paid Tax
        lbl_tax = Label(labelframeleft, text="Paid Tax:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_tax.grid(row=7, column=0, sticky=W)
        txt_tax = ttk.Entry(labelframeleft, width=22,textvariable=self.var_paidtax, font=("arial", 13, "bold"))
        txt_tax.grid(row=7, column=1)

        # Sub Total
        lbl_sub_total = Label(labelframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_sub_total.grid(row=8, column=0, sticky=W)
        txt_sub_total = ttk.Entry(labelframeleft, width=22,textvariable=self.var_actualamount,font=("arial", 13, "bold"))
        txt_sub_total.grid(row=8, column=1)

          # Total Cost
        lbl_total = Label(labelframeleft, text="Total Cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_total.grid(row=9, column=0, sticky=W)
        txt_total = ttk.Entry(labelframeleft, width=22,textvariable=self.var_total, font=("arial", 13, "bold"))
        txt_total.grid(row=9, column=1)

   # =============================== Bill btn ====================================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

    #================================Bottons ===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

    #============================================Right side image ============================================================
        img3 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\bed.jpg")
        img3 = img3.resize((520, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg_logo = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg_logo.place(x=760, y=55, width=520, height=220)

    #=============================== Table Frame and search system=========================================
        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",font=("arial", 12, "bold"), padx=2)
        Table_frame.place(x=435, y=280, width=860, height=260)

       # Label for Search By
        lblSearchBy = Label(Table_frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        # Combobox for Search Options
        self.search_var=StringVar()
        combo_SearchBy = ttk.Combobox(Table_frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_SearchBy["values"] = ("Contact", "Room")
        combo_SearchBy.current(0)
        combo_SearchBy.grid(row=0, column=1, padx=5, pady=10)
 
        self.txt_search=StringVar()
        txt_search = ttk.Entry(Table_frame, width=24,textvariable=self.txt_search, font=("arial", 13, "bold"))
        txt_search.grid(row=0, column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)
        
# ==================================== Show data Table =====================================
        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        # Scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

          # Treeview
        self.room_table = ttk.Treeview(
        details_table,
        columns=("contact", "check_in_date", "check_out_date", "roomtype", "roomavailable", "meal", "noOfdays"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("check_in_date", text="Check-in")
        self.room_table.heading("check_out_date", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")

        self.room_table["show"]="headings"
        for col in ("contact", "check_in_date", "check_out_date", "roomtype", "roomavailable", "meal", "noOfdays"):
            self.room_table.column(col, width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

   # add data 
    def add_data(self):
      if self.var_contact.get() == "" or self.var_check_in_date.get() == "":
          messagebox.showerror("Error", "All Fields are Required", parent=self.root)
      else:
            try:
                conn = mysql.connector.connect( host="localhost",username="root",password="root",database="hotel_mana_system")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO room VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_contact.get(),
                        self.var_check_in_date.get(),
                        self.var_check_out_date.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noofdays.get()       
                    )
                )
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Customer Has Been Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent=self.root)
      
      # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM room")
        rows = my_cursor.fetchall()
    
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert("", "end", values=row)
    
        conn.commit()
        conn.close()
    # get_cursor
    def get_cursor(self,event=""):
      cursor_row=self.room_table.focus()
      content=self.room_table.item(cursor_row)
      row=content["values"]

      self.var_contact.set(row[0]),
      self.var_check_in_date.set(row[1]),
      self.var_check_out_date.set(row[2]),
      self.var_roomtype.set(row[3]),
      self.var_roomavailable.set(row[4]),
      self.var_meal.set(row[5]),
      self.var_noofdays.set(row[6]) 

    # update
    def update(self):

        if self.var_contact.get() =="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else: 
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",
                   (
                        self.var_check_in_date.get(),
                        self.var_check_out_date.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noofdays.get(),
                        self.var_contact.get()
                  )
          )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Deatils Data Has Been Updated Successfully!!",parent=self.root)

    # delete function
    def Delete(self):
        Delete=messagebox.askyesno("Delete","Do you want to delete this data",parent=self.root)
        if Delete>0:         
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
            my_cursor = conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
               return
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Delete", "Customer data has been deleted successfully!", parent=self.root)
        conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_check_in_date.set("")
        self.var_check_out_date.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualamount.set("")
        self.var_total.set("")

   # ===================================== All data fetch ====================================
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
            my_cursor = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not found!",parent=self.root)
            else:
                conn.commit()
                conn.close()  

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=455,y=55,width=300,height=220)   

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
               
    # ==================Gender================================
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
                my_cursor = conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
        
       # =========================== email ==========================================
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
                my_cursor = conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)

        # ============================= Nationality ===================================
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
                my_cursor = conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)

       # ================================= Address ==================================================
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
                my_cursor = conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=120)  

       # ===================================== Id Number =========================================================
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
                my_cursor = conn.cursor()
                query=("select Idproof from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Id Proof:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=150)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=150)            

       # ===================================== Id Number =========================================================
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
                my_cursor = conn.cursor()
                query=("select Idnumber from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Id Number:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=180)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=180)  

        # ============== Search System ===============================
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM room WHERE " + str(self.search_var.get()) + " LIKE %s", ('%' + str(self.txt_search.get()) + '%',))
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
        conn.close()       

    def total(self):
        inDate=self.var_check_in_date.get()
        outDate=self.var_check_out_date.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")       
        outDate=datetime.strptime(outDate,"%d/%m/%Y")   
        self.var_noofdays.set(abs(outDate-inDate).days) 

        days = float(self.var_noofdays.get())
        room_type = self.var_roomtype.get()
        meal = self.var_meal.get()

       # Define prices
        meal_prices = {
           "Breakfast": 300,
            "Lunch": 500,
            "Dinner": 700,
            "All": 1500  # Breakfast + Lunch + Dinner
       }

        room_prices = {
            "Single": 2000,
            "Double": 3000,
            "Luxury": 4000
        }

    # Determine meal cost
        if meal == "All":
            meal_cost = meal_prices["All"]
        else:
            meal_cost = meal_prices.get(meal, 0)

    # Determine room cost
        room_cost = room_prices.get(room_type, 0)

    # Calculate cost per day and total
        per_day_total = meal_cost + room_cost
        total_cost = per_day_total * days
        tax = total_cost * 0.09

    # Update values
        self.var_paidtax.set("Rs." + str("%.2f" % tax))
        self.var_actualamount.set("Rs." + str("%.2f" % total_cost))
        self.var_total.set("Rs." + str("%.2f" % (total_cost + tax)))
         
if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
