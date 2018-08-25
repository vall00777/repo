from math import tan, pi

n = int(input('Enter n: '))
a = float(input('Enter a: '))
num = n * a ** 2
deg = 180 / n 
rad = deg / 180 * pi
den = 4 * tan(rad) 
S = num / den  
print('Area =', S)
