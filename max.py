num = int(input('enter the number'))
max = 0
count = 0

while count < num:
    n = int(input('enter the number'))
    if n >max:
        max=n
    count+=1
print(max)