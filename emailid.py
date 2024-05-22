emailid=input('enter the mail id')

iterate=emailid.find('@')

print('userid',emailid[:iterate])
print('doamail',emailid[iterate+1:])