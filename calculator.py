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

#exponentiation formula
def number_expo(x, y):
   return x ** y

#modulus formula
def number_modulus(x, y):
   return x % y
    

def choose_operation():
  #asks user what operation they want to do
  print("Pick an option below.")
  print("0: stop program")
  print("1: addition")
  print("2: subtraction")
  print("3: multiplication")
  print("4: division")
  print("5: exponentiation")
  print("6: modulus")


def get_user_choice():
#gets the number for which operation the user chooses
  while True:
    
    try:
       user_choice = int(input("Enter choice here: "))
       if user_choice in [0, 1, 2, 3, 4, 5, 6]:
          return user_choice
       else:
          print("Please pick a valid option.")
    except ValueError:
       print("Please enter a number.")
       

while True:
  
#calls functions choose_operation and get_user_choice to get what operation the user wants to perform
  choose_operation()
  user_choice = get_user_choice()

#stops the while loop when user enters 0 as an option for user_choice
  if user_choice == 0:
     break
  
#makes sure the user enter's a number
  try:
#get's the numbers the user wants to use for the calculator
    print("")
    x = int(input("First number: "))
    y = int(input("Second number: "))
  except ValueError:
    print("")
    print("Invalid input! Please enter a number.")
    print("")
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
  elif user_choice == 5:
     print(x, " ** ", y, " = ", number_expo(x, y))
  elif user_choice == 6:
     print(x, " % ", y, " = ", number_modulus(x, y))

  print("")

print("Thank you for useing my calculator!")