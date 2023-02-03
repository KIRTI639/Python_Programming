# The marks obtain by a student in 5 different subjects are input through keyboard. 
# The student gets the division as per the following rules:
# Percentage above or equal to 60- first division
# Percentage between 50 and 59- second division
# Percentage between 40 and 49 – third division
# Percentage below 40- fails.
a = int(input("Enter the Mathematices marks :"))
b = int(input("Enter the Chemistry marks :"))
c = int(input("Enter the  Physics marks :"))
d = int(input("Enter the English marks :"))
e = int(input("Enter the Hindi marks :"))
percentage =((a+b+c+d+e)/500)*100
if percentage>=60:
    print(f"You got 1st position...🎉🎊🎉 with {percentage} % marks.")
    print("Congrates,Maintain this position..")
elif percentage>=50 and percentage<=59:
    print(f"You got the second Position..🤩🤩 with {percentage}% marks.") 
    print("Good, Keep it up!!")
elif percentage>=40 and percentage<=49:
    print(f"You got the Third position..🙂 with {percentage}% marks.")
    print("Nice Performance, You can do it in a better way also.")
elif percentage<40 and percentage>=0:
    print(f"Oops!! You are Failed..😓😓 you got {percentage}% marks")
    print("Better Luck next Time..Hard work is the key to success..")
else:
    print("You entered the invalid marks..😡")              