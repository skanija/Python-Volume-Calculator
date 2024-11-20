#Trevor Kupper
#2/13/22
#Tank Volume Calculator w/ Tkinter Functionality

#Imports tkinter and math
import tkinter as tk
from tkinter import ttk
import math

#Sets up window
root = tk.Tk()
root.title("Tank Volume Calculator")

def calculateDef():
	#Gathers user input for use in function
	shape = shapeButton.get()
	entryLength = float(entry1.get())
	entryWidth = float(entry2.get())
	entryHeight = float(entry3.get())
	measure = choicesVar.get()

	#Changes value based on radio button and input
	if shape == '1':
		#Cylinder
		diameter = entryWidth
		radius = diameter / 2
		length = entryLength
		volume = math.pi * pow(radius, 2) * length
	elif shape =='2':
		#Rectangle
		length = entryLength
		height = entryHeight
		width = entryWidth
		volume = length * width * height
	elif shape == '3':
		#Oval
		diameter = entryWidth
		length = entryLength
		radius = diameter / 2.0
		area = float(math.pi * pow(radius, 2))
		area = 2.0 * radius * length + area
		height = entryHeight
		volume = area * height
	elif shape == '4':
		#Capsule
		length = entryLength
		diameter = entryWidth
		radius = diameter / 2
		volume = math.pi * pow(radius, 2)
		volume = 4 / 3 * radius + length * volume
	else:
		#Gives an error to user
		answerLabel.config(text='Choose a shape')
	
	#Changes value based on option box
	if measure == 'U.S. Gallons':
		volume = volume * 7.481
		volume = round(volume, 2)
		answerLabel.config(text=volume)
	elif measure == 'Imperial Gallons':
		volume = volume * 6.229
		volume = round(volume, 2)
		answerLabel.config(text=volume)
	elif measure == 'Liters':
		volume = volume * 28.317
		volume = round(volume, 2)
		answerLabel.config(text=volume)
	elif measure == 'Cubic Meters':
		volume = volume / 35.315
		volume = round(volume, 2)
		answerLabel.config(text=volume)
	elif measure == 'Cubic Feet':
		volume = round(volume, 2)
		answerLabel.config(text=volume)
	else:
		#Gives an error to user
		answerLabel.config(text='Choose a measurement')

#Sets options for option box
choices = ['U.S. Gallons', 'Imperial Gallons', 'Liters', 'Cubic Meters', 'Cubic Feet']

#Sets variable for option box
choicesVar = tk.StringVar()
choicesVar.set('Measurement')

#Options list
option = tk.OptionMenu(root, choicesVar, *choices)
option.grid(column=2, row=6)

#Sets variables for radio buttons
variable = tk.StringVar(root)
shapeButton = tk.StringVar()

#Length label
label1 = ttk.Label(root, text='Length')
label1.grid(column=2, row=0, pady=5)

#Width/diameter label
label2 = ttk.Label(root, text='Width/Diameter')
label2.grid(column=2, row=2)

#Height label
label3 = ttk.Label(root, text='Height')
label3.grid(column=2, row=4)

#Shape label
label4 = ttk.Label(root, text='Shape')
label4.grid(column=1, row=0)

#Cylinder button
button1 = ttk.Radiobutton(root, text='Cylindrical', variable=shapeButton, value='1')
button1.grid(column=1, row=1, sticky='w', padx=3)

#Rectangle button
button2 = ttk.Radiobutton(root, text='Rectangular', variable=shapeButton, value='2')
button2.grid(column=1, row=2, pady=5, sticky='w', padx=3)

#Oval button
button3 = ttk.Radiobutton(root, text='Ovular', variable=shapeButton, value='3')
button3.grid(column=1, row=3, pady=5, sticky='w', padx=3)

#Capsule button
button4 = ttk.Radiobutton(root, text='Capsule', variable=shapeButton, value='4')
button4.grid(column=1, row=4, pady=5, sticky='w', padx=3)

#Length entry
entry1 = tk.Entry(root, width = 20)
entry1.grid(column=2, row=1, sticky='ew', pady=5, padx=3)
entry1.insert(0,'0')

#Width/radius entry
entry2 = tk.Entry(root, width = 20)
entry2.grid(column=2, row=3, sticky='ew', pady=5, padx=3)
entry2.insert(0,'0')

#Height entry
entry3 = tk.Entry(root, width = 20)
entry3.grid(column=2, row=5, sticky='ew', pady=5, padx=3)
entry3.insert(0,'0')

#Answer text
answerLabel = ttk.Label(root, text='Answer', font=('Arial', 16))
answerLabel.grid(column=2, row=7, pady=5)

#Calculate button
calculate = ttk.Button(root, text="Calculate", command=calculateDef)
calculate.grid(column=2, row=8, pady=5)

#Right side padding
padLabel = ttk.Label(root, text=' ')
padLabel.grid(column=3, row=0)

#Left side padding
padLabel2 = ttk.Label(root, text=' ')
padLabel2.grid(column=0, row=0)

#Bottom padding
padLabel2 = ttk.Label(root, text=' ')
padLabel2.grid(column=0, row=9)

#Infinite loop
root.mainloop()