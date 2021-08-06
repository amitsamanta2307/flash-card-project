from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# --------------------------------- UI --------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(height=526, width=800)
card_front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(column=0, row=2)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(column=1, row=2)

window.mainloop()
