import tkinter
from tkinter import *

def get_window_details():
    window = top.geometry()
    window_details = window.split('+')
    width = int(window_details[0].split('x')[0])
    height = int(window_details[0].split('x')[1])
    x_coordinate = int(window_details[1])
    y_coordinate = int(window_details[2])
    return width, height, x_coordinate, y_coordinate
    
def expand_window(direction, amount: int, current_window_size):
    width = current_window_size[0]
    height = current_window_size[1]
    x_coordinate = current_window_size[2]
    y_coordinate = current_window_size[3]
    
    if direction == "left":
        width = width + amount
        x_coordinate = x_coordinate - amount
    elif direction == "right":
        width = width + amount
    elif direction == "top":
        height = height + amount
        y_coordinate = y_coordinate - amount
    elif direction == "bottom":
        height = height + amount
        
    top.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")     
    
def reset_window():
    top.geometry("400x300+100+100")
    
def toggle_sign():
    if operator_button['text'] == '+':
        operator_button['text'] = '-'
    elif operator_button['text'] == '-':
        operator_button['text'] = '+'
    
top = tkinter.Tk()
top.title("Expanding Window")
reset_window()

left_button = Button(top, text = "Left", command=lambda:expand_window("left", int(f"{operator_button['text']}100"), get_window_details()))
left_button.pack(side = LEFT)

right_button = Button(top, text = "Right", command=lambda:expand_window("right", int(f"{operator_button['text']}100"), get_window_details()))
right_button.pack(side = RIGHT)

top_button = Button(top, text = "Top", command=lambda:expand_window("top", int(f"{operator_button['text']}100"), get_window_details()))
top_button.pack(side = TOP)

bottom_button = Button(top, text = "Bottom", command=lambda:expand_window("bottom", int(f"{operator_button['text']}100"), get_window_details()))
bottom_button.pack(side = BOTTOM)

reset_button = Button(top, text = "Reset", command=lambda:reset_window())
reset_button.pack(side = LEFT, expand = True)

operator_button = Button(top, text = '+', command=lambda: toggle_sign())
operator_button.pack(side = RIGHT, expand = True)

top.mainloop()