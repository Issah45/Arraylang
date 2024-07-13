import sys, os

f = sys.argv[1]
code = open(f, "r").read()

array_normal = [0, 0, 0, 0]
variables = {}

def interprete(what, array=array_normal, position=0):
    mode = "code"
    loop = ""
    
    for letter in what:
        if mode == "code":
            # Arithmetic
            if letter == "+":
                array[position] += 1
            if letter == "-":
                array[position] -= 1
            
            # Pointer
            if letter == "a":
                array[position] += 20
            if letter == "b":
                array[position] += 10
            if letter == "c":
                array[position] += 5
            
            if letter == ">":
                position += 1
            if letter == "<":
                position -= 1
            
            if letter == "/":
                array[position+1] = array[position]
                array[position] = 0
                position += 1
            
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
            
            # Array
            if letter == "A":
                array.append(0)
            
            # Input
            if letter == "i":
                array[position] = int(input())
            
            # Output
            if letter == "o":
                for number in array:
                    print(number, end="")
            
            if letter == "*":
                print(position)
            if letter == "q":
                print(array[position])
            
            if letter == "N":
                print()

            if letter == "Я":
                print("H. inev", end="")
            if letter == "я":
                print("I. So. Grat", end="")
            
            if letter == "Q":
                for v in variables:
                    print(f"{v} = {variables[v]}")
            
            # Modal Commands
            if letter == "$":
                mode = "if"
            
            if letter == "(":
                loop = ""
                mode = "loop"

            if letter == "V":
                mode = "var_set"
            if letter == "B":
                mode = "var_get"
            
            if letter == '"':
                string = ""
                mode = "string"
            
            # Others
            if letter == "C":
                os.system("clear")
        
        # Modes
        elif mode == "if":
            if array[position + 1] == int(letter):
                array[position + 1] = 0
                array[position] = 1
            else:
                array[position + 1] = 0
                array[position] = 0
            mode = "code"
        
        elif mode == "string":
            if letter == "\"":
                print(string, end="")
                mode = "code"
            string += letter
        
        elif mode == "loop":
            if letter == ")":
                mode = "loop2"
            loop += letter
        
        elif mode == "loop2":
            for i in range(int(letter)):
                interprete(loop, array, position)

        elif mode == "var_set":
            variables[letter] = "N"
            mode = "var_set_2"
            l = letter

        elif mode == "var_set_2":
            if letter == "i":
                variables[l] = int(input())
            elif letter == "?":
                variables[l] = array[position]
            else:
                variables[l] = int(letter)
            mode = "code"

        elif mode == "var_get":
            n = variables[letter]
            array[position] = n
            mode = "code"

interprete(code)
