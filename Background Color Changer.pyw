#Script by Chris Skoczylas
#for use with Python 3.6+

from PIL import Image										#must have Pillow installed
import pickle											#used for saving info[] in an unsecure way
import os

def main():
	transparent = os.path.normpath("Images/transparent.png")				#location of transparent image
	data = os.path.normpath("data.pk")							#location of pickled data file
	info = None
	fileName = None
	minColor = 20										#try to not have minColor >= maxColor
	maxColor = 200

	with open(data, "rb") as fi:								#loading data from info.pk
		info = pickle.load(fi)

	justWorkedOn = info[0]								#which background image was just worked on
	Color = info[1]										#current Color of background
	redGoesUp = info[2]
	redGoesDown = info[3]
	greenGoesUp = info[4]
	greenGoesDown = info[5]
	blueGoesUp = info[6]
	blueGoesDown = info[7]

	if justWorkedOn == 1:
		fileName = os.path.normpath("Images/background2.png")			#using forward slashes because python doesn't like \t
		justWorkedOn = 2
	else:
		fileName = os.path.normpath("Images/background1.png")
		justWorkedOn = 1

	img = Image.open(fileName)								#opening the background image and transparent image
	trans = Image.open(transparent)
	#pix = img.load()

	if redGoesUp:										#garbage code to make things change colors
		Color = (Color[0] + 1, Color[1], Color[2])
		if Color[0] >= maxColor:
			redGoesUp = False
			greenGoesDown = True
	elif greenGoesUp:
		Color = (Color[0], Color[1] + 1, Color[2])
		if Color[1] >= maxColor:
			greenGoesUp = False
			blueGoesDown = True
	elif blueGoesUp:
		Color = (Color[0], Color[1], Color[2] + 1)
		if Color[2] >= maxColor:
			blueGoesUp = False
			redGoesDown = True
	elif redGoesDown:
		Color = (Color[0] - 1, Color[1], Color[2])
		if Color[0] <= minColor:
			redGoesDown = False
			greenGoesUp = True
	elif greenGoesDown:
		Color = (Color[0], Color[1] - 1, Color[2])
		if Color[1] <= minColor:
			greenGoesDown = False
			blueGoesUp = True
	elif blueGoesDown:
		Color = (Color[0], Color[1], Color[2] - 1)
		if Color[2] <= minColor:
			blueGoesDown = False
			redGoesUp = True

	img.paste(Color, (0, 0, img.size[0], img.size[1]))					#filling image with color

	#for i in range (img.size[0]):
	#	for j in range (img.size[1]):
	#		pix[i, j] = Color

	img.paste(trans, (0, 0), trans)								#pasting transparent image on top of color
												#paste(image to paste, (where on image to paste), image to use alpha)
	img.save(fileName)
	info = [justWorkedOn, Color, redGoesUp, redGoesDown, greenGoesUp, greenGoesDown, blueGoesUp, blueGoesDown]

	with open(data, "wb") as fi:								#pickling the data
		pickle.dump(info, fi)

main()