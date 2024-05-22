punc='''!''@.""!%#()'''
s1='may!#ank@gmail.com'
s2=''
for x in s1:
    if x not in punc:
        s2+=x
        print(s2)

str='Hi everyone'

print (str.center(2,'*'))