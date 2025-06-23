from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
window.title("Miles to Km Converter")

label_1 = Label(text="Enter distance in miles: ")
label_1.grid(row=0, column=0, padx=10, pady=10)

label_2 = Label(text="Distance in Km is: ")
label_2.grid(row=1, column=0, padx=10, pady=10)

def converter():
    miles = float(miles_input.get())
    km = miles * 1.60934  # Conversion factor
    km_result_entry.config(state="normal")  # Enable editing to update value
    km_result_entry.delete(0, END)  # Clear previous value
    km_result_entry.insert(0, f"{km:.2f}")  # Insert new converted value
    km_result_entry.config(state="readonly")  # Set back to readonly

miles_input = Entry(width=20)
miles_input.grid(row=0, column=1, padx=10, pady=10)

button = Button(text="Convert", command=converter)
button.grid(row=0, column=2, padx=10, pady=10)

km_result_entry = Entry(width=20, state="readonly", readonlybackground="white")  # Readonly result box
km_result_entry.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()
