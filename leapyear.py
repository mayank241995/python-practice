year = int(input('enter the number'))

if year%400 == 0 and year%100 == 0:
    print('leap year')
elif year%400 == 0 and year%100 != 0:
    print('leap year')
else:
    print('not leap year')