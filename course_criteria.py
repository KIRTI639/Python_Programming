# Admission to professional course in a college according to following conditions:
# Marks in Mathematics are greater than or equal to 60 and marks in physics is greater than or equal to 50 and marks in chemistry is 
# greater than or equal to 40

# OR

# Total marks in mathematics, physics and chemistry is greater than or equal to 200.

# OR

# Total marks in mathematics and physics are greater than or equal to 150.
# Marks of all three subjects will be entered through the keyboard.
# WAP to tell whether a student is qualifying for admission or not.

maths = int(input("Enter the Maths marks :"))
physics  = int(input("Enter the Physics marks : "))
chemistry = int(input("Enter the Chemistry marks :"))
if maths>=60 and physics>=50 and chemistry>=40:
    print("Student is eligible for Professional Course....🎈🎈🎈🎈wow")    
    print("🙂")
elif(maths+physics+chemistry)>=200:
    print("Student is eligible for Professional Course....🎈🎈🎈🎈wow")    
    print("🤩")
elif(maths+physics)>=150:
    print("Student is eligible for Professional Course....🎈🎈🎈🎈wow")    
    print("👀")
else:
    print("Sorry,You are not Eligible for Course....") 












# if maths>=60 or physics>=50 or chemistry>=40:
#     if ((maths+physics+chemistry)>=200) and ((maths+physics)>=150):
#         print("Student have the potential to take the professional course.")
#     else:
#         print("Not Eligible")    
# else:
#     print("Not Eligible for a professional course.")        
