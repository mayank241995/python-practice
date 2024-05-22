pro =input('enter the name ')
prize=input('enter the prize')

total_len= len(pro)+len(prize)
dot='.'*(25-total_len)
print(pro+dot+prize)