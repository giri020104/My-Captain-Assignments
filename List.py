lst1=[]
x=int(input("Enter number of elements required in the list"))
for i in range(x):
  f=int(input("Enter the element"))
  lst1.append(f)
lst2=[x for x in lst1 if x>=0]
print('Input: list1= {}Output: list2= {}'.format(lst1,lst2))
