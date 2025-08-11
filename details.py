from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class RoomDetails:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        lbl_title=Label(self.root,text="ROOM ADDING DEPARTMENT" ,font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)

# ============================ Logo =================================
        img2 = Image.open(r"C:\Users\sanja\OneDrive\Desktop\Hotel Mnagement System\images\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg_logo = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg_logo.place(x=5, y=2, width=100, height=40)

#=========================================Lable frame =========================================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)  
      
        # floor
        lbl_floor=Label(labelframeleft,text="Floor: ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,width=20,textvariable=self.var_floor,font=("arial",13,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)  

       # Room No
        lbl_RoomNo=Label(labelframeleft,text="RoomNo: ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        
        self.var_roomNo=StringVar()
        enty_RoomNo=ttk.Entry(labelframeleft,width=20,textvariable=self.var_roomNo,font=("arial",13,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        # Room Type
        lbl_room_type = Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=3, column=0, sticky=W)
        self.var_RoomType = StringVar()  
        combo_room_type = ttk.Combobox(labelframeleft,textvariable=self.var_RoomType, font=("arial", 13, "bold"), width=20, state="readonly")
        combo_room_type["values"] = ("Single", "Double", "Luxury")
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1) 

    #================================Bottons ===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

    # ========================= table frame serach system ======================================
        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details",font=("arial", 12, "bold"), padx=2)
        Table_frame.place(x=600, y=55, width=600, height=350)

    # Scrollbar
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(
        Table_frame,
        columns=("floor", "roomno", "roomType"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomType", text="Room Type")
    

        self.room_table["show"]="headings"
        for col in ("floor", "roomno", "roomType"):
            self.room_table.column(col, width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # add data
    def add_data(self):
      if self.var_floor.get() == "" or self.var_RoomType.get() == "":
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
                    "INSERT INTO details VALUES (%s, %s, %s)",
                    (
                        self.var_floor.get(),
                        self.var_roomNo.get(),
                        self.var_RoomType.get(),     
                    )
                )
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "New Room Added Successfully!!", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something Went Wrong: {str(es)}", parent=self.root)
    # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM details")
        rows = my_cursor.fetchall()
    
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert("", "end", values=row)
    
        conn.commit()
        conn.close()
    # cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])

        self.original_roomNo = row[1]

    # update data
    def update(self):
        if self.var_floor.get() =="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else: 
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE details SET Floor=%s, RoomNo=%s, RoomType=%s WHERE RoomNo=%s",
        (
            self.var_floor.get(),
            self.var_roomNo.get(),
            self.var_RoomType.get(),
            self.original_roomNo  
        )
    )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Deatils Data Has Been Updated Successfully!!",parent=self.root)

    def Delete(self):
        Delete=messagebox.askyesno("Delete","Do you want to delete this room details",parent=self.root)
        if Delete>0:         
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel_mana_system")
            my_cursor = conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
               return
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Delete", "Room Details data has been deleted successfully!", parent=self.root)
        conn.close()
    
    def reset(self):
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_RoomType.set("")

if __name__ == "__main__":
    root = Tk()
    obj = RoomDetails(root)
    root.mainloop()
