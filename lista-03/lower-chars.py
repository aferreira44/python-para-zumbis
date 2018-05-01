chars = []
vowels = ['a', 'e', 'i', 'o', 'u']
count_cons = 0

for i in range(10):
  chars.append(input('Char %d: ' % i).lower())
  if chars[i] not in vowels:
    count_cons += 1

print('Consoantes: %d' % count_cons)