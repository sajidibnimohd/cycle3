import tkinter as tk
import connection


class emp_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#ffc9e7')
        label = tk.Label(self, text="Employee PAGE", font="none 12 bold")
        label.pack()

        func = tk.Button(self, text = "Add a new station", command = lambda: self.controller.show_frame("add_station"))
        func.pack(pady=10)
        addbook = tk.Button(self, text = "Add New Employee", command = lambda: self.controller.show_frame("add_employee"))
        addbook.pack(pady=10)
        delbook = tk.Button(self, text = "Remove an Employee", command = lambda: self.controller.show_frame("del_employee"))
        delbook.pack(pady=10)

        btn = tk.Button(self, text = "Go back to home page", command = lambda: controller.show_frame('login'))
        btn.pack(pady=20)


class add_station(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#ffc9e7')
        label = tk.Label(self, text="Add New Customer", font="none 12 bold")
        label.pack(side="top", fill="x", pady=10)
        welcome_msg = tk.Label(self, text = "Welcome! Please enter your details", font = "none 12 bold")
        welcome_msg.pack()

        sname = tk.Label(self, text = "Station Name: ", font = "none 12 bold")
        sname_t = tk.Entry(self, width = 30, bg = "white")
        sname.pack()
        sname_t.pack()
        sid = tk.Label(self, text = "Station ID: ", font = "none 12 bold")
        sid_t = tk.Entry(self, width = 30, bg = "white")
        sid.pack()
        sid_t.pack()
        scity = tk.Label(self, text = "Station city: ", font = "none 12 bold")
        scity_t = tk.Entry(self, width = 30, bg = "white")
        scity.pack()
        scity_t.pack()
        scount = tk.Label(self, text = "Station country: ", font = "none 12 bold")
        scount_t = tk.Entry(self, width = 30, bg = "white")
        scount.pack()
        scount_t.pack()

        func_btn = tk.Button(self, text="Add new station", command=lambda: self.func(sid_t.get(),sname_t.get(),scity_t.get(),scount_t.get()))
        func_btn.pack(pady=10)

        button = tk.Button(self, text="Go back to Admin page", command=lambda: controller.show_frame("emp_page"))
        button.pack(pady=20)

        btn = tk.Button(self, text = "Go back to home page", command = lambda: controller.show_frame('login'))
        btn.pack(pady=20)
    
    def func(self,sname,sid,scity,scount):
        connection.cur.callproc('NEW_STATION', [sid,sname,scity,scount])
        x = "Successfully added!"
        print(x)
        msg_label = tk.Label(self, text = x, font = "none 12 bold")
        msg_label.pack()
        connection.conn.commit()

class add_employee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#ffc9e7')
        label = tk.Label(self, text="Add a Employee", font="none 12 bold")
        label.pack(side="top", fill="x", pady=10)

        empid = tk.Label(self, text = "Employee ID: ", font = "none 12 bold")
        empid_t = tk.Entry(self, width = 30, bg = "white")
        empid.pack()
        empid_t.pack()
        name = tk.Label(self, text = "Name: ", font = "none 12 bold")
        name_t = tk.Entry(self, width = 30, bg = "white")
        name.pack()
        name_t.pack()
        email = tk.Label(self, text = "Email ID: ", font = "none 12 bold")
        email_t = tk.Entry(self, width = 30, bg = "white")
        email.pack()
        email_t.pack()
        prof = tk.Label(self, text = "Profession: ", font = "none 12 bold")
        prof_t = tk.Entry(self, width = 30, bg = "white")
        prof.pack()
        prof_t.pack()
        sal = tk.Label(self, text = "Salary: ", font = "none 12 bold")
        sal_t = tk.Entry(self, width = 30, bg = "white")
        sal.pack()
        sal_t.pack()
        address = tk.Label(self, text = "Address: ", font = "none 12 bold")
        address_t = tk.Entry(self, width = 30, bg = "white")
        address.pack()
        address_t.pack()
        phone = tk.Label(self, text = "Phone No: ", font = "none 12 bold")
        phone_t = tk.Entry(self, width = 30, bg = "white")
        phone.pack()
        phone_t.pack()

        func_btn = tk.Button(self, text="Add Employee", command=lambda: self.func(empid_t.get(),name_t.get(),email_t.get(),prof_t.get(),sal_t.get(),address_t.get(),phone_t.get()))
        func_btn.pack(pady=10)

        button = tk.Button(self, text="Go back to Employee page", command=lambda: controller.show_frame("emp_page"))
        button.pack(pady=20)

        btn = tk.Button(self, text = "Go back to home page", command = lambda: controller.show_frame('login'))
        btn.pack(pady=20)
    
    def func(self,empid,name,email,prof,sal,address,phone):
        connection.cur.callproc('add_employee', [empid,name,email,prof,sal,address,phone])
        print('Employee data inserted properly')
        query_label = tk.Label(self,text="Employee added successfully")
        query_label.pack(pady=20)
        connection.conn.commit()

class del_employee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#ffc9e7')
        label = tk.Label(self, text="Remove an employee", font="none 12 bold")
        label.pack(side="top", fill="x", pady=10)

        empID = tk.Label(self, text = "Emp ID: ", font = "none 12 bold")
        empID_t = tk.Entry(self, width = 30, bg = "white")
        empID.pack()
        empID_t.pack()
        phone = tk.Label(self, text = "Phone no: ", font = "none 12 bold")
        phone_t = tk.Entry(self, width = 30, bg = "white")
        phone.pack()
        phone_t.pack()

        func_btn = tk.Button(self, text="Remove Employee", command=lambda: self.func(empID_t.get(),phone_t.get()))
        func_btn.pack(pady=10)

        button = tk.Button(self, text="Go back to Employee page", command=lambda: controller.show_frame("emp_page"))
        button.pack(pady=20)

        btn = tk.Button(self, text = "Go back to home page", command = lambda: controller.show_frame('login'))
        btn.pack(pady=20)
    
    def func(self,empid,phone):
        connection.cur.callproc('del_employee', [empid,phone])
        print('Employee removed properly')
        query_label = tk.Label(self,text="Employee removed successfully")
        query_label.pack(pady=20)
        connection.conn.commit()
        