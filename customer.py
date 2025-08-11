from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

#=========================== variable ==================================

        self.var_ref=StringVar() 
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()


#===========================TITLE===========================================
        lbl_title=Label(self.root,text="ADD CUSTOMER DEATILS" ,font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)

# ============================ Logo =================================
        img2 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg_logo = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg_logo.place(x=5, y=2, width=100, height=40)
 
#=============================== Label ====================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Deatails",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

#=====================================labels and entry =========================================
       #cust ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=22,textvariable=self.var_ref,font=("arial",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

        # Customer Name
        lbl_cname = Label(labelframeleft, text="Customer Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, width=22,textvariable=self.var_cust_name, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

       # Mother's Name
        lbl_mname = Label(labelframeleft, text="Mother Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft, width=22,textvariable=self.var_mother ,font=("arial", 13, "bold"))
        txtmname.grid(row=2, column=1)

        # Gender
        label_gender = Label(labelframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("arial", 13, "bold"), width=20, state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.grid(row=3, column=1)

        #  Post Code
        lbl_postcode = Label(labelframeleft, text="PostCode", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_postcode.grid(row=4, column=0, sticky=W)
        txt_postcode = ttk.Entry(labelframeleft, width=22,textvariable=self.var_post, font=("arial", 13, "bold"))
        txt_postcode.grid(row=4, column=1)

        #  Mobile
        lbl_mobile = Label(labelframeleft, text="Mobile", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=5, column=0, sticky=W)
        txt_mobile = ttk.Entry(labelframeleft, width=22,textvariable=self.var_mobile,font=("arial", 13, "bold"))
        txt_mobile.grid(row=5, column=1)

          # Email
        lbl_email = Label(labelframeleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)
        txt_email = ttk.Entry(labelframeleft, width=22,textvariable=self.var_email, font=("arial", 13, "bold"))
        txt_email.grid(row=6, column=1)

        #  Nationality
        lbl_nationality = Label(labelframeleft, text="Nationality", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_nationality.grid(row=7, column=0, sticky=W)
        combo_nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("arial", 13, "bold"), width=20, state="readonly")
        combo_nationality["values"] = ("Indian", "American", "British", "Canadian", "Australian", "Other")
        combo_nationality.grid(row=7, column=1)


        #  ID Proof Type
        lbl_idproof = Label(labelframeleft, text="ID Proof Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_idproof.grid(row=8, column=0, sticky=W)
        combo_idproof = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, font=("arial", 13, "bold"), width=20, state="readonly")
        combo_idproof["values"] = ("AadharCard", "Passport", "Driving License", "Other")
        combo_idproof.grid(row=8, column=1)

       #  ID Number
        lbl_idnumber = Label(labelframeleft, text="ID Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_idnumber.grid(row=9, column=0, sticky=W)
        txt_idnumber = ttk.Entry(labelframeleft, width=22,textvariable=self.var_id_number,font=("arial", 13, "bold"))
        txt_idnumber.grid(row=9, column=1)

      #  Address
        lbl_address = Label(labelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)
        txt_address = ttk.Entry(labelframeleft, width=22,textvariable=self.var_address, font=("arial", 13, "bold"))
        txt_address.grid(row=10, column=1)

    #================================Bottons ===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.Reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

   #=============================== Table Frame and search system=========================================
        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",font=("arial", 12, "bold"), padx=2)
        Table_frame.place(x=435, y=50, width=860, height=490)

       # Label for Search By
        lblSearchBy = Label(Table_frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        # Combobox for Search Options
        self.search_var=StringVar()
        combo_SearchBy = ttk.Combobox(Table_frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_SearchBy["values"] = ("Mobile", "Ref")
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
        details_table.place(x=0, y=50, width=860, height=350)

        # Scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

          # Treeview
        self.Cust_Details_Table = ttk.Treeview(
        details_table,
        columns=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Customer Ref")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="ID Proof")
        self.Cust_Details_Table.heading("idnumber", text="ID Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"]="headings"
        for col in ("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"):
            self.Cust_Details_Table.column(col, width=100)
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
      if self.var_mobile.get() == "" or self.var_mother.get() == "":
          messagebox.showerror("Error", "All Fields are Required", parent=self.root)
      else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="root",
                    database="hotel_mana_system"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_ref.get(),
                        self.var_cust_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_id_proof.get(),
                        self.var_id_number.get(),
                        self.var_address.get()
                    )
                )
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Customer Has Been Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent=self.root)
            
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows = my_cursor.fetchall()
    
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for row in rows:
                self.Cust_Details_Table.insert("", "end", values=row)
    
        conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
      cursor_row=self.Cust_Details_Table.focus()
      content=self.Cust_Details_Table.item(cursor_row)
      row=content["values"]

      self.var_ref.set(row[0])
      self.var_cust_name.set(row[1])
      self.var_mother.set(row[2])
      self.var_gender.set(row[3])
      self.var_post.set(row[4])
      self.var_mobile.set(row[5])
      self.var_email.set(row[6])
      self.var_nationality.set(row[7])
      self.var_id_proof.set(row[8])
      self.var_id_number.set(row[9])
      self.var_address.set(row[10])

    def update(self):
      if self.var_mobile.get() =="":
        messagebox.showerror("Error","'Please Enter Mobile Number",parent=self.root)
      else:
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
        my_cursor = conn.cursor()
        my_cursor.execute("update customer set Name=%s,mother=%s,gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where ref=%s",
                   (
                        self.var_cust_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_id_proof.get(),
                        self.var_id_number.get(),
                        self.var_address.get(),
                        self.var_ref.get()
                  )
          )
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Customer Deatils Has Been Updated Successfully!!",parent=self.root)

    def Delete(self):
      Delete=messagebox.askyesno("Delete","Do you want to delete this data",parent=self.root)
      if Delete>0:
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
        my_cursor = conn.cursor()
        query="delete from customer where ref=%s"
        value=(self.var_ref.get(),)
        my_cursor.execute(query,value)
      else:
        if not Delete:
          return

      conn.commit()
      self.fetch_data()
      messagebox.showinfo("Delete", "Customer data has been deleted successfully!", parent=self.root)
      conn.close()

    def Reset(self):
      #self.var_ref.set("")
      self.var_cust_name.set(""),
      self.var_mother.set(""),
      #self.var_gender.set(""),
      self.var_post.set(""),
      self.var_mobile.set(""),
      self.var_email.set(""),
      # self.var_nationality.set(""),
      # self.var_id_proof.set(""),
      self.var_id_number.set(""),
      self.var_address.set("")
    
      x=random.randint(1000,9999)
      self.var_ref.set(str(x))

    def search(self):
      conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
      my_cursor = conn.cursor()
      my_cursor.execute("SELECT * FROM customer WHERE " + str(self.search_var.get()) + " LIKE %s", ('%' + str(self.txt_search.get()) + '%',))
      rows=my_cursor.fetchall()
      if len(rows)!=0:
        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
        for i in rows:
          self.Cust_Details_Table.insert("",END,values=i)
      conn.close()

      

if __name__ == "__main__":
    root= Tk()
    obj=Cust_Win(root)
    root.mainloop()