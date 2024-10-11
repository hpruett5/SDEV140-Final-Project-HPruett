#this prints the assignment title
print("MO8 Final Project Hannah Pruett- Hannah's Homemade GUI")
print("")

#this imports tkinter
import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#file_path = os.path.dirname(os.path.abspath(__file__))

# set local path to current folder

#this is a function for the second window that will pop out once the button on the first window is hit. 
def open_window1():
    window1 = tk.Toplevel(root)
    #creates title for the window, size of window, and background color of light pink
    window1.title("Hannah's Homemade")
    window1.geometry("400x800")
    window1.configure(bg="#FFC0CB")
    #this opens a shopping cart image for window1 to show that it is essentially a "shopping cart". 
    module_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(module_path, "shoppingcart.gif")
    output_path = os.path.join(module_path, "shoppingcart.gif")
    img2 = ImageTk.PhotoImage(Image.open (output_path))
    #determines the size of the image
    panel = Label(window1, image = img2, width=250, height=190)
    panel.image = img2
    panel.pack()


    #this is a label that gives user instruction to create their order, beginning with entering their name
    label1 = tk.Label(window1, text="Please enter your name to begin your order:")
    label1.pack()
    #this adds pretty space around the label
    label1.pack(pady=(3,3))
    #this is an entry box for the user to input their name
    entry1 = tk.Entry(window1)
    entry1.pack()
    #this adds pretty space
    entry1.pack(pady=(1,1))
    #this is a label that gives user instruction to enter their phone number
    labele = tk.Label(window1, text = "Please Enter Your Phone Number.")
    labele.pack()
    #adds pretty space
    labele.pack(pady=(1,1))
    #this creates the entry box for the user to input their phone number
    entrye = tk.Entry(window1)
    entrye.pack()
    #adds pretty space
    entrye.pack(pady=(1,1))
    #this is a label for the bar soap spin box    
    label2 = tk.Label(window1, text = "Handmade Bar Soap $4 per bar (unscented, 0-10 bars per order)")
    label2.pack()
    #adds pretty space
    label2.pack(pady=(1,1))
    #this creates a spinbox with values 0-10
    spinbox1 = ttk.Spinbox(window1, from_=0, to_=10)
    #adds pretty space
    spinbox1.pack(pady=1)
    #this is a label for the chapstick spin box
    label3 = tk.Label(window1, text = "Beeswax Chapstick $2 per stick (mint, 0-10 sticks per order)")
    label3.pack()
    #adds pretty space
    label3.pack(pady=(1,1))
    #this creates a spinbox with values 0-10
    spinbox2 = ttk.Spinbox(window1, from_=0, to_=10)
    #adds pretty sapce
    spinbox2.pack(pady=1)
    #this is a label for the lotion spin box
    label4 = tk.Label(window1, text = "Oil-based Lotion $5 per bottle (citrus - 8 oz, 0-10 bottles per order)")
    label4.pack()
    #adds pretty space
    label4.pack(pady=(1,1))
    #this creates a spinbox with values from 0-10 
    spinbox3 = ttk.Spinbox(window1, from_=0, to_=10)
    #adds pretty space
    spinbox3.pack(pady=1)
    #this is a label for the sunscreen spin box
    label5 = tk.Label(window1, text = "Sunscreen Stick $4 per stick (mint, 0-10 sticks per order)")
    label5.pack()
    #adds pretty space
    label5.pack(pady=(1,1))
    #this creates a spinbox with values from 0-10
    spinbox4 = ttk.Spinbox(window1, from_=0, to_=10)
    #adds pretty space
    spinbox4.pack(pady=1)
    #this is a label for the address entry box
    label6 = tk.Label(window1, text = "Enter Address, City, State, Zipcode")
    label6.pack()
    #adds pretty space
    label6.pack(pady=(1,1))
    #this creates the address entry box
    entry2 = tk.Entry(window1)
    entry2.pack()
    #adds pretty space
    entry2.pack(pady=(1,1))
    #this is a label for the payment information entry box
    labeln = tk.Label(window1, text = "Enter Name on Credit Card")
    labeln.pack()
    #adds pretty space
    labeln.pack(pady=(1,1))
    #this creates the payment name entry box
    entryn = tk.Entry(window1)
    entryn.pack()
    #adds pretty space
    entryn.pack(pady=(1,1))
    #this is a label for the payment card number entry box
    label7 = tk.Label(window1, text = "Enter Credit Card Number (16 digits, no spaces)")
    label7.pack()
    #adds pretty space
    label7.pack(pady=(1,1))
    #this creates the entry box for the card number
    entry3 = tk.Entry(window1)
    entry3.pack()
    #adds pretty space
    entry3.pack(pady=(1,1))    
    #this is a label for the card expiration date entry box
    label8 = tk.Label(window1, text = "Enter Credit Card Expiration Date (##/##)")
    label8.pack()
    #adds pretty space
    label8.pack(pady=(1,1))
    #this creates the expiration date entry box
    entry4 = tk.Entry(window1)
    entry4.pack()
    #adds pretty space
    entry4.pack(pady=(1,1))
    #label that gives instructions for CSV entry box
    label9 = tk.Label(window1, text = "Enter CSV Number (3 digits on back of card)")
    label9.pack()
    #adds pretty space
    label9.pack(pady=(1,1))
    #entry box for CSV number on card
    entry9 = tk.Entry(window1)
    entry9.pack()
    #adds pretty space
    entry9.pack(pady=(1,1))
        #this is a submit button that prints out user input in terminal
    button1 = tk.Button(window1, text="Submit", command=lambda: print("Order: ", entry1.get(), "\nPhone: ", int(entrye.get()), "\nSoap: ", spinbox1.get(), \
                                                                      "\nChapstick: ", spinbox2.get(), "\nLotion: ", spinbox3.get(), \
                                                                        "\nSunscreen: ", spinbox4.get(), "\nAddress: " , entry2.get(), \
                                                                            "\nName on Card: ", entryn.get(), "\nCard Number: ", int(entry3.get()), \
                                                                            "\nCard Expiration Date : ", (entry4.get()), "\nCSV Number: ", int(entry9.get()), \
                                                                                "\nTotal: $", (int(spinbox1.get())*4) + (int(spinbox2.get())*2) + (int(spinbox3.get())*5) + (int(spinbox4.get())*4)))
    button1.pack()
    #this adds pretty space
    button1.pack(pady=(1,1))
    #this is a terminate button for the user to exit the second window
    button2=tk.Button(window1, text = "Exit",
                   command=window1.destroy)
    button2.pack()
    #this adds pretty space
    button2.pack(pady=(1,1))

#creates the main window called Hannah's Homemade, estbalishes geometry and background color of light purple
root = tk.Tk()
root.title("Hannah's Homemade")
root.geometry("800x600")
root.configure(bg="#DDA0DD")

#from PIL import ImageTk, Image
#IMG_PATH = "HHlogo.jpg"
#IMG_PATH = "logoHH.gif"
# this opens Hannah's Homemade Logo in the main window
module_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(module_path, "logoHH.gif")
output_path = os.path.join(module_path, "logoHH.gif")
img = ImageTk.PhotoImage(Image.open (output_path))
#determines the size of the image
panel = Label(root, image = img, width=500, height=500)
panel.image = img
panel.pack()

#adds label that welcomes the user
labela=tk.Label(root, text="Welcome to Hannah's Homemade")
labela.pack()
#this adds pretty space around the label
labela.pack(pady=(10,10))
#adds button that calls the open_window1 function to open the order window
button_open1 = tk.Button(root, text="Click to Begin your Order", command=open_window1)
button_open1.pack()
#this adds pretty space around the button
button_open1.pack(pady=(10,10))

#this starts the program 
root.mainloop()