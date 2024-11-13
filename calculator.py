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
    

def choose_operation():
  #asks user what operation they want to do
  print("Pick an option below.")
  print("0: stop program")
  print("1: addition")
  print("2: subtraction")
  print("3: multiplication")
  print("4: division")

#get's user input for which kind of basic operation they want
  user_choice = int(input("Enter you're choice here: "))
  return user_choice


while True:
  
#calls function choose_operation to get what the user wants to do
  user_choice = choose_operation()
  
#Makes the choose_operation function loop if user_choice is not equal to a valid option
  while user_choice > 4 or user_choice < 0:
     print("")
     print("You entered an invalid option please pick a valid option.")
     print("")
     user_choice = choose_operation()

#stops the while loop when user enters 0 as an option for user_choice
  if user_choice == 0:
     break
  
#makes sure the user enter's a number
  try:
#get's the numbers the user wants to use for the calculator
    x = int(input("First number: "))
    y = int(input("Second number: "))
  except ValueError:
    print("Invalid input! Please enter a number.")
    continue

    

#using these print functions to make the output look cleaner
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

print("Thank you for useing my calculator!")