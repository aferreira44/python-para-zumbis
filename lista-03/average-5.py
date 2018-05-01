soma = 0
for i in range(5):  
  soma += int(input('Nota %d: ' %i))

print('Média: %.2f' % float(soma / 5))