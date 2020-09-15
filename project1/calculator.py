#this function handles the logic behind the calculator 
#it takes in a command parameter which is a string 
#we compare the string against the type of operation we want to do using string
#comparison through the if statements 
#we then do the operation that matches the one selected 
#we then return the solution to the operation we did in the variable to_return
#we are able to have the user input two numbers at a time because we split the string
#at spaces so we can get both values 
def calculator(command):
    to_return = 0
    if command == "addition":
        num1, num2 = input("Enter two numbers: ").split(" ")
        total = int(num1) + int(num2)
        to_return = total
    elif command == "subtraction":
        num1, num2 = input("Enter two numbers: ").split(" ")
        total = int(num1) - int(num2)
        to_return = total
    elif command == "multiplication":
        num1, num2 = input("Enter two numbers: ").split(" ")
        total = int(num1) * int(num2)
        to_return = total
    elif command =="division":
        num1, num2 = input("Enter two numbers: ").split(" ")
        total = int(num1) / int(num2)
        to_return = total
    return to_return

#handles the main program 
#we use a counter to have a while loop that will allow the user to do infinite 
#operations until they type the word quit which quits the calculator
def main():
    counter = 0
    while counter != 1:
         print("Choose an operation: " "\n" + " 1. Addition" "\n"+ " 2. Subtraction""\n"+ " 3. Multiplication" "\n" + " 4. Division" "\n" + " Quit to exit the calculator")
         commandName = input().lower()
         if commandName == "quit":
                counter = 1
                print("Bye bye")
         else:
             to_return = calculator(commandName)
             print(to_return)
             print("\n")
    
main()