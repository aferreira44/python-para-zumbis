'''
1 day = 1440 minutes

1 cigar => 10 minutes
144 cigars => 1440 minutes => 1 day
'''

cigar_amount = int(input('Cigarretes per day: '))
years = int(input('Years smoking: '))

days_lost = years * 365 * cigar_amount / 144

print('Smoker lost %.2f days' %days_lost)