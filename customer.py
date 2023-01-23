import tkinter as tk
import connection


class cust_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#b3ecec')
        label = tk.Label(self, text="CUSTOMER PAGE", font="none 12 bold")
        label.pack()

        func = tk.Button(self, text = "Add New Customer", command = lambda: self.controller.show_frame("Add_Cust"))
        func.pack(pady=10)
        crs_reg = tk.Button(self, text = "Pay Fees", command = lambda: self.controller.show_frame("pay_fees"))
        crs_reg.pack(pady=10)
        btn = tk.Button(self, text = "Go back to home page", command = lambda: controller.show_frame('login'))
        btn.pack(pady=20)


class Add_Cust(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#b3ecec')
        label = tk.Label(self, text="Add New Customer", font="none 12 bold")
        label.pack(side="top", fill="x", pady=10)
        welcome_msg = tk.Label(self, text = "Welcome! Please enter your details", font = "none 12 bold")
        welcome_msg.pack()

        name = tk.Label(self, text = "Full Name: ", font = "none 12 bold")
        name_t = tk.Entry(self, width = 30, bg = "white")
        name.pack()
        name_t.pack()
        custID = tk.Label(self, text = "Customer ID: ", font = "none 12 bold")
        custID_t = tk.Entry(self, width = 30, bg = "white")
        custID.pack()
        custID_t.pack()
        phone = tk.Label(self, text = "Phone: ", font = "none 12 bold")
        phone_t = tk.Entry(self, width = 30, bg = "white")
        phone.pack()
        phone_t.pack()
        address = tk.Label(self, text = "Address: ", font = "none 12 bold")
        address_t = tk.Entry(self, width = 30, bg = "white")
        address.pack()
        address_t.pack()
        dob = tk.Label(self, text = "Date of Birth: ", font = "none 12 bold")
        dob_t = tk.Entry(self, width = 30, bg = "white")
        dob.pack()
        dob_t.pack()

        func_btn = tk.Button(self, text="Add Customer", command=lambda: self.func(custID_t.get(),name_t.get(),phone_t.get(),address_t.get(),dob_t.get()))
        func_btn.pack(pady=10)

        button = tk.Button(self, text="Go back to Customer page", command=lambda: controller.show_frame("cust_page"))
        button.pack(pady=20)

        btn = tk.Button(self, text = "Go back to home page", command = lambda: controller.show_frame('login'))
        btn.pack(pady=20)
    
    def func(self,userid, username,phone,address,dob):
        connection.cur.callproc('add_user', [userid,username,phone,address,dob])
        x = "Successfully added!"
        print(x)
        msg_label = tk.Label(self, text = x, font = "none 12 bold")
        msg_label.pack()
        connection.conn.commit()

class pay_fees(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#b3ecec')
        label = tk.Label(self, text="Pay for ticket", font="none 12 bold")
        label.pack(side="top", fill="x", pady=10)

        userid = tk.Label(self, text = "UserID: ", font = "none 12 bold")
        userid_t = tk.Entry(self, width = 30, bg = "white")
        userid.pack()
        userid_t.pack()
        arriv = tk.Label(self, text = "Arrival station: ", font = "none 12 bold")
        arriv_t = tk.Entry(self, width = 30, bg = "white")
        arriv.pack()
        arriv_t.pack()
        depart = tk.Label(self, text = "Departure station: ", font = "none 12 bold")
        depart_t = tk.Entry(self, width = 30, bg = "white")
        depart.pack()
        depart_t.pack()
        date = tk.Label(self, text = "Date: ", font = "none 12 bold")
        date_t = tk.Entry(self, width = 30, bg = "white")
        date.pack()
        date_t.pack()
        price = tk.Label(self, text = "Price: ", font = "none 12 bold")
        price_t = tk.Entry(self, width = 30, bg = "white")
        price.pack()
        price_t.pack()


        func_btn = tk.Button(self, text="Pay the fees", command=lambda: self.func(price_t.get(),userid_t.get(),date_t.get(),arriv_t.get(),depart_t.get()))
        func_btn.pack(pady=10)

        button = tk.Button(self, text="Go back to Customer page", command=lambda: controller.show_frame("login"))
        button.pack(pady=20)

        btn = tk.Button(self, text = "Go back to home page", command = lambda: controller.show_frame('login'))
        btn.pack(pady=20)
    
    def func(self,price,user,date,arriv,depart):
        connection.cur.callproc('payfees', [price,user,date,arriv,depart])
        x = "Successfully added!"
        print(x)
        msg_label = tk.Label(self, text = x, font = "none 12 bold")
        msg_label.pack()
        connection.conn.commit()
