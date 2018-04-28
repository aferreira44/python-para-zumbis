import math

area = float(input('Tamanho da área (m2): '))

litros = math.ceil(area / 3)
latas = math.ceil(litros / 18)

valor_total = latas * 80

print('Latas: %d, Valor Total: R$ %.2f' % (latas, valor_total))