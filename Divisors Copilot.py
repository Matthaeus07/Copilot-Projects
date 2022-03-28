#Make a GUI application that will allow the user to input a number and then have the application print out a list of all the divisord of that number.


from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Divisor")
root.geometry("500x500")

def gather_input():
    number = int(entry.get())
    divisor_list = []
    for i in range(1, number+1):
        if number % i == 0:
            divisor_list.append(i)
    #Put a "," between each number in the list
    divisor_list = str(divisor_list).replace("[", "").replace("]", "").replace(",", ", ")
    #display the divisor_list in the GUI below each other
    label = tk.Label(root, text=divisor_list)
    label.place(x=100, y=100)
    

#text bot the user can input a number
entry = Entry(root)
entry.pack()

#button that will call the gather_input function
button = Button(root, text="Print Divisors", command=gather_input)
button.pack()

root.mainloop()