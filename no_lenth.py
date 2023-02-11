# Write a program to count the total number of digits in a number
# For example, the number is 75869, so the output should be 5.
# a = 75869
# b = str(a)
# c = len(b)
# print(f"Length of {a} is {c}.")

a = int(input("Enter the number..."))
count = 0
while(a>0):
    a = a//10
    # a = a%10
    count+=1
print(count)    
