import tkinter as tk
import login
import customer
import employee
class mainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry('500x600')
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} 
    
        frames = (login.login,customer.Add_Cust,customer.cust_page,customer.pay_fees,employee.add_employee,employee.add_station,employee.emp_page,employee.del_employee)

        for i in frames:
            frame = i(parent=container, controller=self)

            self.frames[i.__name__] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.show_frame('login')

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()



if __name__ == "__main__":
    window = mainWindow()
    window.mainloop()