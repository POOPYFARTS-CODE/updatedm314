import tkinter as tk
from tkinter import ttk
from nike import nike
from adidas import adidas
from supreme import supreme

screen = tk.Tk()
screen.title("Shoe Buyer")
screen.geometry('800x800')

ttk.Label(screen, text = "Shoe Autobuyer",
          foreground ="black", anchor="center",
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 

ttk.Label(screen, text = "Select the company :",  
        font = ("Times New Roman", 10)).grid(column = 0,  
        row = 15, padx = 10, pady = 25) 

ttk.Label(screen, text = "Select the size :",  
        font = ("Times New Roman", 10)).grid(column = 0,
        row = 20)

ttk.Label(screen, text = "Enter the link :",
        font = ("Times New Roman", 10)).grid(column = 0,
        row = 40)

url = tk.Entry(screen)
url.grid(column=1,row=40)

n = tk.StringVar()
s = tk.StringVar()
_ = tk.OptionMenu(screen, n, "Nike","Adidas","Supreme","Shopify").grid(row=15,column=1)
_ = tk.OptionMenu(screen, s, "S","L","M","XL","XXL","XXXL").grid(row=20,column=1)

def f():
    global url
    if n=="Adidas":
        adidas(url)
    elif n=="Supreme":
        supreme(url)
    elif n=="Nike":
        nike(url,s)
button = tk.Button(screen, text="OK", command=f).grid(row=60,column=4)
tk.mainloop()
