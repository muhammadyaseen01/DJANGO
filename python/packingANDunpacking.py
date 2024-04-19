# - is like destructuring in javascript
# - unpacking ---> jab list k elements ko hum alag alag variables me store krte hain
# - packing --->  jab variables ki value ko list me store krte



l1=[21,43,22,64,27,85,79]
# print (l1[4])

for i in l1:
    print(i)

x = 0
while x<=len(l1)-1:
    print (l1[x])
    x+=1

#Unpacking - 
# a,b,c,d,e,f,g = l1
# print (a," ",b," ",c," ",d," ",e," ",f," ",g)

l2 = [True, 3+4j,"abc",4.6,13]
a1,a2,a3,a4,a5 = l2
print(a1," ",a2," ",a3," ",a4," ",a5)

# Packing -
a,b,c,d,e = 87,114.78,"string",True,8+6j
print (a," ",b," ",c," ",d," ",e)
l3=[a,b,c,a,c,e,d,e]
print(l3)



