import sys

f = sys.argv[1]
code = open(f, "r").read()

standard = {
	1: " ", 2: "a",
	3: "b", 4: "c",
	5: "d", 6: "e",
	7: "f", 8: "g",
	9: "i", 10: "j",
	11: "k", 12: "l",
	13: "m", 14: "n",
	15: "o", 16: "p",
	17: "q", 18: "r",
	19: "s", 20: "t",
	21: "u", 22: "v",
	23: "w", 24: "x",
	25: "y", 26: "z",
	27: ".", 28: ",",
	29: "!", 30: "'",
	31: "\"", 32: "?",
	33: "#", 34: "h.inev",
	35: "+", 36: "-",
	37: "h", 38: "\n",
	39: "0", 40: "1",
	41: "2", 42: "3",
	43: "4", 44: "5",
	45: "6", 46: "7",
	47: "8", 48: "9"
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
		if letter == "p":
			print(position)
		if letter == "q":
			print(array[position])
		if letter == "o":
			for number in array:
				print(number, end="")
		
		# Displaying Things & Input
		if letter == ".":
			print(standard[array[position]], end="")
		if letter == "i":
			array[position] = int(input())
		if letter == "0":
			if array[position+1] == 0:
				array[position] = 1
			else:
				array[position] = 0
			array[position+1] = 0
		if letter == "e":
			array[position+1] = array[position]
			array[position] = 0
			position += 1
		
		# Math
		if letter == "v":
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

try:
	interprete(code)
except:
	print("there is something wrong with your (bad) code")
