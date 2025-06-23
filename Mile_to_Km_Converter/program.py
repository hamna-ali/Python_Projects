from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.config(padx=20, pady=20, bg="pink")  # Background color for the window
window.title("Miles to Km Converter")

label_font = ("Times New Roman", 12)  # Set font to Times New Roman, normal size

label_1 = Label(text="Enter distance in miles:", fg="black",bg="pink")  # Black text
label_1.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Align left

label_2 = Label(text="Distance in Km is:", fg="black",bg="pink")  # Black text
label_2.grid(row=1, column=0, padx=10, pady=10, sticky="w")  # Align left

def converter():
    miles = float(miles_input.get())
    km = miles * 1.60934  # Conversion factor
    km_result_entry.config(state="normal")  # Enable editing
    km_result_entry.delete(0, END)  # Clear previous result
    km_result_entry.insert(0, f"{km:.2f}")  # Insert new converted value
    km_result_entry.config(state="readonly")  # Set back to readonly

miles_input = Entry(width=20, font=("Times New Roman", 12))
miles_input.grid(row=0, column=1, padx=10, pady=10)

button = Button(text="Convert", command=converter, font=("Times New Roman", 12))
button.grid(row=0, column=2, padx=10, pady=10)

km_result_entry = Entry(width=20, state="readonly", readonlybackground="white", fg="black", font=("Times New Roman", 12))
km_result_entry.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()


