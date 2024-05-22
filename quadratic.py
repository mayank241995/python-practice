import math

a = int( input('enter a number'))
b = int( input('enter b number'))
c = int( input('enter c number'))

quard = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)

print(quard)