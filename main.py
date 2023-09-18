from tkinter import *
from tkinter import messagebox
import webcolors

FONT_NAME = "Courier"

#Kolory
COLOUR_PALETTE = ["#FAF1E4".lower(), "#CEDEBD".lower(), "#9EB384".lower(), "#435334".lower()]

#Kolory w formacie RGB
# COLOUR_PALETTE_RGB = []
# for color in COLOUR_PALETTE:
#     rgb_color = webcolors.hex_to_rgb(color)
#     COLOUR_PALETTE_RGB.append('#%02x%02x%02x' % rgb_color)







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Image Watermarking")

window.config(padx=100, pady=100, bg=COLOUR_PALETTE[0])

window.mainloop()