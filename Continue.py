# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use &#39;continue&#39; statement.
for a in range(0,7):
    if((a==3) or (a == 6)):
        continue
    print(a)