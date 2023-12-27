import sys

f = sys.argv[1]
code = open(f, "r").read()

standard = {
	1: "a", 2: "b", 3: "c",
	4: "d", 5: "e", 6: "f",
	7: "g", 8: "h", 9: "i",
	10: "j", 11: "k", 12: "l",
	13: "m", 14: "n", 15: "o",
	16: "p", 17: "q", 18: "r",
	19: "s", 20: "t", 21: "u",
	22: "v", 23: "w", 24: "x",
	25: "y", 26: "z", 27: "1",
	28: "2", 29: "3", 30: "4",
	31: "5", 32: "6", 33: "7",
	34: "8", 35: "9", 36: "0",
	37: " ", 38: ".", 39: ",",
	40: "!", 41: "#", 42: "$",
	43: "'", 44: "\"", 45: "|",
	46: "\n"
}

def interprete(what):
	array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	position = 0
	
	for letter in what:
		# Array Position
		if letter == "+":
			array[position] += 1
		if letter == "-":
			array[position] -= 1
		if letter == "a":
			array[position] += 20
		if letter == "b":
			array[position] += 10
		if letter == "c":
			array[position] += 5
		
		# Moving The Pointer
		if letter == ">":
			position += 1
		if letter == "<":
			position -= 1
		if letter == "*":
			print(position)
		if letter == "o":
			for number in array:
				print(number, end="")
		
		# Displaying Things & Input
		if letter == "&":
			print(standard[array[position]], end="")
		if letter == "i":
			array[position] = int(input())
		if letter == "0":
			if array[position+1] == 0:
				array[position] = 1
			else:
				array[position] = 0
			array[position+1] = 0
		if letter == "/":
			array[position+1] = array[position]
			array[position] = 0
			position += 1
		if letter == "q":
			print(array[position])
		
		# Math
		if letter == "\\":
			array.pop(position)
			position -= 1
			array.append(0)
		if letter == "w":
			array[position] = array[position] + array[position + 1]
			array[position + 1] = 0
		if letter == "x":
			array[position] = array[position] - array[position + 1]
			array[position + 1] = 0
		if letter == "y":
			array[position] = array[position] * array[position + 1]
			array[position + 1] = 0
		if letter == "z":
			array[position] = round(array[position] / array[position + 1])
			array[position + 1] = 0
		if letter == "A":
			array.append(0)
		
		if letter == "%":
			print("Arraylang Version 0.2")

interprete(code)
