# adds x and y
def add(x, y):
    return x + y

#subtracts x and y
def sub(x, y):
    return x - y

#multiplys x and y
def mult(x, y):
    return x * y

#divides x and y
def div(x, y):
    if y == 0:
        return ("cannot divide by zero")
    else:
        return x // y
    
    #get's user input for which kind of basic operation they want
choice = int(input("pick an option 1: add 2: subtract 3: multiply 4: divide : "))

#get's the numbers for the functions
x = int(input("Enter the first number for the calculator: "))
y = int(input("now enter the 2nd number: "))

#using if statments to figure out what the user wants
if choice == 1:
    print(x, " + ", y, " = ", add(x, y))
elif choice == 2:
    print(x, " - ", y, " = ", sub(x, y))
elif choice == 3:
    print(x, " * ", y, " = ", mult(x, y))
elif choice == 4:
    print(x, " / ", y, " = ", div(x, y))
else:
    print("you did not enter a correct option")