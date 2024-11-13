print("Welcome to my calculator! Pick one of the options below to get started.")

# adds x and y
def add_numbers(x, y):
    return x + y

#subtracts x and y
def subtract_numbers(x, y):
    return x - y

#multiplys x and y
def multiply_numbers(x, y):
    return x * y

#divides x and y
def divide_numbers(x, y):
    if y == 0:
        return ("cannot divide by zero")
    else:
        return x // y
    

while True:
#asks user what operation they want to do
  print("Pick an option below.")
  print("0: stop program")
  print("1: addition")
  print("2: subtraction")
  print("3: multiplication")
  print("4: division")

#get's user input for which kind of basic operation they want
  user_choice = int(input("Enter you're choice here: "))

  if user_choice > 4 or user_choice < 0:
    print("You did not enter a valid option")
    break
  elif user_choice == 0:
     print("Bye, have a good day!")
     break

#get's the numbers the user wants to use for the calculator
  x = int(input("First number: "))
  y = int(input("Second number: "))

#the print statment on line 46 and 58 make it easier to read the output of the calculator in my opinion
  print("")

#using if statments to figure out what the user wants
  if user_choice == 1:
    print(x, " + ", y, " = ", add_numbers(x, y))
  elif user_choice == 2:
    print(x, " - ", y, " = ", subtract_numbers(x, y))
  elif user_choice == 3:
    print(x, " * ", y, " = ", multiply_numbers(x, y))
  elif user_choice == 4:
    print(x, " / ", y, " = ", divide_numbers(x, y))

  print("")