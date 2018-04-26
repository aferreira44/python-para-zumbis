price = float(input('Price:'))
percent = float(input('Discount %:')) / 100

discount = (price * percent)

print('Discount:', discount, 'Total:', price - discount)