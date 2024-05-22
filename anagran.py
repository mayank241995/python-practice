s1=input('enter the string 1')
s2=input('enter the string 2')

if len(s1)!=len(s2):
    print('not anagram')
else:
    for x in s2:
       if x not in s1:
           print('not anagrm')
           break;
    else:
       print("anagram")