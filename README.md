# New Arraylang
In New Arraylang, data is stored on a 16-bit 1 dimensional-stack (although it can be infinite with the `A` function). You can move through the stack and change values. Arraylang also has modes, which are used for loops, if statements, and variables\

## Commands
`>` Moves to the next cell\
`<` Moves to the previous cell\
`+` Increases the value of the current cell by 1\
`-` Reduces the value of the current cell by 1\
`a` Increases the value of the current cell by 20\
`b` Increases the value of the current cell by 10\
`c` Increases the value of the current cell by 5\
`*` Displays the current cell number\
`o` Displays the entire array\
`i` Gets an integer input\
`/` Moves the value of the current cell to the next cell, emptying the current cell, and moving the pointer to the next cell\
`\` Empties the current cell\
`w` Adds the current cell to the next cell, emptying the next cell\
`x` Subtracts the current cell to the next cell, emptying the next cell\
`y` Multiplies the current cell by the next cell, emptying the next cell\
`z` Divides the current cell by the next cell, emptying the next cell\
`q` Prints the current cell value\
`$` If the cell after the current cell is equal to the current cell's value, the current cell will be 1, if not the current cell will be zero, then the cell after the current cell will be set back to zero\
`A` adds an empty cell to the array\
`()` runs the code inside the brackets for a certain number of times e.g. `(++q)5`\
`V` variable setter (`Va5` means a = 5. If it is `Vai`, it will take an input and if it is `Va?`, then it will use the current cell as a variable)\
`B` variable getter (`Ba` sets the current cell to the variable a)\
`R` removes a variable (`Ra` removes the a variable)
`Q` prints out all variables and their values\
`N` prints out a new line\
`"` prints out a string e.g. `"Hello"` would print out Hello\
`{}` uses Tkinter to show an alert e.g. `{hello}` would make an alert saying hello\