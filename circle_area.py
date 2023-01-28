# Write a Python program which accepts the radius of a circle from the user and compute
#  the area


# radius = int(input("Enter the radius of the circle :"))
# area = 3.14*radius*radius
# print(f"Area of the circle is {area}.")


def area():
    r = int(input("Enter the radius :"))
    a = round((3.14*r*r),2)
    return a  
print("area is :", area()) 

