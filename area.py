def areaofcircle(radius):
  import math
  if r>=0:
    area=math.pi*r*r
    return area
  else:
    return ('Radius of a circle cannot be negative')
r=float(input("Enter radius of a circle: "))
x=areaofcircle(r)
print(x)
