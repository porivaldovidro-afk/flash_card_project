from tkinter import *
import pandas as pd
import  random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/english_words.csv")
to_learn_data = ""
try:
    to_learn_data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data.to_csv("./data/words_to_learn.csv", index=False)
    to_learn_data = pd.read_csv("./data/words_to_learn.csv")
else:
    french_words = to_learn_data.to_dict(orient="records")
    word = {}

def next_card():
    global word
    word = random.choice(french_words)
    to_learn = word["English"]
    canvas.itemconfig(canvas_image, image=english_card)
    canvas.itemconfig(card_title, text="English", fill="black", font=("Arial", 40, "italic"),)
    canvas.itemconfig(card_word, text=to_learn, fill="black", font=("Arial", 60, "bold"))
    window.after(3000, background_card)

def is_known():
    global word
    if word:
        french_words.remove(word)
        update = pd.DataFrame(french_words)
        update.to_csv("./data/words_to_learn.csv", index=False)
    word = random.choice(french_words)
    to_learn = word["English"]
    canvas.itemconfig(canvas_image, image=english_card)
    canvas.itemconfig(card_title, text="English", fill="black", font=("Arial", 40, "italic"),)
    canvas.itemconfig(card_word, text=to_learn, fill="black", font=("Arial", 60, "bold"))
    window.after(3000, background_card)

def background_card():
    global word
    english_translate = word["Portuguese"]
    canvas.itemconfig(canvas_image, image=portuguese_card)
    canvas.itemconfig(card_title, text="Portugues", fill="white")
    canvas.itemconfig(card_word, text=english_translate, fill="white")
    window.after_cancel(translate)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
english_card = PhotoImage(file="./images/card_front.png")
portuguese_card = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=english_card)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 283, text="Word", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)


wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button()
wrong_button.config(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0, pady=50)

right_img = PhotoImage(file="./images/right.png")
right_button = Button()
right_button.config(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1, pady=50)


next_card()


translate = window.after(3000, background_card)

window.mainloop()
