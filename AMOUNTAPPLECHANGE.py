amount_money = int(input('Enter the amount of money you have: '))
price_apple = int(input('What is the price of the apple you wish to purchase?: '))
maximum_apple = int(amount_money/price_apple)
change = int((amount_money) - (price_apple*maximum_apple))
print(f"You can buy {maximum_apple} apples and your change is {change} pesos.")