#Script by Chris Skoczylas
#for use with Python 3.6+

from PIL import Image										#must have Pillow installed
import pickle
import tkinter

def main():
	newfile = "data.pk"									#save data file name

	root = tkinter.Tk()									#getting screen resolution of user
	x = root.winfo_screenwidth()
	y = root.winfo_screenheight()

	justWorkedOn = 1									#this should be 1 or 2
	Color = (200,20,20)									#starts at max red
	redGoesUp = False
	redGoesDown = False
	blueGoesUp = True
	blueGoesDown = False
	greenGoesUp = False
	greenGoesDown = False

	Info = [justWorkedOn, Color, redGoesUp, redGoesDown, greenGoesUp, greenGoesDown, blueGoesUp, blueGoesDown]

	with open(newfile, "wb") as fi:								#saving initial data
		pickle.dump(Info, fi)

	newImage = Image.new("RGB", (x, y), "white")
	newImage.save("Images/background1.png")
	newImage.save("Images/background2.png")					#creating default backgrounds for user

main()