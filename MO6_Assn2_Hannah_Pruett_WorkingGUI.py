#MO6_Assn2_Hannah_Pruett
#Hannah Pruett
#created 2024-09-27
#this program is a GUI that introduces Hannah's Homemade ordering system. It has a toplevel window that opens an ordering window and allows user to input information. 

#this prints the assignment title
print("MO6 Assn2 Hannah Pruett- Hannah's Homemade: Begin order GUI")
print("")

#this imports tkinter
import tkinter as tk

#this is a function for the second window that will pop out once the button on the first window is hit. 
def open_window1():
    window1 = tk.Toplevel(root)
    #creates title for the window, size of window, and background color of light pink
    window1.title("Hannah's Homemade")
    window1.geometry("300x200")
    window1.configure(bg="#FFC0CB")
    #this is a label that gives user instruction to create their order
    label1 = tk.Label(window1, text="Please enter your name to begin your order:")
    label1.pack()
    #this adds pretty space around the label
    label1.pack(pady=(10,10))
    #this is an entry box for the user to input their name
    entry1 = tk.Entry(window1)
    entry1.pack()
    #this adds pretty space
    entry1.pack(pady=(10,10))
    #this is a submit button that prints out user input in terminal
    button1 = tk.Button(window1, text="Submit", command=lambda: print("Order: ", entry1.get()))
    button1.pack()
    #this adds pretty space
    button1.pack(pady=(10,10))
    #this is a terminate button for the user to exit the second window
    button2=tk.Button(window1, text = "Exit",
                   command=window1.destroy)
    button2.pack()
    #this adds pretty space
    button2.pack(pady=(10,10))

#creates the main window called Hannah's Homemade, estbalishes geometry and background color of light purple
root = tk.Tk()
root.title("Hannah's Homemade")
root.geometry("300x100")
root.configure(bg="#DDA0DD")
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