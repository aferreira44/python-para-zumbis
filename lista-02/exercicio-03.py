peso = float(input('Peso: '))
excesso = multa = 0

if peso > 50:
  excesso = peso % 50
  multa = excesso * 4

print('Excesso: %.2f, Multa: %.2f' % (excesso, multa))