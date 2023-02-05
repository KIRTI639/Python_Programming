# WAP to find the greatest of three numbers entered through keyboard.
a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))
if a>b and a>c :
    print(f"{a} is the greatest number.")
elif b>a and b>c:
    print(f"{b} is the greatest number.")
elif c>a and c>b:
    print(f"{c} is the greatest number") 
elif a==b==c:
    print("All numbers are same.")

