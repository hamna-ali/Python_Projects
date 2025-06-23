from tkinter import *
import random
from tkinter import messagebox
import pandas

# --- Load Data ---
try:
    data = pandas.read_csv("French_Words.csv")
    words_dict = data.to_dict(orient="records")
except FileNotFoundError:
    messagebox.showerror("Error", "French_Words.csv not found.")
    words_dict = []

# --- Variables ---
score = 0
current_word = {}
flip_timer = None
next_card_timer = None

# --- Functions ---
def next_card():
    global current_word, flip_timer, next_card_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    if next_card_timer:
        window.after_cancel(next_card_timer)

    if not words_dict:
        canvas.itemconfig(card_title, text="🎉 Done!", fill="black")
        canvas.itemconfig(card_word, text=f"Final Score: {score}", fill="black")
        return

    current_word = random.choice(words_dict)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")

    # Flip to English after 3 seconds
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global next_card_timer
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")

    # Auto-go to next card after 2 more seconds
    next_card_timer = window.after(2000, next_card)

def is_known():
    global score
    if current_word in words_dict:
        words_dict.remove(current_word)
        score += 1
        score_text.config(text=f"Score: {score}")
    next_card()

# --- UI Setup ---
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Score Label at Top Left
score_text = Label(text="Score: 0", bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold"))
score_text.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=cross_image, highlightthickness=0, command=next_card)
no_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
yes_button = Button(image=tick_image, highlightthickness=0, command=is_known)
yes_button.grid(row=1, column=1)

# Start
next_card()

window.mainloop()



