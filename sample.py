# This is a comment
# Something that has quotes is a string which is text
# Something like this 12 is an int or integer
# Below is a variable
repeat = "R"

# Below is a loop, so while repeat equals "R" it will do everything below it
while repeat == "R":
# Below is the print function, which prints whatever you put in the parentheses
	print("Ask your mathematical question.")
	print("Possible options are: +, -, x")

# Below is the input function and whatever you type in after you see the prompt will be saved in the variable a
	a = input("Enter the operator you want to use: ")
# This is an if statement or a "conditional" so if what you type into the above prompt is "+" then it will do everything below it
	if a == "+":
		a1 = input("Enter the first number you want to add: ", )
		
# Below is the int() command which will turn "12" into 12
		i1 = int(a1)
		a2 = input("Enter the second number you want to add: ", )
		i2 = int(a2)
		print(i1 + i2)

	if a == "x":
		a1 = input("Enter the first number you want to multiply: ", )
		i1 = int(a1)
		a2 = input("Enter the second number you want to multiply: ", )
		i2 = int(a2)
		print(i1 * i2)
	
	if a == "-":
		a1 = input("What number would you like to start with? ", )
		i1 = int(a1)
		a2 = input(f"Enter the number you would like to subtract from {i1}? ")
	
		i2 = int(a2)
		print(i1 - i2)
		
# Hope this helped!