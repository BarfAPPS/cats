import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO

root = tk.Tk()
root.title("cat picker")

label = tk.Label(root, text="Loading cats!")
label.pack()

img_label = tk.Label(root)
img_label.pack()

def load_cat_image():
    label.config(text="Loading cat image...")
    root.update_idletasks()  # Update UI before download
    response = requests.get("https://cataas.com/cat")
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize( (300,300))
    tk_img = ImageTk.PhotoImage(img)
    img_label.config(image=tk_img)
    img_label.image = tk_img
    label.config(text="Do you like this cat?")

def clicked_yes():
    label.config(text="yes!")
    root.after(1000, load_cat_image)

def clicked_no():
    label.config(text="no!")
    root.after(1000, load_cat_image)

yes_button = tk.Button(root, text="Yes", command=clicked_yes)
yes_button.pack(side=tk.LEFT, padx=10, pady=10)

no_button = tk.Button(root, text="No", command=clicked_no)
no_button.pack(side=tk.RIGHT, padx=10, pady=10)
load_cat_image()


root.mainloop()

