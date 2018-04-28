a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

nums = [a, b, c]
maior = nums[0]

for n in nums:
  if n > maior:
    maior = n

print('O maior número é %.2f' % maior)