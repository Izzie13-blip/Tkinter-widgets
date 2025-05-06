from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('image')
root.geometry('400x400')

upload = Image.open("images.jpg")
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, height=450, width=300)
label.place(x=50, y=0)

label2 = Label(root, text="A Lamborghini")
label2.place(x=40, y=360)

root.mainloop()