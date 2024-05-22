num=int(input('enter the number'))
psum=0
nsum=0
count=0

while count<num:
    n=int(input('enter the number'))
    if n >0:
            psum=psum + n
    else:
            nsum=nsum +n
    count=count + 1
print('+ive sum',psum)
print('-ive sum',nsum)