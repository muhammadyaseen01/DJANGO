# - len() ---> return length of specified iterable
# - min() --->> return min value of elements
# - max() --->> return max value of elements
# - sum() ---> return sum of elements
# - sorted() ---> return a sorted list of elements
    # it always returns a list no matter which iterable i pass in argument

l1=[21,43,22,64,27,85,79]
a = len(l1)
print(a)

print (min(l1)) #it give min value by comparing all elements so it is imp that elements must be comparable (eg: str and int is not comparable so it gives error)
print (max(l1)) # same as min 
print (sum(l1)) # # it sum elements which can be add o/w it gives error (eg:int+str / str + complex)


# - SORTED()
l2 = sorted(l1) # it not change the original iterable
print(l1,l2)# it return the new list of elements
str1 = "avdsfg"
print(str1,sorted(str1))# it return a list of given iterable
tup = ('abs','def','geh')
print (tup,sorted(tup))

