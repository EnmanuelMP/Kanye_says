from tkinter import *
import requests

# Kanye REST API URL
URL = "https://api.kanye.rest"

def get_quote()->None:
    """Fetches a quote from the Kanye REST API and updates the canvas with the new quote."""
    response:dict = requests.get(URL).json()
    canvas.itemconfig(quote_text,text=response["quote"])

# ____________________________ USER INTERFACE ______________________________
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Canvas setup
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Kanye button setup
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Running the GUI event loop
window.mainloop()
