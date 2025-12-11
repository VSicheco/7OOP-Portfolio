from tkinter import *
from tkinter import messagebox
import tkinter as tk

class MyWindow:
    # initiallized all widgets and controls
    def __init__(self, win):
        self.lbl1 = Label(win, text='First number')
        self.lbl2 = Label(win, text='Second number')
        self.lbl3 = Label(win, text='Result')
        
        self.first_number = Entry(bd=3)
        self.second_number = Entry()
        self.result = Entry(state='readonly')
        
        self.add_button = Button(win, text='Add')
        self.subtract_button = Button(win, text='Subtract')
        self.clear_button = Button(win, text='Clear')
        self.about_button = Button(win, text='About')
        
        self.lbl1.place(x=100, y=50)
        self.first_number.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.second_number.place(x=200, y=100)
        
        self.add_button = Button(win, text='Add', command=self.add)
        self.subtract_button = Button(win, text='Subtract', command=self.sub)
        self.clear_button = Button(win, text='Clear', command=self.clear)
        self.about_button = Button(win, text='About', command=self.display_about)
        
        self.add_button.place(x=100, y=150)
        self.subtract_button.place(x=200, y=150)
        self.clear_button.place(x=300, y=150)
        self.about_button.place(x=10, y=10)
        
        self.lbl3.place(x=100, y=200)
        self.result.place(x=200, y=200)
        

    #function definition
    def add(self):
            self.result.delete(0, 'end')
            try:
                num1 = int(self.first_number.get())
                num2 = int(self.second_number.get())
            except ValueError:
                messagebox.showerror("Look at this guy", "Text is not allowed! - Numbers  Only")
              
            result = num1 + num2  
            self.toggle_readonly(self.result)
            self.clear_result()
            self.result.insert(END, str(result))
            self.toggle_readonly(self.result)
            
    def sub(self):
        self.result.delete(0, 'end')
        try:
            num1 = int(self.first_number.get())
            num2 = int(self.second_number.get())
        except ValueError:
            messagebox.showerror("Look at this guy", "Text is not allowed! - Numbers  Only")
            
        result = num1 - num2
        self.toggle_readonly(self.result)
        self.clear_result()
        self.result.insert(END, str(result))
        self.toggle_readonly(self.result)
        
    def clear(self):
        self.first_number.delete(0, tk.END)
        self.second_number.delete(0, tk.END)
        self.result.delete(0, tk.END)
        
    def clear_result(self):
        self.result.delete(0, tk.END)
        
    def display_about(self):
        messagebox.showinfo('Calculator', 'ulatorCalc' * 50)

    def toggle_readonly(self, entry_field): 
        current_state = entry_field.cget('state')
        
        if current_state == 'readonly':
            entry_field.configure(state='normal')
        elif current_state == 'normal':
            entry_field.configure(state='readonly')
            
#test the class
if __name__ == '__main__':
    window=Tk()
    mywin=MyWindow(window)
    window.title('Calculator')
    window.geometry("400x300+10+10")
    window.mainloop()