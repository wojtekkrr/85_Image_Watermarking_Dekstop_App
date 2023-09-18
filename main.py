from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageOps
import os

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

FRAME_THICKNESS = 10

# Kolory
COLOUR_PALETTE = ["#FAF1E4", "#CEDEBD", "#9EB384", "#435334"]


# ---------------------------- IMPORTING AN IMAGE ------------------------------- #
def open_image():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    # Sprawdzenie czy wybrano obraz
    try:
        with Image.open(file_path) as image:
            pass
    except AttributeError:
        pass
    else:
        with Image.open(file_path) as image:
            img_width = image.width
            img_height = image.height
            ratio = 20
            # Utworzenie miniatury do poglądu
            image.thumbnail((img_width / ratio, img_height / ratio))
            # Utworzenie ramki
            photo_with_frame = ImageOps.expand(image, border=FRAME_THICKNESS, fill=COLOUR_PALETTE[1])
            photo = ImageTk.PhotoImage(photo_with_frame)
            # Przypisanie miniatury do etykiety
            picture_miniature.config(image=photo)
            picture_miniature.image = photo
            # Usunięcie komunikatu, odnośnie dodania znaku wodnego (powtórne użycie applikacji)
            task_completed.config(text="")


# ---------------------------- WATERMARKING AN IMAGE ------------------------------- #
def add_watermark():
    # Sprawdzenie czy uzupełniono pola wyboru
    if text_entry.get() == "" or font_entry.get() == "" or size_entry.get() == "":
        messagebox.showinfo(title="Oops", message="Dont leave empty spaces")
    else:
        text = text_entry.get()
        size = size_entry.get()
        font = font_entry.get()
        # Sprawdzenie czy podano prawidłowe parametry czcionki
        try:
            font_truetype = ImageFont.truetype(f"{font.lower()}.ttf", int(size))
        except OSError:
            messagebox.showinfo(title="Oops", message="Enter proper font name.")
        except ValueError:
            messagebox.showinfo(title="Oops", message="Enter proper font size.")
        else:
            text_color = (255, 255, 255)
            text_position = (100, 100)
            # Sprawdzenie czy wybrano obraz
            try:
                with Image.open(file_path) as image_to_watermark:
                    pass
            except NameError:
                messagebox.showinfo(title="Oops", message="Add a picture")
            else:
                # Dodanie znaku wodnego
                with Image.open(file_path) as image_to_watermark:
                    draw = ImageDraw.Draw(image_to_watermark)
                    draw.text(text_position, text, fill=text_color, font=font_truetype)
                    # Utworzenie ścieżki do zapisu
                    file_path_clean = file_path.rsplit("/", 1)[0]
                    target_file_path = file_path_clean + "/watermark/"
                    # Utworzenie katalogu w folderze z wybranym obrazem
                    if not os.path.exists(target_file_path):
                        os.makedirs(target_file_path)
                    file_name = file_path.split("/")[-1]
                    image_to_watermark.save(target_file_path + file_name)

                    # Komunikat, że się udało
                    task_completed.config(text="Task Completed!", font=(FONT_NAME, 25), bg=COLOUR_PALETTE[0],
                                          fg=COLOUR_PALETTE[2])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Image Watermarking")
window.config(padx=100, pady=50, bg=COLOUR_PALETTE[0])

title = Label(text="Image Watermarking", font=(FONT_NAME, 35), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
title.grid(column=0, row=0, columnspan=2, pady=(0, 50))

picture_miniature = Label()
picture_miniature.grid(column=0, row=2, columnspan=2, pady=25)

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

add_picture = Button(text="Add Picture", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3],
                     command=open_image)
add_picture.grid(column=0, row=1, columnspan=2)

add_watermark = Button(text="Add Watermark", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3],
                       command=add_watermark)
add_watermark.grid(column=0, row=6, columnspan=2, pady=25)

window.mainloop()
