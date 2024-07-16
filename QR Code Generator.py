# Importing required modules
from tkinter import * 
import qrcode
import os

# GUI Properties
root = Tk()
root.title("QR Code Generator")
root.geometry("1200x600")
root.config(bg = "#AE2321")
root.resizable(False, False)

# Icon Image
image_icon = PhotoImage(file = "icon.png")
root.iconphoto(False, image_icon)

# Defining the QR Code Generate Function
def generate():
    name = title.get()
    text = link.get()
    url = location.get()
    
    # Ensuring link field is non-empty
    if (url == '' and text == ''):
        Label(root, text = "Please enter a link or location...", fg = "white", bg = "#AE2321", font = 15).place(x = 50, y = 370)
        return
    
    # Ensuring that directory exists
    if not os.path.exists("QR Code"):
        os.makedirs("QR Code")

    if url != '':
        qr = qrcode.make(location2url())
        qr.save("QR Code/" + str(name) + ".png")
    
    if text != '':
        qr = qrcode.make(text)
        qr.save("QR Code/" + str(name) + ".png")

    # Display QR Image
    global Image
    Image = PhotoImage(file = "QR Code/" + str(name) + ".png")
    Image_view.config(image = Image)
   
def location2url():
    text = location.get()
    
    # Format of location url: ' ' --> '%20'
    url = "https://www.google.com/maps/dir//"
    for i in range(0, len(text)):
        if text[i] != ' ':
            url = url + text[i]
        else:
            url = url + '%20'
            
    return url
            
# QR Image properties
Image_view = Label(root, bg = "#AE2321")
Image_view.pack(padx = 50, pady = 10, side = RIGHT)

# Label and their entry field 
Label(root, text = "Title", fg = "white", bg = "#AE2321", font = 15).place(x = 50, y = 170)
title = Entry(root, width = 15, font = "arial 15")
title.place(x = 150, y = 170)

Label(root, text = "Link", fg = "white", bg = "#AE2321", font = 15).place(x = 50, y = 210)
link = Entry(root, width = 28, font = "arial 15")
link.place(x = 150, y = 210)

Label(root, text = "Location", fg = "white", bg = "#AE2321", font = 15).place(x = 50, y = 250)
location = Entry(root, width = 32, font = "arial 15")
location.place(x = 150, y = 250)

# Generate Button
Button(root, text = "Generate", width = 20, height = 2, fg = "white", bg = "black", command = generate).place(x = 50, y = 300)

# Initializing the GUI
root.mainloop()