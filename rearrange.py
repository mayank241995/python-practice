s=('EnTerString')
lower=''
upper=''
for x in s:
    print(x)
    if x.islower():
        lower+=x
    else:
        upper+=x
        str2=lower+upper
print('str ',str2)


