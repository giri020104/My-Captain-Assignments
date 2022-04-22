x=int(input('Enter number of terms: '))
ft=0
st=1
print(ft,st,end=" ")
for i in range(2,x):
  tt=ft+st
  ft=st
  st=tt
  print(tt,end=" ")
