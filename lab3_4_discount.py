def calculate_price(price, discount=10):
    new_price = price-(discount/100)*price
    return new_price


price = int(input("Enter the price"))
discount = input("Do you want to add a discount?")
if discount == "yes":
    a = int(input("Enter the required discount:"))
    print("The new price is:", calculate_price(price, a))

elif discount == "no":
    print("The new price is:", calculate_price(price))

else:
    print("wrong i/p")


