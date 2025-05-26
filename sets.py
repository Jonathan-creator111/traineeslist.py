#difference
x={1,2,3,4,5,6,7}
y={5,6,7,8,9,10}
z=x-y
print(z)
z=x.difference(y)
print(z)
z=y.difference(x)
print(z)
#Union
z=x.union(y)
print(z)
#symetric difference
z=x.symmetric_difference(y)
print(z)
#intersection
z=x.intersection(y)
print(z)