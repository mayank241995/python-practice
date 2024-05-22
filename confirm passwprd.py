Pass=input('enter the pass')
repass= input('enter the password again')

if Pass == repass:
    print('same')
elif Pass.casefold()==repass.casefold():
    print('kindly check upper case')
else:
    print('not same ')