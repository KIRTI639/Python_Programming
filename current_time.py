#  Write a Python program to display the current date and time

from datetime import datetime
a = datetime.now()
current_time = a.strftime("%H:%M:%S")
print(current_time)

# from datetime import datetime

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)