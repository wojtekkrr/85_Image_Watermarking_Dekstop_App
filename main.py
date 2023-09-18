from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import webcolors
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageOps

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

FRAME_THICKNESS = 10

#Kolory
COLOUR_PALETTE = ["#FAF1E4".lower(), "#CEDEBD".lower(), "#9EB384".lower(), "#435334".lower()]

# ---------------------------- IMPORTING AN IMAGE ------------------------------- #
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    with Image.open(file_path) as image:
        img_width = image.width
        img_height = image.height
        ratio = 20
        #Utworzenie miniatury do poglądu
        image.thumbnail((img_width/ratio, img_height/ratio))
        #Utworzenie ramki
        photo_with_frame = ImageOps.expand(image, border=FRAME_THICKNESS, fill=COLOUR_PALETTE[2])
        photo = ImageTk.PhotoImage(photo_with_frame)
        #Przypisanie miniatury do etykiety
        picture_miniature.config(image=photo)
        picture_miniature.image = photo









# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Image Watermarking")

window.config(padx=100, pady=50, bg=COLOUR_PALETTE[0])

title = Label(text="Image Watermarking", font=(FONT_NAME, 35), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
title.grid(column=0, row=0, columnspan=2)

add_picture = Button(text="Add Picture", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], command=open_image)
add_picture.grid(column=0, row=1)

picture_miniature = Label()
picture_miniature.grid(column=1, row=1)

window.mainloop()