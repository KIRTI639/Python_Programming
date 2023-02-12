# WAP TO PRINT THE PRIME NUMBERS BETWEEN 1 TO 50
# a = int(input("Enter the number...."))
# count = 0
# i = 1
# while(a>=i):
#     if a%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Given number is a prime number...")
# else:
#     print("Not a prime number....")         


x = int(input("Starting number..."))
y = int(input("Ending number.."))
while(x<=y):
    a = x
    count = 0
    i = 1
    while(a>=i):
        if a%i==0:
            count+=1
        i+=1
    if count==2:
        print(f"{a} is a prime number...")
    # else:
    #     print(f"{a} is Not a prime number....")
    x+=1         


