import math
def price_of_pizza_unit(diameter,price):
    area=math.pi*(diameter/100/2)**2
    return price /area

pizza1=price_of_pizza_unit(30,15)
pizza2=price_of_pizza_unit(40,35)

if pizza1<pizza2:
    print("Pizza1 is cheaper:")
else:
    print("pizza2 is cheaper: ")
