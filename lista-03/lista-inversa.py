nums = []

for i in range(10):
  nums.append(float(input('Número %d: ' %i)))
  i += 1

for i in range(9, -1, -1):
  print('Número %d: %f' % (i, nums[i]))