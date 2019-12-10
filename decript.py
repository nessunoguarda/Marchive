#!/bin/python3

from PIL import Image

def morseint(string):
	if string == "bllll":
		return "1"
	elif string == "bblll":
		return "2"
	elif string == "bbbll":
		return "3"
	elif string == "bbbbl":
		return "4"
	elif string == "bbbbb":
		return "5"
	elif string == "lbbbb":
		return "6"
	elif string == "llbbb":
		return "7"
	elif string == "lllbb":
		return "8"
	elif string == "llllb":
		return "9"
	elif string == "lllll":
		return "0"
	elif string =="bl":
		return "a"
	elif string =="lbbb":
		return "b"
	elif string =="lblb":
		return "c"
	elif string =="lbb":
		return "d"
	elif string =="b":
		return "e"
	elif string =="bblb":
		return "f"
	elif string =="llb":
		return "g"
	elif string =="bbbb":
		return "h"
	elif string =="bb":
		return "i"
	elif string =="blll":
		return "j"
	elif string =="lbl":
		return "k"
	elif string =="blbb":
		return "l"
	elif string =="ll":
		return "m"
	elif string =="lb":
		return "n"
	elif string =="lll":
		return "o"
	elif string =="bllb":
		return "p"
	elif string =="llbl":
		return "q"
	elif string =="blb":
		return "r"
	elif string =="bbb":
		return "s"
	elif string =="l":
		return "t"
	elif string =="bbl":
		return "u"
	elif string =="bbbl":
		return "v"
	elif string =="bll":
		return "w"
	elif string =="lbbl":
		return "x"
	elif string =="lbll":
		return "y"
	elif string =="llbb":
		return "z"
	else:
		return "~"

def strtomorse(string):
	output = ""
	counter = 0
	for x in string:
		if x== "1":
			counter += 1
		elif counter > 0 and x == "0":
			if counter == 3:
				output += "l"
			else:
				output += "b"
			counter = 0
	return output
			
filename = "pwd.png"

image = Image.open(filename)


convert = ""
array = []
width, height = image.size
RGB = image.convert("RGB")
for y in range(0, height):
	#matrix
	array.append([])
	for x in range(0, width):
		pixel = RGB.getpixel((x,y))
		array[y].append(pixel)
s = array[0][0]
list_morse = []
#print(array)
for y in range(1, height,2):
	for x in range(0, width):
		if array[y][x] == s:
			convert += "0"
		else:
			convert += "1"
	list_morse.append(convert)
	convert = ""
#print(list_morse)	

i = 0
password = ""
for x in list_morse:
	app = strtomorse(list_morse[i])
	#print(app)
	app = morseint(app) 
	if app != "~":
		password += str(app)
	i += 1
print(password)

