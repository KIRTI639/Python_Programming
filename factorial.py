# WAP to print calculate the factorial of number entered through keyboard;
# while(True):
# a = int(input("Enter the number whose factorial you want to calculate..."))
# fact = 1
# b=a
# while(a>=1):
#     fact = fact*a
#     a-=1
# print(f"Factorial of {b} is {fact}...")    
# print(f"Factorial of is {fact}...")
    # b = input("If you wanted to continue press Y else N : ").lower()
    # if b=="y":
    #     continue
    # elif b=="n":
    #     break
    # else:
    #     print("Invalid input")

b = int(input("Enter the number...."))
fact = 1
for a in range(1,b+1):
    fact = fact*a
print(f"Factorial of {b} is {fact}...")    


