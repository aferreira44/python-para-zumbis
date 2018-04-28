a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

nums = [a, b, c]
menor = maior = nums[0]

for n in nums:
  if n > maior:
    maior = n
  if n < menor:
    menor = n

print('Maior: %.2f, Menor: %.2f' % (maior, menor))