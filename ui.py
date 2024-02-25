import tkinter as tk
import main

def on_button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Simple GUI")

def load_data():
    data = main.runAllImage(2)

def save_data():
    # Your code to save data from Tkinter widgets back to your project
    print("not")

load_button = tk.Button(root, text="Load Data", command=load_data)
save_button = tk.Button(root, text="Save Data", command=save_data)

data_label = tk.Label(root, text="Data will be displayed here")

data_label.pack()
load_button.pack()
save_button.pack()


root.mainloop()
