a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if a + b <= c or a + c <= b or b + c <= a:
  print('Não é um triângulo')
elif a == b == c:
  print('É um triângulo equilátero')
elif a != b != c:
  print('É um triângulo escaleno')
else:
  print('É um triângulo isósceles')
