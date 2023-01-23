import tkinter as tk
from connection import *

class login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#cbe5ab')
        self.controller = controller
        lb = tk.Label(self, text="Railway Reservation System", font = "none 14 bold")
        lb.pack(side = "top", fill = "x", pady = 10)
        tk.Button(self, text="Customer Menu", command = lambda: controller.show_frame('cust_page')).pack()
        tk.Button(self, text="Employee Menu", command = lambda: controller.show_frame('emp_page')).pack()