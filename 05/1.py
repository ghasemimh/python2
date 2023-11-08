f_name = input("Enter your f_name: ")
l_name = input("Enter your l_name: ")
price = input("Enter the price of good: ")
reclaiming = input("Enter Reclaiming: ")

result = {"first_name": f_name , "last_name": l_name}

while True:
    try:
        price = float(price)
        break

    except:
        print("Error:( price of good is invalid")
        price = input("Enter the price of good again: ")


while True:
    try:
        reclaiming = int(reclaiming)
        break

    except:
        print("Error:( preclaiming is invalid")
        reclaiming = input("Enter the reclaiming again: ")


if reclaiming < 14:
    pass

elif price < 60:
    price *= 1.25

elif price < 180:
    price *= 1.4

else:
    print("no sale")

result["final price"] = price
print(result)