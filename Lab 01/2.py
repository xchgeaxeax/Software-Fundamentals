price = float(input('Enter a price: '))
price = price * (1 + 0.15)
price = round(price, 2)
print('GST applied: ' + str(price))
