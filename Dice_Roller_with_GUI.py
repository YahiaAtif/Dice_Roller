import tkinter
from PIL import Image, ImageTk
import random

win = tkinter.Tk()
win.title("Rolling Dice")
win.geometry('350x280')
win.eval("tk::PlaceWindow . center")

dice_images = ['one.png', 'two.png', 'three.png', 'four.png', 'five.png', 'six.png']
img = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))

lbl_image = tkinter.Label(win, image = img)
lbl_image.image = img
lbl_image.pack(expand = True)

def roll_the_dice():
	img = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))
	lbl_image.configure(image = img)
	lbl_image.image = img 

btn = tkinter.Button(win, text = 'ROLL THE DICE', command = roll_the_dice)
btn.pack(expand = True)

win.mainloop()