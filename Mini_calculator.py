# WAP that implements the simple calculator that has following menu:
# Enter 1 to find the addition of two numbers.
# Enter 2 to find the subtraction of two numbers.
# Enter 3 to find the multiplication of two numbers.
# Enter 4 to find the division of two numbers.
# Enter 5 to find the square of a number.
# Enter 6 to find the cube of a number.
print("Enter 1 to find the addition of two numbers.")
print("Enter 2 to find the subtraction of two numbers.")
print("Enter 3 to find the multiplication of two numbers.")
print("Enter 4 to find the division of two numbers.")
print("Enter 5 to find the square of a number.")
print("Enter 6 to find the cube of a number.")
c =int(input())
match(c):
    case 1:
        a = int(input("Enter the  1st number :"))
        b = int(input("Enter the second number :"))
        print(f"Sum of the numbers is {a+b}.❣")
    case 2:
        a = int(input("Enter the  1st number :"))
        b = int(input("Enter the second number :"))
        print(f"Subtraction of the numbers is {a-b} ❤.")
    case 3:
        a = int(input("Enter the  1st number :"))
        b = int(input("Enter the second number :"))
        print(f"Multiplication of the numbers is {a*b} 🧡")
    case 4:
        a = int(input("Enter the  1st number :"))
        b = int(input("Enter the second number :"))
        print(f"Division of the numbers is {a/b}. 💙")
    case 5:
        a = int(input("Enter the number."))
        print(f"Square of the number is {a**2} 🖤")
    case 6:
        a = int(input("Enter the number."))
        print(f"Cube of the given number is {a**3}.💜")
    case _:
        print("😡😡 You didn't able to read properly whatever the instructions are given...")    
        
        


                   

   