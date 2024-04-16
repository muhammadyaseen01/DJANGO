l1= []
#OR
l2 = list() # agr aise list obj lanaynge to no argument ya 1 argument de sakte srf
# both are the ways of initializing the list obj
print(l1,l2)

l3 = list() # making obj by giving no argument

# l4 = list(10) # by giving 1 argument --> lakin aise krne se error de rha h 
        # jab bhi list obj is tarah banaynge to argument me atmost 1 argument hi de sakte lakin wo iterable hona zarori h ---> is example me mene int pass kia jo k iterable nh is liyhe error

# l5 = list(1,3,6,8,4,2) # isme 1 se ziada argumentws pass krdiye h mene to error dega

l6 = list("10") # wahan par string pass ki h jo iterable h 
        # koi bhi iterable de sakte jitna bhi bara ho (iterble ho or argument 1 h)
print(l6)

l7 = list((1,2,3,4,5))
print(l7)
l8 = list(range (1,6,2))
print(l8)
