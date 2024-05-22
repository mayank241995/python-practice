amount = float(input('enter the numeber'))
if amount <=1000:
    disc=amount * 10/100
elif amount >1000 and amount <=5000:
    disc = amount * 20/100
else:
    disc = amount * 50/100

totaldisc=amount-disc
print(totaldisc)
