from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import webcolors
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageOps
import os

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

FRAME_THICKNESS = 10

#Kolory
COLOUR_PALETTE = ["#FAF1E4".lower(), "#CEDEBD".lower(), "#9EB384".lower(), "#435334".lower()]

# ---------------------------- IMPORTING AN IMAGE ------------------------------- #
def open_image():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    with Image.open(file_path) as image:
        image_to_watermark = image
        img_width = image.width
        img_height = image.height
        ratio = 20
        #Utworzenie miniatury do poglądu
        image.thumbnail((img_width/ratio, img_height/ratio))
        #Utworzenie ramki
        photo_with_frame = ImageOps.expand(image, border=FRAME_THICKNESS, fill=COLOUR_PALETTE[1])
        photo = ImageTk.PhotoImage(photo_with_frame)
        #Przypisanie miniatury do etykiety
        picture_miniature.config(image=photo)
        picture_miniature.image = photo


# ---------------------------- WATERMARKING AN `IMAGE` ------------------------------- #
def add_watermark():
    if text_entry.get() == "" or font_entry.get() == "" or size_entry.get() == "":
        messagebox.showinfo(title="Oops", message="Dont leave empty spaces")
    else:
        text = text_entry.get()
        size = size_entry.get()
        font = font_entry.get()
        font_truetype = ImageFont.truetype(f"{font.lower()}.ttf", int(size))

        text_color = (255, 255, 255)
        text_position = (100, 100)

        with Image.open(file_path) as image_to_watermark:
            draw = ImageDraw.Draw(image_to_watermark)
            draw.text(text_position, text, fill=text_color, font=font_truetype)
            file_path_clean = file_path.rsplit("/", 1)[0]
            target_file_path = file_path_clean + "/watermark/"
            if not os.path.exists(target_file_path):
                os.makedirs(target_file_path)
            file_name = file_path.split("/")[-1]
            image_to_watermark.save(target_file_path + file_name)

        task_completed.config(text="Task Completed!", font=(FONT_NAME, 25), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[2])#Tu coś nie trybi i nie wiem czemu od początku się komunikat wyświetlas






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Image Watermarking")

window.config(padx=100, pady=50, bg=COLOUR_PALETTE[0])

title = Label(text="Image Watermarking", font=(FONT_NAME, 35), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
title.grid(column=0, row=0, columnspan=2)

picture_miniature = Label()
picture_miniature.grid(column=0, row=2, columnspan=2)

text_label = Label(text="Text:", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
text_label.grid(column=0, row=3)

font_label = Label(text="Font:", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
font_label.grid(column=0, row=4)

size_label = Label(text="Size:", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
size_label.grid(column=0, row=5)

task_completed = Label()
task_completed.grid(column=0, row=7, columnspan=2)

text_entry = Entry(width=35, bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
text_entry.grid(column=1, row=3)
text_entry.focus()

font_entry = Entry(width=35, bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
font_entry.grid(column=1, row=4)

size_entry = Entry(width=35, bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
size_entry.grid(column=1, row=5)

add_picture = Button(text="Add Picture", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3], command=open_image)
add_picture.grid(column=0, row=1, columnspan=2)

add_watermark = Button(text="Add Watermark", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3], command=add_watermark)
add_watermark.grid(column=0, row=6, columnspan=2)

window.mainloop()