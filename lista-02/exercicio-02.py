year = int(input('Year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print('É um ano bissexto!')
else:
  print('Não é um ano bissexto!')