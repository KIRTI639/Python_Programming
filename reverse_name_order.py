# Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them

a = input("Enter the first name :")
b = input("Enter the last name :")
c = a+" "+b
print (c)
print(c[-1::-1])
