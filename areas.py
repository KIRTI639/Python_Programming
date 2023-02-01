# Write a program that has following menu:
# Enter 1 to find the area of rectangle.
# Enter 2 to find the area of circle.
# Values for length and width of a rectangle and value of a radius of
# circle will be entered through keyboard.
print("Enter 1 for rectangle area...")
print("Enter 2 for circle area...")
num = int(input())
match(num):
    case 1:
        length = int(input("Enter the length of the rectangle :"))
        width = int(input("Enter the width of the Rectangle :"))
        Area_rectangle = length*width
        print(f"Area of the rectangle is {Area_rectangle}.")
    case 2:
        radius = int(input("Enter the Radius of the Circle :"))
        Area_circle = 3.14*radius*radius
        print(f"Area of the Circle is {Area_circle}.")