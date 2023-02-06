# If cost price and selling price of an item is input through keyboard. Write a program to determine how much profit he made or how
# much loss he got.
cost_price = float(input("Enter the Cost Price :"))
selling_price = float(input("Enter the selling Price :"))
if selling_price>cost_price:
    Profit = selling_price - cost_price
    print(f"Profit, to the seller is {selling_price-cost_price}.")
    print(f"Seller get the profit of {round((Profit/cost_price)*100,2)} %")
else:
    Loss = cost_price - selling_price    
    print(f"Loss, to the seller is {cost_price-selling_price} . ")
    print(f"Seller get the loss of {round((Loss/cost_price)*100,2)}%")
