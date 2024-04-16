def square(a):
    return a*a

x= map(square,[1,2,3,4])

for e in x:
    print (e,end=" ")



 #FILTER---> jab kisi iterable me se filter krna ho cond laga kr
print()

def fltr(x):
    if x % 3 ==0    :
        return x

y = filter(fltr,[1,2,3,4,5,6,7,8])
for e in y:
    print (e,end=" ")
print()

from functools import reduce

x = reduce (lambda a,b : a+b, [1,2,3,4,5])
print(x)