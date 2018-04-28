price_hour = float(input('Valor / Hora: R$ '))
hours = float(input('Horas Trabalhadas: '))

salary = price_hour * hours
ir, inss, sind = [salary * 0.11, salary * 0.08, salary * 0.05]
liquid = salary - ir - inss - sind


print('\n+Salario Bruto: R$ %.2f \n' % salary)

print('-IR: R$ %.2f' % ir)
print('-INSS: R$ %.2f' % inss)
print('-Sindicato: R$ %.2f \n' % sind)
print ('=Salário Líquido: R$ %.2f\n' % liquid)