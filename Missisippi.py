def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

x=input("Enter a string: ")
y=(most_frequent(x))
for i,j in y.items():
    print(i,'=',j)
