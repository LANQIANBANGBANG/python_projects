import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French",fill="#000000")
    canvas.itemconfig(card_word, text=current_card["French"],fill="#000000")
    canvas.itemconfig(card_image, image=card_front_img)
    window.after(3000, flip_card)
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="#FFFFFF")
    canvas.itemconfig(card_word,text=current_card["English"],fill="#FFFFFF")
    canvas.itemconfig(card_image,image=card_back_img)

window = Tk()#add a window
window.title("Flashy") # window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR) # padding to the left and right and padding to the top and button

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
dontknow_button = Button(image=cross_image,highlightthickness=0,borderwidth=0,command=flip_card)
dontknow_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image,highlightthickness=0,borderwidth=0,command=next_card)
know_button.grid(row=1, column=1)

window.after(3000, flip_card)

next_card()

window.mainloop()# keeps it running until you close the window