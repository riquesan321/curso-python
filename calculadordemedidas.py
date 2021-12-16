n = int(input('DIGITE A DISTANCIA EM METROS: '))

mkm = n / 1000
mcm = n * 100
mmm = mcm * 1000


print('{} Metros convertido para KM é {}KM'.format(n,mkm))
print('{} Metros convertido para cm é {}cm'.format(n,mcm))
print('{} Metros convertido para mm é {}mm'.format(n,mmm))