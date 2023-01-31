# Write a program that has following menu:
# Enter 1 to find out whether the entered number is even or odd.
# Enter 2 to find out whether the entered number is positive or negative.
print("Enter 1 to check even or odd number...")
print("Enter 2 to check Positive or Negative number...")
b = int(input("Enter number.."))
num = int(input("Enter the number.."))
match(b):
    case 1:
        print("Even number" if num %2==0 else "Odd number")
    case 2:    
        print("Positive number" if num>=0 else "Negative number")